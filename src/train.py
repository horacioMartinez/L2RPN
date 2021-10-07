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
        global first_env_since_overflow

        # print("--- %s seconds ---" % (time.time() - start_time))
        self._calc_sub_topo_dict(observation)
        some_line_disconnected = not np.all(observation.topo_vect != -1)

        current_time_step = env.nb_time_step

        if below_rho_threshold:
            first_env_since_overflow = None
        else:
            if first_env_since_overflow == None:
                first_env_since_overflow = env.copy()

        if some_line_disconnected:
            # TODO: Mix reconnect action with other actions ??
            action = self._reconnect_action(observation)
            if action is not None:
                return action, -1

        if below_rho_threshold:  # No overflow
            if not some_line_disconnected:
                action = self._reset_redispatch(observation)
                if action is not None:
                    # print("RESET REDISPATCH !")
                    return action, -1
                action = self._reset_topology(observation)
                if action is not None:
                    # print("RESET TOPOLOGY !")
                    return action, -1
            _, _, done, _ = observation.simulate(self.do_nothing_action)
            observation._obs_env._reset_to_orig_state()
            # TODO: Should we simulate like PARL and do something else if this would fail? Sometimes done returns true
            # assert not done
            return self.do_nothing_action, -1

        # buckets.update_bucket(observation, sorted_actions)

        # NOTE: In final agent, if we are beow attention budget we shouldn't run the simulations for the alarm feature ! (Because we wouldn't trigger the alarm anyways.)
        alarm_action = None
        alarm_is_legal = observation.attention_budget[0] >= 1.0
        alarm_doesnt_overlap = (
            True  # observation.time_since_last_alarm[0] == -1 or observation.time_since_last_alarm[0] > 5
        )
        # We could avoid triggering alarm if we already did before the max/min timesteps. What happens if two alarms are triggered ???
        if alarm_is_legal and alarm_doesnt_overlap and observation.rho.max() > ALARM_RHO_THRESHOLD:
            alarm_action = self.process_alarm_action(env, observation)

        o, _, d, info_simulate = observation.simulate(self.do_nothing_action)
        observation._obs_env._reset_to_orig_state()
        assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

        min_rho = o.rho.max() if not d else 9999
        # print(
        #    "%s, heavy load, line-%d load is %.2f"
        #    % (str(observation.get_time_stamp()), observation.rho.argmax(), observation.rho.max())
        # )

        if training:
            banned_actions_indexes = []
            while True:
                action_index = self.buckets.select_action_Q_Learning(observation, banned_actions_indexes)
                selected_action = self.action_space.from_vect(self.all_actions[action_index])
                if action_index == 0:
                    # Do nothing action
                    assert np.array_equal(self.all_actions[action_index], self.do_nothing_action.to_vect())
                    return selected_action, action_index
                is_legal = self.is_legal_action(selected_action, observation)
                if is_legal:
                    return selected_action, action_index
                banned_actions_indexes.append(action_index)
        # else:
        #     # Pick greedy action if possible:
        #     sorted_actions_indexes = self.buckets.get_actions_sorted_by_value(observation)
        #     if sorted_actions_indexes.size > 0:
        #         index = 0
        #         while index < len(sorted_actions_indexes):
        #             action_index = sorted_actions_indexes[index]
        #             selected_action = self.action_space.from_vect(self.all_actions[action_index])
        #             if action_index == 0:
        #                 # Do nothing action
        #                 assert np.array_equal(self.all_actions[action_index], self.do_nothing_action.to_vect())
        #                 return self.combine_actions(alarm_action, selected_action, observation), action_index
        #             is_legal = self.is_legal_action(selected_action, observation)
        #             if is_legal:
        #                 return self.combine_actions(alarm_action, selected_action, observation), action_index
        #             index += 1

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

        start_time = time.time()
        return self.combine_actions(alarm_action, selected_action, observation), -1

    def get_action_from_index(self, observation, action_index):
        selected_action = self.action_space.from_vect(self.all_actions[action_index])
        if action_index == 0:
            # Do nothing action
            assert np.array_equal(self.all_actions[action_index], self.do_nothing_action.to_vect())
            return selected_action
        is_legal = self.is_legal_action(selected_action, observation)
        if is_legal:
            return selected_action
        return None

    def update_training(self, previous_obs, new_obs, done, action_index, reward):
        previous_bucket_hash = self.buckets.bucket_hash_of_observation(previous_obs)
        if done:
            bucket_hash = None
        else:
            bucket_hash = self.buckets.bucket_hash_of_observation(new_obs)

        self.buckets.update_bucket_action_values_Q_Learning(action_index, previous_bucket_hash, bucket_hash, reward)


