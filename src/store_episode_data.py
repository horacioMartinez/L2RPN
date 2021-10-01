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
from buckets import Buckets
from alarm import Alarm

# NOTE: Final agent should have same thresholds !
ALARM_RHO_THRESHOLD = 1.0
RHO_THRESHOLD = 1.0
RHO_THRESHOLD_RESET_REDISPATCH = 1.0
RHO_THRESHOLD_RECONNECT = 1.0


class Trainer(BaseAgent):
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

    def is_legal_redispatch_action(self, action, obs):
        adict = action.as_dict()
        if "redispatch" not in adict:
            assert False
        # TODO!
        return True

    def __init__(self, env, action_space):
        BaseAgent.__init__(self, action_space)
        self.action_space = action_space
        self.do_nothing_action = action_space({})

        bus_actions62_name = None
        bus_actions146_name = None
        bus_actions1255_name = None
        if "2021" in env.name:
            bus_actions62_name = "bus_actions62_2021.npy"
            bus_actions146_name = "bus_actions146_2021.npy"
            bus_actions1255_name = "bus_actions1255_2021.npy"
            redispatch_actions_name = "redispatch_actions_from_PARL_2021.npy"
        elif "2020" in env.name:
            bus_actions62_name = "bus_actions62_2020.npy"
            bus_actions146_name = "bus_actions146_2020.npy"
            bus_actions1255_name = "bus_actions1255_2020.npy"
            redispatch_actions_name = "redispatch_actions_from_PARL_2020.npy"
        else:
            assert False

        self.do_nothing_action_vect = np.array([self.do_nothing_action.to_vect()])
        self.bus_actions62 = np.load(os.path.join("./data/", bus_actions62_name))
        self.bus_actions146 = np.load(os.path.join("./data/", bus_actions146_name))
        self.bus_actions_62_146 = np.concatenate((self.bus_actions62, self.bus_actions146), axis=0)
        self.bus_actions1255 = np.load(os.path.join("./data/", bus_actions1255_name))
        self.bus_actions_62_146_1255 = np.concatenate((self.bus_actions_62_146, self.bus_actions1255), axis=0)
        self.redispatch_actions = np.load(os.path.join("./data/", redispatch_actions_name))
        self.all_actions = np.concatenate((self.do_nothing_action_vect, self.bus_actions_62_146), axis=0)
        print("bus_actions_62_146 actions SIN BUCKETS")

        buckets_save_file = "./data/buckets-" + str(len(self.all_actions)) + ".pkl"
        print("buckets_save_file:", buckets_save_file)
        self.buckets = Buckets(buckets_save_file)
        self.buckets.initalize(self.all_actions)

    def _reset_redispatch(self, observation):
        # From rl_agent
        if not np.all(observation.target_dispatch == 0.0):
            gen_ids = np.where(observation.gen_redispatchable)[0]
            gen_ramp = observation.gen_max_ramp_up[gen_ids]
            changed_idx = np.where(observation.target_dispatch[gen_ids] != 0.0)[0]
            redispatchs = []
            for idx in changed_idx:
                target_value = observation.target_dispatch[gen_ids][idx]
                value = min(abs(target_value), gen_ramp[idx])
                value = -1 * target_value / abs(target_value) * value
                redispatchs.append((gen_ids[idx], value))
            act = self.action_space({"redispatch": redispatchs})

            (
                obs_simulate,
                reward_simulate,
                done_simulate,
                info_simulate,
            ) = observation.simulate(act)
            observation._obs_env._reset_to_orig_state()

            assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

            if not done_simulate and obs_simulate is not None and not any(np.isnan(obs_simulate.rho)):
                if np.max(obs_simulate.rho) < RHO_THRESHOLD_RESET_REDISPATCH:
                    return act

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
        if np.all(action.redispatch == 0.0):
            return self.is_legal_bus_action(action, observation)
        else:
            return self.is_legal_redispatch_action(action, observation)

    def process_alarm_action(self, env, observation):
        # print("observation.is_alarm_illegal", observation.is_alarm_illegal)
        # print("observation.time_since_last_alarm", observation.time_since_last_alarm)
        # print("observation.last_alarm", observation.last_alarm)
        # print("observation.attention_budget", observation.attention_budget)
        # print("observation.was_alarm_used_after_game_over", observation.was_alarm_used_after_game_over)

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

    def act(self, env, observation, reward, training, below_rho_threshold, done=False):
        global start_time

        # print("--- %s seconds ---" % (time.time() - start_time))
        self._calc_sub_topo_dict(observation)
        some_line_disconnected = not np.all(observation.topo_vect != -1)

        current_time_step = env.nb_time_step

        # GET RHOS FOR ALARM STUFF >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        actions_rho = []
        if EPISODE_INFORMATION_STORAGE_THRESHOLD < observation.rho.max():
            for action_vect in self.all_actions:
                illegal_or_done = np.full(59, 99.0)
                action = self.action_space.from_vect(action_vect)
                is_legal = self.is_legal_action(action, observation)

                if not is_legal:
                    actions_rho.append(illegal_or_done)
                    continue

                obs, _, done, info_simulate = observation.simulate(action)
                observation._obs_env._reset_to_orig_state()
                assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

                if done:
                    actions_rho.append(illegal_or_done)
                    continue
                actions_rho.append(obs.rho)
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GET RHOS FOR ALARM STUFF

        if some_line_disconnected:
            # TODO: Mix reconnect action with other actions ??
            action = self._reconnect_action(observation)
            if action is not None:
                return action, actions_rho

        if below_rho_threshold:  # No overflow
            if not some_line_disconnected:
                action = self._reset_redispatch(observation)
                if action is not None:
                    # print("RESET REDISPATCH !")
                    return action, actions_rho
                action = self._reset_topology(observation)
                if action is not None:
                    # print("RESET TOPOLOGY !")
                    return action, actions_rho
            _, _, done, _ = observation.simulate(self.do_nothing_action)
            observation._obs_env._reset_to_orig_state()
            # TODO: Should we simulate like PARL and do something else if this would fail? Sometimes done returns true
            # assert not done
            return self.do_nothing_action, actions_rho

        o, _, d, info_simulate = observation.simulate(self.do_nothing_action)
        observation._obs_env._reset_to_orig_state()
        assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

        min_rho = o.rho.max() if not d else 9999

        selected_action = self.action_space({})
        min_rho = 99

        assert len(actions_rho) > 0
        action_index = 0
        for rho in actions_rho:
            if rho.max() < min_rho:
                min_rho = rho.max()
                selected_action = self.action_space.from_vect(self.all_actions[action_index])
            action_index += 1

        # < REMOVE ONCE WE KNOW ITS OK
        start_time = time.time()
        return selected_action, actions_rho


