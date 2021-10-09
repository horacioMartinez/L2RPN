from enum import Flag
from mmap import ALLOCATIONGRANULARITY
import copy
import pickle
import math
import sys
import random
import resource
from random import randrange, seed
from threading import current_thread
from grid2op import Observation
from lightsim2grid import LightSimBackend
import os
import time
import grid2op
import numpy as np
from multiprocessing import cpu_count
from grid2op.Environment import SingleEnvMultiProcess
from grid2op.Reward.BaseReward import BaseReward
from grid2op.Reward import RedispReward
from grid2op.Agent import BaseAgent
from scipy.optimize.optimize import bracket
from alarm import Alarm

ALARM_RHO_THRESHOLD = 0.0
RHO_THRESHOLD = 1.0
RHO_THRESHOLD_RECONNECT = 1.0


class Agent(BaseAgent):
    def is_legal_bus_action(self, action, obs):
        adict = action.as_dict()
        if "change_bus_vect" not in adict:
            assert False
        substation_to_operate = int(adict["change_bus_vect"]["modif_subs_id"][0])
        if obs.time_before_cooldown_sub[substation_to_operate]:
            return False
        for line in [
            eval(key)
            for key, val in adict["change_bus_vect"][str(substation_to_operate)].items()
            if "line" in val["type"]
        ]:
            if obs.time_before_cooldown_line[line] or not obs.line_status[line]:
                return False
        return True

    def __init__(self, env, action_space, this_directory_path="./"):
        BaseAgent.__init__(self, action_space)
        self.action_space = action_space
        self.do_nothing_action = action_space({})

        self.do_nothing_action_vect = np.array([self.do_nothing_action.to_vect()])
        self.bus_actions62 = np.load(os.path.join("./data/bus_actions62_2021.npy"))
        self.bus_actions146 = np.load(os.path.join("./data/bus_actions146_2021.npy"))
        self.bus_actions_62_146 = np.concatenate((self.bus_actions62, self.bus_actions146), axis=0)
        self.all_actions = np.concatenate((self.do_nothing_action_vect, self.bus_actions_62_146), axis=0)
        self.previous_rho_for_alarm = None

    def _reset_topology(self, observation):
        if np.max(observation.rho) < 0.95:
            offset = 0
            for sub_id, sub_elem_num in enumerate(observation.sub_info):
                sub_topo = self.sub_topo_dict[sub_id]

                if sub_id == 28:
                    sub28_topo = np.array([2, 1, 2, 1, 1])
                    if (
                        not np.all(sub_topo.astype(int) == sub28_topo.astype(int))
                        and observation.time_before_cooldown_sub[sub_id] == 0
                    ):
                        sub_id = 28
                        act = self.action_space({"set_bus": {"substations_id": [(sub_id, sub28_topo)]}})

                        (
                            obs_simulate,
                            reward_simulate,
                            done_simulate,
                            info_simulate,
                        ) = observation.simulate(act)
                        observation._obs_env._reset_to_orig_state()
                        assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]
                        if not done_simulate and obs_simulate is not None and not any(np.isnan(obs_simulate.rho)):
                            if np.max(obs_simulate.rho) < 0.95:
                                return act
                    continue

                if np.any(sub_topo == 2) and observation.time_before_cooldown_sub[sub_id] == 0:
                    sub_topo = np.where(sub_topo == 2, 1, sub_topo)  # bus 2 to bus 1
                    sub_topo = np.where(sub_topo == -1, 0, sub_topo)  # don't do action in bus=-1
                    reconfig_sub = self.action_space({"set_bus": {"substations_id": [(sub_id, sub_topo)]}})

                    (
                        obs_simulate,
                        reward_simulate,
                        done_simulate,
                        info_simulate,
                    ) = observation.simulate(reconfig_sub)
                    observation._obs_env._reset_to_orig_state()

                    assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

                    if not done_simulate:
                        assert np.any(obs_simulate.topo_vect != observation.topo_vect)  # have some impact

                    if not done_simulate and obs_simulate is not None and not any(np.isnan(obs_simulate.rho)):
                        if np.max(obs_simulate.rho) < 0.95:
                            return reconfig_sub

        if np.max(observation.rho) >= 1.0:
            sub_id = 28
            sub_topo = self.sub_topo_dict[sub_id]
            if np.any(sub_topo == 2) and observation.time_before_cooldown_sub[sub_id] == 0:
                sub28_topo = np.array([1, 1, 1, 1, 1])
                act = self.action_space({"set_bus": {"substations_id": [(sub_id, sub28_topo)]}})

                (
                    obs_simulate,
                    reward_simulate,
                    done_simulate,
                    info_simulate,
                ) = observation.simulate(act)
                observation._obs_env._reset_to_orig_state()
                assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]
                if not done_simulate and obs_simulate is not None and not any(np.isnan(obs_simulate.rho)):
                    if np.max(obs_simulate.rho) < 0.99:
                        return act

    def _calc_sub_topo_dict(self, observation):
        offset = 0
        self.sub_topo_dict = {}
        for sub_id, sub_elem_num in enumerate(observation.sub_info):
            sub_topo = observation.topo_vect[offset : offset + sub_elem_num]
            offset += sub_elem_num
            self.sub_topo_dict[sub_id] = sub_topo

    def _reconnect_action(self, observation):
        disconnected = np.where(observation.line_status == False)[0].tolist()

        for line_id in disconnected:
            if observation.time_before_cooldown_line[line_id] == 0:
                action = self.action_space({"set_line_status": [(line_id, +1)]})
                simulation_obs, _, _, _ = observation.simulate(action)
                observation._obs_env._reset_to_orig_state()

                if (
                    np.max(observation.rho) < RHO_THRESHOLD_RECONNECT
                    and np.max(simulation_obs.rho) >= RHO_THRESHOLD_RECONNECT
                ):
                    continue

                return action

    def is_legal_action(self, action, observation):
        if action == self.do_nothing_action:
            return True
        return self.is_legal_bus_action(action, observation)

    def process_alarm_action(self, env, observation, alarm_features):
        alarms_lines_area = env.alarms_lines_area
        alarms_area_names = env.alarms_area_names
        zone_for_each_lines = alarms_lines_area
        line_most_overloaded = np.argmax(observation.rho)
        line_name = observation.name_line[line_most_overloaded]
        # Some lines are in more than one area, which one to chose ?
        zone_name = zone_for_each_lines[line_name][0]
        #'east' = 0, 'middle' = 1, 'west' = 2
        zone_index = [alarms_area_names.index(zone_name)]
        alarm_action = self.action_space({"raise_alarm": zone_index})
        return alarm_action

    def combine_actions(self, actionA, actionB, observation):
        if actionA == None:
            return actionB
        if actionB == None:
            return actionA
        combined_action = actionA + actionB
        (
            obs_simulate,
            reward_simulate,
            done_simulate,
            info_simulate,
        ) = observation.simulate(combined_action)
        observation._obs_env._reset_to_orig_state()
        assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]
        return combined_action

    def extract_alarm_features(self, obs):
        if self.previous_rho_for_alarm is None:
            feature_rho_delta = np.zeros_like(obs.rho)
        else:
            feature_rho_delta = self.previous_rho_for_alarm - obs.rho

        processed_features = np.array([])

        # feature_actions_rho = features["actions_rho"]
        feature_rho = np.copy(obs.rho)
        feature_topo_vect = np.copy(obs.topo_vect)
        feature_load_p = np.copy(obs.load_p)
        feature_load_q = np.copy(obs.load_q)
        feature_load_v = np.copy(obs.load_v)
        feature_gen_p = np.copy(obs.gen_p)
        feature_gen_q = np.copy(obs.gen_q)
        feature_gen_v = np.copy(obs.gen_v)
        feature_month = obs.month
        feature_day = obs.day
        feature_day_of_week = obs.day_of_week
        feature_hour_of_day = obs.hour_of_day
        feature_minute_of_hour = obs.minute_of_hour
        feature_timestep_overflow = np.copy(obs.timestep_overflow)
        feature_time_before_cooldown_line = np.copy(obs.time_before_cooldown_line)
        feature_time_before_cooldown_sub = np.copy(obs.time_before_cooldown_sub)
        feature_time_next_maintenance = np.copy(obs.time_next_maintenance)

        processed_features = (
            np.concatenate(
                (
                    # [feature_under_attack],
                    # [feature_attack_duration],
                    # [feature_timesteps_since_last_attack],
                    # [feature_timesteps_since_ongoing_attack_started],
                    feature_topo_vect,
                    feature_load_p,
                    feature_load_q,
                    feature_load_v,
                    feature_gen_p,
                    feature_gen_q,
                    feature_gen_v,
                    feature_rho,
                    feature_rho_delta,
                    feature_timestep_overflow,
                    feature_time_before_cooldown_line,
                    feature_time_before_cooldown_sub,
                    feature_time_next_maintenance,
                    [feature_month],
                    [feature_day],
                    [feature_day_of_week],
                    [feature_hour_of_day],
                    [feature_minute_of_hour],
                )
            )
            .flatten()
            .astype(np.float32)
        )

        assert not np.isnan(processed_features).any()
        assert len(processed_features) == 690
        return processed_features

    def act(self, observation, reward, done):
        env = observation._obs_env

        self._calc_sub_topo_dict(observation)
        current_time_step = env.nb_time_step

        # ALARM >
        # TODOOOOOOOOOOOOOOOOOOOOOOOOOOOOO: VERIFICAR QUE ESTAN BIEN LOS FEATURES; VER QUE ESTEN EN EL MISMO ORDEN Y DEN LO MISMO QUE EN STORE_EPISODE_DATA
        # TODOOOOOOOOOOOOOOOOOOOOOOOOOOOOO: VERIFICAR QUE ESTAN BIEN LOS FEATURES; VER QUE ESTEN EN EL MISMO ORDEN Y DEN LO MISMO QUE EN STORE_EPISODE_DATA
        alarm_action = None
        alarm_is_legal = observation.attention_budget[0] >= 1.0
        if alarm_is_legal and observation.rho.max() > ALARM_RHO_THRESHOLD:
            alarm_features = self.extract_alarm_features(observation)
            alarm_action = self.process_alarm_action(env, observation, alarm_features)
        self.previous_rho_for_alarm = observation.rho
        # < ALARM

        some_line_disconnected = not np.all(observation.topo_vect != -1)

        if some_line_disconnected:
            # TODO: Mix reconnect action with other actions ??
            action = self._reconnect_action(observation)
            if action is not None:
                return self.combine_actions(alarm_action, action, observation)

        below_rho_threshold = observation.rho.max() < RHO_THRESHOLD

        if below_rho_threshold:  # No overflow
            if not some_line_disconnected:
                action = self._reset_topology(observation)
                if action is not None:
                    return self.combine_actions(alarm_action, action, observation)
            _, _, done, _ = observation.simulate(self.do_nothing_action)
            observation._obs_env._reset_to_orig_state()
            # TODO: Should we simulate like PARL and do something else if this would fail? Sometimes done returns true
            # assert not done
            action = self.do_nothing_action
            return self.combine_actions(alarm_action, action, observation)

        o, _, d, info_simulate = observation.simulate(self.do_nothing_action)
        observation._obs_env._reset_to_orig_state()
        assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

        min_rho = o.rho.max() if not d else 9999

        # 1-depth simulation search of action with least rho.
        selected_action = self.action_space({})
        min_rho = 99
        for action_vect in self.all_actions:
            action = self.action_space.from_vect(action_vect)
            is_legal = self.is_legal_action(action, observation)

            if not is_legal:
                continue

            obs, _, done, info_simulate = observation.simulate(action)
            observation._obs_env._reset_to_orig_state()
            assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]
            if done:
                continue

            count_disconnected_sim = len(obs.rho) - np.count_nonzero(obs.rho)
            THRESHOLD_MAX_COUNT_DISCONNECTED_SIMUL = 3
            if count_disconnected_sim >= THRESHOLD_MAX_COUNT_DISCONNECTED_SIMUL:
                continue

            if obs.rho.max() < min_rho:
                min_rho = obs.rho.max()
                selected_action = action

        return self.combine_actions(alarm_action, selected_action, observation)


