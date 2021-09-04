"""
In this file, a multi-process training for PPO model is designed.
training process:
    The environment steps “do nothing” action (except reconnection of lines)
    until encountering a dangerous scenario, then its observation is sent to
    the Senior Student to get a “do something” action. After stepping this
    action, the reward is calculated and fed back to the Senior Student for
    network updating.

author: chen binbin
mail: cbb@cbb1996.com
"""
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

buckets = Buckets()

# NOTE: Final agent should have same thresholds !
RHO_THRESHOLD = 1.0
RHO_THRESHOLD_RESET_REDISPATCH = 1.0
RHO_THRESHOLD_RECONNECT = 1.0

# Q(St,At) <- Q(St,At) + alpha(Rt+1 + gamma*max_a(Q(St+1,a)) - Q(St,At))


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

        self.bus_actions62 = np.load(os.path.join("./data/", bus_actions62_name))
        self.bus_actions146 = np.load(os.path.join("./data/", bus_actions146_name))
        self.bus_actions_62_146 = np.concatenate((self.bus_actions62, self.bus_actions146), axis=0)
        self.bus_actions1255 = np.load(os.path.join("./data/", bus_actions1255_name))
        self.bus_actions_62_146_1255 = np.concatenate((self.bus_actions_62_146, self.bus_actions1255), axis=0)
        self.redispatch_actions = np.load(os.path.join("./data/", redispatch_actions_name))
        self.all_actions = np.concatenate((self.bus_actions_62_146_1255, self.redispatch_actions), axis=0)

        self.start_learning_episode_time_step = -1
        self.batch_iterations = 0  # Batch goes from time we pass rho threshold to when we pass it.
        self.start_of_batch_env = None

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

    def act(self, env, observation, reward, done=False):
        global buckets
        global global_min_rho
        global start_time
        global first_env_since_overflow
        global batch_iteration

        print("--- %s seconds ---" % (time.time() - start_time))

        some_line_disconnected = not np.all(observation.topo_vect != -1)
        below_rho_threshold = observation.rho.max() < RHO_THRESHOLD
        current_time_step = env.nb_time_step

        print("current_time_step:", current_time_step)
        if below_rho_threshold:
            first_env_since_overflow = None
            batch_iteration = 0  # Reset batch iterations if we get out of this batch and continue with the episode
            print("Below threshold, rho:", observation.rho.max())
        else:
            print("Above threshold, rho:", observation.rho.max())
            if first_env_since_overflow == None:
                first_env_since_overflow = env.copy()

        if some_line_disconnected:
            # TODO: Mix reconnect action with other actions ??
            action = self._reconnect_action(observation)
            if action is not None:
                return action

        if below_rho_threshold:  # No overflow
            if not some_line_disconnected:
                # TODO: try with ._reset_topology() ? Makes sense that it would be better than not doing it.
                action = self._reset_redispatch(observation)
                if action is not None:
                    return action
            _, _, done, _ = observation.simulate(self.do_nothing_action)
            observation._obs_env._reset_to_orig_state()
            # TODO: Should we simulate like PARL and do something else if this would fail? Sometimes done returns true
            # assert not done
            return self.do_nothing_action

        sorted_actions = np.arange(len(self.all_actions))
        buckets.update_bucket(observation, sorted_actions)

        o, _, d, info_simulate = observation.simulate(self.do_nothing_action)
        observation._obs_env._reset_to_orig_state()
        assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

        min_rho = o.rho.max() if not d else 9999
        print(
            "%s, heavy load, line-%d load is %.2f"
            % (str(observation.get_time_stamp()), observation.rho.argmax(), observation.rho.max())
        )

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
        global buckets
        # print("BUCKETS -----------------_> ")
        # print(buckets.buckets_)
        buckets.save_buckets_to_disk()


start_time = time.time()
MAX_BATCH_ITERATIONS = 10
batch_iteration = 0

number_of_episodes = 1
NUM_CORE = cpu_count()
print("CPU counts：%d" % NUM_CORE)
track = "l2rpn_icaps_2021_large"
env = grid2op.make(track, backend=LightSimBackend(), reward_class=RedispReward)

agent = Trainer(env, env.action_space)
print("start training...")
for i in range(number_of_episodes):
    print("Running episode:", i)
    env.seed(i + 10)
    obs = env.reset()
    done = False
    reward = env.reward_range[0]
    first_env_since_overflow = None
    batch_iteration = 0
    while not done:
        act = agent.act(env, obs, reward, done)

        timestep = env.nb_time_step
        obs, reward, done, info = env.step(act)

        if done and timestep < 8061 and batch_iteration < MAX_BATCH_ITERATIONS and first_env_since_overflow != None:
            batch_iteration += 1
            env = first_env_since_overflow.copy()
            obs = env.get_obs()
            done = False
            print("Returning to timestep:", env.nb_time_step)
            print("---")

print("FINISH!!")
agent.end()