EPISODE_INFORMATION_STORAGE_THRESHOLD = 0.8
episode_data = None
disc_lines_before_cascade = []
disc_lines_in_cascade = []


# For each episode we store its name. For each timestep we store the timestep number and the features:
# Time of day, day of the week, week of the month?, month of the year?.
# Rhos of each line.
# Rhos of simulations of the 62 + 142 actions !!! << !!!!
# Bus of each element (-1 if disconnected)
# Loads/Generators
# Should timestep be a feature ???? It makes sense that it is one, because we should trigger alarms more agressevily if few remain!.

# obs = raw_obs.to_dict()

# loads = []
# for key in obs["loads"]:
#     loads.append(obs["loads"][key])
# loads = np.concatenate(loads)

# prods = []
# for key in obs["prods"]:
#     prods.append(obs["prods"][key])
# prods = np.concatenate(prods)

# lines_or = []
# for key in obs["lines_or"]:
#     lines_or.append(obs["lines_or"][key])
# lines_or = np.concatenate(lines_or)

# lines_ex = []
# for key in obs["lines_ex"]:
#     lines_ex.append(obs["lines_ex"][key])
# lines_ex = np.concatenate(lines_ex)

# features = np.concatenate([loads, prods, lines_or, lines_ex])
# features = np.array([features[i] for i in range(len(features)) if i not in self.zero_std])

# loads = []
# for key in ["q", "v"]:
#     loads.append(obs["loads"][key])
# loads = np.concatenate(loads)

# prods = []
# for key in ["q", "v"]:
#     prods.append(obs["prods"][key])
# prods = np.concatenate(prods)

# features = np.concatenate([loads, prods])
# features = np.array([features[i] for i in range(len(features)) if i not in self.zero_std])
# norm_features = (features - self.mean) / self.std

# rho = obs["rho"]
# time_info = np.array([raw_obs.month - 1, raw_obs.hour_of_day])

# x['day_of_week'] = raw_obs.day_of_week
# x['month'] = raw_obs.month
# x['hour_of_day'] = raw_obs.hour_of_day