def run_training_batch_full_search(agent, starting_env):
    agent.buckets.init_learning_batch()
    list_false = [False] * len(agent.all_actions)
    visited_step_action_indexes = []
    action_index_histories = []
    counter = 0
    while True:
        env_batch = starting_env.copy()
        obs = env_batch.get_obs()
        below_rho_threshold = obs.rho.max() < RHO_THRESHOLD
        max_rho = obs.rho.max()
        done = False
        # print("Start batch iteration --->")
        should_brake_batch = False
        step = 0
        action_index_history = []
        bad_brake = False
        while True:
            # print("·", obs.rho.max())
            if len(visited_step_action_indexes) < step + 1:
                visited_step_action_indexes.append(list_false.copy())
            timestep = env_batch.nb_time_step

            step_action_indexes = visited_step_action_indexes[step]
            is_there_next_step = len(visited_step_action_indexes) > step + 1
            # Check if next steps are all done, if so, set to True our step
            if is_there_next_step:
                if all(x for x in visited_step_action_indexes[step + 1]):
                    visited_step_action_indexes[step + 1] = list_false.copy()
                    completed_action_index = step_action_indexes.index(False)
                    step_action_indexes[completed_action_index] = True
                    # print(visited_step_action_indexes)
                    # print("Setting to True because child is full!")
                    bad_brake = True
                    break
            try:
                action_index = step_action_indexes.index(False)
            except:
                assert False
                break

            # Act according to action_index

            action = agent.get_action_from_index(obs, action_index)
            action_index_history.append(action_index)
            if action == None:
                done = True
                below_rho_threshold = False
            else:
                obs, r, done, info = env_batch.step(action)
                max_rho = obs.rho.max()
                below_rho_threshold = max_rho < RHO_THRESHOLD

            should_brake = False
            if done or below_rho_threshold:
                should_brake = True
                step_action_indexes[action_index] = True

            step += 1

            we_win_or_below_threhsold = False
            # print(visited_step_action_indexes)
            counter += 1
            if done:
                if timestep < 8061:
                    # print("We lost!")
                    we_win_or_below_threhsold = False
                else:
                    # print("We won!")
                    we_win_or_below_threhsold = True
            elif below_rho_threshold:
                # print("We got below threshold!")
                we_win_or_below_threhsold = True

            if we_win_or_below_threhsold:
                should_brake_batch = True
            if should_brake:
                break

            assert not should_brake
        # print("<----- End batch iteration")
        if not bad_brake:
            action_index_histories.append(action_index_history)
        # Once all root action indexes have been visited break:
        if should_brake_batch or all(x for x in visited_step_action_indexes[0]):
            print("WE WOOOOOOOOOOOOOOOOOOOOOOOON !! ")
            print("should_brake_batch:", should_brake_batch)
            break
    print("Action index histories:")
    for action_history in action_index_histories:
        print(action_history)


def find_lowest_rho_action_index(agent, starting_env):
    actions_rhos = []
    num_actions = len(agent.all_actions)
    i = 0
    highest = 999
    lowest = -highest
    while i < len(agent.all_actions):
        env_batch = starting_env.copy()
        obs = env_batch.get_obs()
        obs_TEMP = obs
        action_index = i
        action = agent.get_action_from_index(obs, action_index)
        if action == None:
            rho = highest * 2
        else:
            (
                obs_simulate,
                reward_simulate,
                done_simulate,
                info_simulate,
            ) = obs_TEMP.simulate(action)
            obs_TEMP._obs_env._reset_to_orig_state()
            assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

            obs, r, done, info = env_batch.step(action)
            if done:
                we_lose = len(info["exception"]) > 0
                if we_lose:
                    rho = highest
                else:
                    rho = lowest
            else:
                rho = obs.rho.max()
            if done_simulate:
                print("RHO: ", rho, " SIMULATED RHO: ", highest)
            else:
                print("RHO: ", rho, " SIMULATED RHO: ", obs_simulate.rho.max())

        actions_rhos.append(rho)
        i += 1
    print(actions_rhos)
    return actions_rhos.index(min(actions_rhos))


def run_training_batch_greedy_search(agent, starting_env):
    env_batch = starting_env.copy()
    obs = env_batch.get_obs()
    while True:
        lowest_rho_action_index = find_lowest_rho_action_index(agent, env_batch)
        action = agent.get_action_from_index(obs, lowest_rho_action_index)
        assert action != None
        obs, r, done, info = env_batch.step(action)
        below_rho_threshold = obs.rho.max() < RHO_THRESHOLD

        print("lowest_rho_action_index:", lowest_rho_action_index)
        if done:
            we_lose = len(info["exception"]) > 0
            if we_lose:
                print("WE LOOOOOOOOOOOOOOSE!")
                break
            else:
                print("WE WIIN!")
                break
        if below_rho_threshold:
            print("BELOW THRESHOLD !!!!!!!!!!!!!!!")
            break