if len(sys.argv) < 4:
    print("Not enough arguments. USAGE: <Eval/Train/EvalInTraining> <NumScenarios> <#cpus> <id_cpu>")
    exit()

assert str(sys.argv[1]) == "Eval" or str(sys.argv[1]) == "EvalInTraining"

EVAL_TRAINING_DATA = str(sys.argv[1]) == "EvalInTraining"

number_of_scenarios = int(sys.argv[2])
NUMBER_OF_CPUS = int(sys.argv[3])
CPU_ID = int(sys.argv[4])

assert CPU_ID < NUMBER_OF_CPUS


SEED = 0
random.seed(0)

env_train = grid2op.make("l2rpn_icaps_2021_large_train", backend=LightSimBackend(), reward_class=RedispReward)
env_val = grid2op.make("l2rpn_icaps_2021_large_val", backend=LightSimBackend(), reward_class=RedispReward)
agent = Agent(env_train, env_train.action_space)

env_val.chronics_handler.seed(SEED)
env_val.chronics_handler.shuffle()
env_train.chronics_handler.seed(SEED)
env_train.chronics_handler.shuffle()

episode_true_index = 0
episode_names = []
survived_timesteps = []
alarm_scores = []

if EVAL_TRAINING_DATA:
    env = env_train
else:
    env = env_val