# def useful_state(obs,value_multiplier):
#     selected_obs = np.hstack((obs.topo_vect,obs.line_status))
#     selected_obs = np.hstack((selected_obs,obs.load_p/100))#
#     selected_obs = np.hstack((selected_obs,obs.load_q/100))
#     selected_obs = np.hstack((selected_obs,obs.prod_p/100))
#     selected_obs = np.hstack((selected_obs,obs.prod_v/value_multiplier))
#     selected_obs = np.hstack((selected_obs,obs.rho))
#     # selected_obs = np.hstack((selected_obs,obs.day))
#     selected_obs = np.hstack((selected_obs,obs.hour_of_day/24))
#     selected_obs = np.hstack((selected_obs,obs.minute_of_hour/60))
#     # selected_obs = np.hstack((selected_obs,obs.day_of_week/7))
#     return selected_obs


def extract_timestep_features_for_alarm(
    episode_seed, env, obs, info, done, timestep, actions_rho, disc_lines_before_cascade
):
    if done:
        return None
    info = {}
    info["timestep"] = timestep
    info["disc_lines_before_cascade"] = disc_lines_before_cascade
    info["actions_rho"] = np.copy(actions_rho)
    info["rho"] = np.copy(obs.rho)
    info["topo_vect"] = np.copy(obs.topo_vect)
    info["line_status"] = np.copy(obs.line_status)
    info["load_p"] = np.copy(obs.load_p)
    info["load_q"] = np.copy(obs.load_q)
    info["load_v"] = np.copy(obs.load_v)
    info["gen_p"] = np.copy(obs.gen_p)
    info["gen_q"] = np.copy(obs.gen_q)
    info["gen_v"] = np.copy(obs.gen_v)
    info["year"] = obs.year
    info["month"] = obs.month
    info["day"] = obs.day  # 1,2,3,4,5, etc
    info["day_of_week"] = obs.day_of_week  # monday,tuesday,etc
    info["hour_of_day"] = obs.hour_of_day
    info["minute_of_hour"] = obs.minute_of_hour
    info["timestep_overflow"] = np.copy(obs.timestep_overflow)
    info["time_before_cooldown_line"] = np.copy(obs.time_before_cooldown_line)
    info["time_before_cooldown_sub"] = np.copy(obs.time_before_cooldown_sub)
    return info


def save_episode_data_to_disk(name, episode_seed):
    save_name = "data/episodes_data/episode_data-" + name + "-" + str(episode_seed) + ".pkl"
    if os.path.isfile(save_name):
        print("File already exists!!")
        assert False
    print("Saving episodes data to file:", save_name)
    with open(save_name, "wb") as f:
        pickle.dump(episode_data, f, pickle.HIGHEST_PROTOCOL)
    print("Saved episodes data to", save_name)


def store_information_for_alarm(episode_seed, env, obs, info, done, timestep, actions_rho):
    global episode_data
    global disc_lines_before_cascade
    global disc_lines_in_cascade

    episode_name = env.chronics_handler.get_name()
    if episode_data == None:
        print("BEGIN Storing information for episode: ", episode_name)
        assert timestep == 0
        episode_data = []
        disc_lines_before_cascade = []
        disc_lines_in_cascade = []
        return
    assert timestep > 0

    if done:
        disc_lines_in_cascade = list(np.where(info["disc_lines"] == 0)[0])
    else:
        disc_lines_before_cascade.append(list(np.where(info["disc_lines"] == 0)[0]))
        if (len(disc_lines_before_cascade)) > 4:
            disc_lines_before_cascade.pop(0)

    if not done and obs.rho.max() <= EPISODE_INFORMATION_STORAGE_THRESHOLD:
        assert len(actions_rho) == 0
        return

    we_won = False
    if done:
        we_won = len(info["exception"]) == 0
        if we_won:
            assert timestep == 8062

    disc_lines_before_cascade_copy = copy.deepcopy(disc_lines_before_cascade)
    disc_lines_in_cascade_copy = []
    if done and not we_won:
        disc_lines_in_cascade_copy = copy.deepcopy(disc_lines_in_cascade)

    if not done:
        assert len(actions_rho) > 0
        features = extract_timestep_features_for_alarm(
            episode_seed, env, obs, info, done, timestep, actions_rho, disc_lines_before_cascade_copy
        )

    if done:
        if we_won:
            timestep_information = {"timestep": timestep, "done": done, "we_won": we_won}
        else:
            timestep_information = {
                "timestep": timestep,
                "done": done,
                "we_won": we_won,
                "disc_lines_before_cascade": disc_lines_before_cascade_copy,
                "disc_lines_in_cascade": disc_lines_in_cascade_copy,
            }
    else:
        timestep_information = {
            "timestep": timestep,
            "features": features,
            "done": done,
        }

    episode_data.append(timestep_information)
    if done:
        save_episode_data_to_disk(episode_name, episode_seed)
        episode_data = None
        print("DONE Storing episode:", episode_name)