def run_training_batch(agent, starting_env):
    batch_iteration = 0
    agent.buckets.init_learning_batch()
    while batch_iteration < MAX_BATCH_ITERATIONS:
        env_batch = starting_env.copy()
        obs = env_batch.get_obs()
        below_rho_threshold = obs.rho.max() < RHO_THRESHOLD
        max_rho = obs.rho.max()
        reward = 0
        done = False
        # print("Start batch iteration --->")
        steps = 0
        bucket_hashes = []
        action_indexes = []
        while True:
            action, action_index = agent.act(env_batch, obs, reward, True, below_rho_threshold, done)
            action_indexes.append(action_index)
            bucket_hashes.append(agent.buckets.bucket_hash_of_observation(obs))

            timestep = env_batch.nb_time_step
            previous_obs = obs
            obs, r, done, info = env_batch.step(action)
            steps += 1
            previous_max_rho = max_rho
            max_rho = obs.rho.max()
            below_rho_threshold = max_rho < RHO_THRESHOLD
            # print("max_rho:", max_rho)
            # print("selected_action_index:", action_index)
            reward = previous_max_rho - max_rho
            should_brake = False
            should_brake_batch = False
            we_win_or_below_threhsold = False
            if done:
                if timestep < 8061:
                    # print("We lost!")
                    bucket_hashes = []
                    action_indexes = []
                    reward = -999999
                    should_brake = True
                else:
                    # print("We won!")
                    reward = 999999
                    we_win_or_below_threhsold = True
                    should_brake = True
            elif below_rho_threshold:
                # print("We got below threshold!")
                reward = 999999  # The lower the amount of steps it took to exit, the better
                we_win_or_below_threhsold = True
                should_brake = True
            if action_index >= 0:
                agent.update_training(previous_obs, obs, done, action_index, reward)

            if we_win_or_below_threhsold:
                batch_iteration = MAX_BATCH_ITERATIONS

            if should_brake:
                break

            assert not should_brake

        batch_iteration += 1
        # print("<--- End batch iteration")
    agent.buckets.finalize_learning_batch(bucket_hashes, action_indexes)


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
    print("Start evaluating in training data")
    for i in range(number_of_scenarios):
        while episode_true_index < i * NUMBER_OF_CPUS + CPU_ID:
            env_train.reset()
            episode_true_index += 1

        print("Running episode:", i, "(", env_train.chronics_handler.get_name(), ")")
        env_seed = i + SEED
        agent_seed = i + SEED
        env_train.seed(env_seed)
        obs = env_train.reset()
        done = False
        reward = env_train.reward_range[0]
        first_env_since_overflow = None
        timestep = 0
        last_train_timestep = 0
        while not done:
            below_rho_threshold = obs.rho.max() < RHO_THRESHOLD
            act, action_index = agent.act(env_train, obs, reward, True, below_rho_threshold, done)

            timestep = env_train.nb_time_step
            obs, reward, done, info = env_train.step(act)
            if done:
                print(info)
            # print(below_rho_threshold)
            # print(first_env_since_overflow)
            # print(timestep)
            # print(info)
            print("obs.rho.max():", obs.rho.max())
            if done and timestep < 8061 and last_train_timestep < timestep and first_env_since_overflow != None:
                last_train_timestep = timestep
                env_train = first_env_since_overflow.copy()
                obs = env_train.get_obs()
                # print("Running training batch before timestep:", last_train_timestep, "---->")
                print("Start training batch ------>")
                run_training_batch_greedy_search(agent, first_env_since_overflow)
                # run_training_batch_full_search(agent, first_env_since_overflow)
                # run_training_batch(agent, first_env_since_overflow)
                print("<----- Done training batch")

        print("Completed episode", i, ",number of timesteps:", timestep)
        GBmemory = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / (1024 * 1024)
        print("Memory used (GB):", GBmemory)
        if GBmemory > MAX_MEMORY_GB:
            break
        if i % SAVE_BUCKET_INTERVAL == 0:
            agent.buckets.save_buckets_to_disk()
else:
    episode_names = []
    survived_timesteps = []
    alarm_scores = []
    if EVAL_TRAINING_DATA:
        env = env_train
    else:
        env = env_val
    print("Total number of chronics:", len(env.chronics_handler.chronics_used))
    under_attack_count = 0
    not_under_attack_count = 0
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
        below_rho_threshold = True
        # ALARM >
        alarm = Alarm(env)
        disc_lines_before_cascade = []
        disc_lines_in_cascade = []
        # < ALARM
        while not done:
            act, action_index = agent.act(env, obs, reward, False, below_rho_threshold, done)
            action_timestep = timestep
            obs, reward, done, info = env.step(act)
            below_rho_threshold = obs.rho.max() < RHO_THRESHOLD
            under_attack = info["opponent_attack_line"] is not None and len(info["opponent_attack_line"]) > 0
            timestep = env.nb_time_step

            # if under_attack or not below_rho_threshold:
            # print(">>>>>>>")
            # print("Timestep:", timestep)
            # print("obs.rho.max():", obs.rho.max())
            # if under_attack:
            #    print("UNDER ATTACK:")
            #    print(info["opponent_attack_line"])
            # print(obs.topo_vect)
            if done:
                if timestep < 8060:
                    if under_attack:
                        under_attack_count += 1
                    else:
                        not_under_attack_count += 1

                survived_timesteps.append(timestep)
                print(info)

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
            # if not done:
            # assert math.isclose(alarm.budget, obs.attention_budget, rel_tol=1e-3)
            # < ALARM

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
    print("under_attack_count:", under_attack_count)
    print("not_under_attack_count:", not_under_attack_count)

if TRAIN:
    agent.buckets.save_buckets_to_disk()
print("FINISH!!")
