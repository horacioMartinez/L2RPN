import random
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
        self.all_actions = np.concatenate(
            (self.do_nothing_action_vect, self.bus_actions_62_146_1255, self.redispatch_actions), axis=0
        )
        self.buckets = Buckets()
        self.buckets.initalize(self.all_actions)
        self.previous_bucket_hash = None
        self.previous_action_index = None

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

    def initialize_for_training_episode(self):
        self.previous_bucket_hash = None
        self.previous_action_index = None

    def act(self, env, observation, reward, training, below_rho_threshold, done=False):
        global start_time
        global first_env_since_overflow

        print("--- %s seconds ---" % (time.time() - start_time))
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
                return action

        if below_rho_threshold:  # No overflow
            if not some_line_disconnected:
                action = self._reset_redispatch(observation)
                if action is not None:
                    print("RESET REDISPATCH !")
                    return action
                action = self._reset_topology(observation)
                if action is not None:
                    print("RESET TOPOLOGY !")
                    return action
            _, _, done, _ = observation.simulate(self.do_nothing_action)
            observation._obs_env._reset_to_orig_state()
            # TODO: Should we simulate like PARL and do something else if this would fail? Sometimes done returns true
            # assert not done
            return self.do_nothing_action

        # buckets.update_bucket(observation, sorted_actions)

        o, _, d, info_simulate = observation.simulate(self.do_nothing_action)
        observation._obs_env._reset_to_orig_state()
        assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

        min_rho = o.rho.max() if not d else 9999
        print(
            "%s, heavy load, line-%d load is %.2f"
            % (str(observation.get_time_stamp()), observation.rho.argmax(), observation.rho.max())
        )

        if training:
            # Pick action randomly (For now)
            selected_action = None
            action_valid = False
            action_index = -1
            while action_valid == False:
                action_index = randrange(len(self.all_actions))
                selected_action = self.action_space.from_vect(self.all_actions[action_index])
                is_legal = False
                if np.all(selected_action.redispatch == 0.0):
                    action_valid = self.is_legal_bus_action(selected_action, observation)
                else:
                    action_valid = self.is_legal_redispatch_action(selected_action, observation)
            bucket_hash = self.buckets.bucket_hash_of_observation(observation)

            if self.previous_bucket_hash != None:
                assert self.previous_action_index != None
                print("Train!")
                self.buckets.update_bucket_action_values_Q_Learning(
                    self.previous_action_index, self.previous_bucket_hash, bucket_hash, reward
                )

            self.previous_bucket_hash = bucket_hash
            self.previous_action_index = action_index
            return selected_action

        # else

        # 1-depth simulation search of action with least rho.
        selected_action = self.action_space({})
        for action_vect in self.bus_actions_62_146:
            action = self.action_space.from_vect(action_vect)
            is_legal = False
            if np.all(action.redispatch == 0.0):
                is_legal = self.is_legal_bus_action(action, observation)
            else:
                is_legal = self.is_legal_redispatch_action(action, observation)

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
        return selected_action

    def end(self):
        self.buckets.save_buckets_to_disk()


def run_training_batch(agent, starting_env):
    batch_iteration = 0
    while batch_iteration < MAX_BATCH_ITERATIONS:
        batch_iteration += 1
        env_batch = starting_env.copy()
        obs = env_batch.get_obs()
        reward = env_batch.reward_range[0]
        done = False
        agent.initialize_for_training_episode()
        while True:
            episode_data = {"rewards": [], "action_indexes": []}
            if done:
                if timestep < 8061:
                    print("We lost!")
                else:
                    print("We won!")
                break
            below_rho_threshold = obs.rho.max() < RHO_THRESHOLD
            if below_rho_threshold:
                # Update reward with OK
                break
            act = agent.act(env_batch, obs, reward, True, below_rho_threshold, done)
            timestep = env_batch.nb_time_step
            obs, reward, done, info = env_batch.step(act)


random.seed(0)

TRAIN = True
start_time = time.time()
MAX_BATCH_ITERATIONS = 10
number_of_episodes = 1
NUM_CORE = cpu_count()
print("CPU counts：%d" % NUM_CORE)

env_train = grid2op.make("l2rpn_icaps_2021_large_train", backend=LightSimBackend(), reward_class=RedispReward)
env_val = grid2op.make("l2rpn_icaps_2021_large_val", backend=LightSimBackend(), reward_class=RedispReward)
agent = Trainer(env_train, env_train.action_space)
print("start training...")
for i in range(number_of_episodes):
    print("Running episode:", i)
    print(env_train.chronics_handler.get_name())
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
        act = agent.act(env_train, obs, reward, False, below_rho_threshold, done)

        timestep = env_train.nb_time_step
        obs, reward, done, info = env_train.step(act)
        # TODO: Try reset topology ??? Otherwise we fail as soon as opponent disconnects one line.
        # print(info)
        # print(below_rho_threshold)
        # print(first_env_since_overflow)
        # print(timestep)
        # print(info)
        if TRAIN and done and timestep < 8061 and last_train_timestep < timestep and first_env_since_overflow != None:
            last_train_timestep = timestep
            env_train = first_env_since_overflow.copy()
            obs = env_train.get_obs()
            print("Running training batch before timestep:", last_train_timestep, "---->")
            run_training_batch(agent, first_env_since_overflow)
            print("<----- Done training batch")

    print("Completed episode", i, ",number of timesteps:", timestep)

print("FINISH!!")
agent.end()