if len(sys.argv) < 4:
    print("Not enough arguments. USAGE: <Eval/Train/EvalInTraining> <NumScenarios> <#cpus> <id_cpu>")
    exit()

assert str(sys.argv[1]) == "Train" or str(sys.argv[1]) == "Eval" or str(sys.argv[1]) == "EvalInTraining"
TRAIN = str(sys.argv[1]) == "Train"
EVAL_TRAINING_DATA = str(sys.argv[1]) == "EvalInTraining"

number_of_scenarios = int(sys.argv[2])
NUMBER_OF_CPUS = int(sys.argv[3])
CPU_ID = int(sys.argv[4])

assert CPU_ID < NUMBER_OF_CPUS


random.seed(0)

MAX_MEMORY_GB = 32
start_time = time.time()
MAX_BATCH_ITERATIONS = 1000000
NUM_CORE = cpu_count()
SAVE_BUCKET_INTERVAL = 1
# SEED = CPU_ID
SEED = 0
print("CPU counts：%d" % NUM_CORE)

# env = grid2op.make("l2rpn_icaps_2021_large")
# nm_env_train, nm_env_val = env.train_val_split_random(pct_val=10.0)

env_train = grid2op.make("l2rpn_icaps_2021_large_train", backend=LightSimBackend(), reward_class=RedispReward)
env_val = grid2op.make("l2rpn_icaps_2021_large_val", backend=LightSimBackend(), reward_class=RedispReward)
agent = Trainer(env_train, env_train.action_space)

env_val.chronics_handler.seed(SEED)
env_val.chronics_handler.shuffle()
env_train.chronics_handler.seed(SEED)
env_train.chronics_handler.shuffle()

episode_true_index = 0
if TRAIN:
    assert False
else:
    episode_names = []
    survived_timesteps = []
    if EVAL_TRAINING_DATA:
        env = env_train
    else:
        assert False  # Only use training data for this!
        env = env_val
    print("Total number of chronics:", len(env.chronics_handler.chronics_used))
    for i in range(number_of_scenarios):
        # if i < 57:
        # env.reset()
        #            continue
        while episode_true_index < i * NUMBER_OF_CPUS + CPU_ID:
            env.reset()
            episode_true_index += 1
        env_seed = i + SEED
        agent_seed = i + SEED
        env.seed(env_seed)
        obs = env.reset()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Running episode:", i, "(", env.chronics_handler.get_name(), ")")
        episode_names.append(env.chronics_handler.get_name())

        done = False
        info = None
        timestep = 0
        reward = 0
        below_rho_threshold = True
        while not done:
            act, actions_rho = agent.act(env, obs, reward, False, below_rho_threshold, done)
            store_information_for_alarm(env_seed, env, obs, info, done, timestep, actions_rho)
            obs, reward, done, info = env.step(act)
            below_rho_threshold = obs.rho.max() < RHO_THRESHOLD
            under_attack = info["opponent_attack_line"] is not None and len(info["opponent_attack_line"]) > 0
            timestep = env.nb_time_step
            if done:
                survived_timesteps.append(timestep)
                print(info)

            assert not obs.is_alarm_illegal[0]  # Only true if last alarm was illegal
        store_information_for_alarm(env_seed, env, obs, info, done, timestep, actions_rho)

        print("Completed episode", i, ",number of timesteps:", timestep)
    print("---------------------------")
    print("Episodes:", episode_names)
    print("Num timesteps", len(survived_timesteps), " survived timesteps:", survived_timesteps)
    average = 0
    for survived_timestep in survived_timesteps:
        average += survived_timestep
    average = average / len(survived_timesteps)
    print("-> Average survived timesteps:", average)
    GBmemory = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / (1024 * 1024)
    print("Memory used (GB):", GBmemory)
    print("Environment used:", "env_train" if env == env_train else "env_val", "Seed used:", SEED)

if TRAIN:
    agent.buckets.save_buckets_to_disk()
print("FINISH!!")
