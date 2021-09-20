import random
import resource
from random import randrange
from threading import current_thread
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

# NOTE: Final agent should have same thresholds !
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
        self.all_actions = np.concatenate((self.do_nothing_action_vect, self.bus_actions62), axis=0)

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
        if np.all(action.redispatch == 0.0):
            return self.is_legal_bus_action(action, observation)
        else:
            return self.is_legal_redispatch_action(action, observation)

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
        # else
        # Pick greedy action if possible:
        sorted_actions_indexes = self.buckets.get_actions_sorted_by_value(observation)
        if sorted_actions_indexes.size > 0:
            index = 0
            while index < len(sorted_actions_indexes):
                action_index = sorted_actions_indexes[index]
                selected_action = self.action_space.from_vect(self.all_actions[action_index])
                if action_index == 0:
                    # Do nothing action
                    assert np.array_equal(self.all_actions[action_index], self.do_nothing_action.to_vect())
                    return selected_action, action_index
                is_legal = self.is_legal_action(selected_action, observation)
                if is_legal:
                    return selected_action, action_index
                index += 1

        # 1-depth simulation search of action with least rho.
        selected_action = self.action_space({})
        for action_vect in self.bus_actions62:
            action = self.action_space.from_vect(action_vect)
            is_legal = self.is_legal_action(action, observation)

            if not is_legal:
                continue

            obs, _, done, info_simulate = observation.simulate(action)
            observation._obs_env._reset_to_orig_state()
            assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

            if done:
                continue
            if obs.rho.max() < min_rho:
                min_rho = obs.rho.max()
                selected_action = action

        start_time = time.time()
        return selected_action, -1

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


random.seed(0)

MAX_MEMORY_GB = 32
TRAIN = True
start_time = time.time()
MAX_BATCH_ITERATIONS = 1000000
number_of_episodes = 1
NUM_CORE = cpu_count()
SAVE_BUCKET_INTERVAL = 1
print("CPU counts：%d" % NUM_CORE)

env_train = grid2op.make("l2rpn_icaps_2021_large_train", backend=LightSimBackend(), reward_class=RedispReward)
env_val = grid2op.make("l2rpn_icaps_2021_large_val", backend=LightSimBackend(), reward_class=RedispReward)
agent = Trainer(env_train, env_train.action_space)
print("start training...")
for i in range(number_of_episodes):
    print("Running episode:", i)
    # print(env_train.chronics_handler.get_name())
    env_seed = i
    agent_seed = i
    env_train.seed(env_seed)
    obs = env_train.reset()
    done = False
    reward = env_train.reward_range[0]
    first_env_since_overflow = None
    timestep = 0
    last_train_timestep = 0
    while not done:
        below_rho_threshold = obs.rho.max() < RHO_THRESHOLD
        act, action_index = agent.act(env_train, obs, reward, False, below_rho_threshold, done)

        timestep = env_train.nb_time_step
        obs, reward, done, info = env_train.step(act)
        # print(info)
        # print(below_rho_threshold)
        # print(first_env_since_overflow)
        # print(timestep)
        # print(info)
        print("obs.rho.max():", obs.rho.max())
        if TRAIN and done and timestep < 8061 and last_train_timestep < timestep and first_env_since_overflow != None:
            last_train_timestep = timestep
            env_train = first_env_since_overflow.copy()
            obs = env_train.get_obs()
            # print("Running training batch before timestep:", last_train_timestep, "---->")
            print("Start training batch ------>")
            # run_training_batch_full_search(agent, first_env_since_overflow)
            run_training_batch(agent, first_env_since_overflow)
            print("<----- Done training batch")

    print("Completed episode", i, ",number of timesteps:", timestep)
    GBmemory = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / (1024 * 1024)
    print("Memory used (GB):", GBmemory)
    if GBmemory > MAX_MEMORY_GB:
        break
    if i % SAVE_BUCKET_INTERVAL == 0 and TRAIN:
        agent.buckets.save_buckets_to_disk()

agent.buckets.save_buckets_to_disk()
print("FINISH!!")