print("Total number of chronics:", len(env.chronics_handler.chronics_used))
for i in range(number_of_scenarios):
    while episode_true_index < i * NUMBER_OF_CPUS + CPU_ID:
        env.reset()
        episode_true_index += 1
    env_seed = i + SEED
    agent_seed = i + SEED
    env.seed(env_seed)
    obs = env.reset()
    ############### RUN SPECFIC EPISODE #################
    # env_train.chronics_handler.reset()
    # episode_seed = 126
    # episode_id = np.where(
    #    env_train.chronics_handler.real_data.subpaths
    #    == "/home/horacio/data_grid2op/l2rpn_icaps_2021_large_train/chronics/Scenario_august_238"
    # )[0][0]
    # print("episode_id:", episode_id)
    # env.seed(episode_seed)
    # env.set_id(episode_id)
    # env.reset()
    #####################################################
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Running episode:", i, "(", env.chronics_handler.get_name(), ")")
    episode_names.append(env.chronics_handler.get_name())
    done = False
    info = None
    timestep = 0
    reward = 0
    # ALARM >
    alarm = Alarm(env)
    disc_lines_before_cascade = []
    disc_lines_in_cascade = []
    # < ALARM
    while not done:
        act = agent.act(obs, reward, done)
        action_timestep = timestep
        obs, reward, done, info = env.step(act)
        timestep = env.nb_time_step
        if done:
            survived_timesteps.append(timestep)

        assert not obs.is_alarm_illegal[0]  # Only true if last alarm was illegal
        # ALARM >
        if done:
            disc_lines_in_cascade = list(np.where(info["disc_lines"] == 0)[0])
        else:
            disc_lines_before_cascade.append(list(np.where(info["disc_lines"] == 0)[0]))
            if (len(disc_lines_before_cascade)) > 4:
                disc_lines_before_cascade.pop(0)
        alarm_action = None
        if np.any(act.raise_alarm):
            alarm_action = act.raise_alarm
        if action_timestep > 0:
            alarm.update_timestep(action_timestep, alarm_action)
    # ALARM >
    we_won = len(info["exception"]) == 0
    if we_won:
        assert timestep == 8062
    alarm_score = alarm.compute_score(timestep, we_won, disc_lines_before_cascade, disc_lines_in_cascade)
    alarm_scores.append(alarm_score)
    print("ALARM SCORE:", alarm_score)
    # < ALARM
    print("Completed episode", i, ",number of timesteps:", timestep)

print("---------------------------")
print("Episodes:", episode_names)
print("Num timesteps", len(survived_timesteps), " survived timesteps:", survived_timesteps)
print("Alarm scores", alarm_scores)
average = 0
for survived_timestep in survived_timesteps:
    average += survived_timestep
average = average / len(survived_timesteps)
print("-> Average survived timesteps:", average)
average_alarm_score = 0
for alarm_score in alarm_scores:
    average_alarm_score += alarm_score
average_alarm_score = average_alarm_score / len(alarm_scores)
print("-> Average alarm score:", average_alarm_score)
GBmemory = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / (1024 * 1024)
print("Memory used (GB):", GBmemory)
print("Environment used:", "env_train" if env == env_train else "env_val", "Seed used:", SEED)
print("FINISH!!")
