import os
import datetime
import time
import inspect
import numpy as np
import sys
from grid2op.Agent import BaseAgent
from buckets import bucket_hash_of_observation

np.set_printoptions(threshold=sys.maxsize)


def print_echo(expr):
    outer_locals = inspect.currentframe().f_back.f_locals
    result = eval(expr, globals(), outer_locals)
    print(expr, "=>", result, type(result))


start_time = time.time()
global_min_rho = 0
buckets = {}


class MyAgent(BaseAgent):
    """
    This is the most basic BaseAgent. It is purely passive, and does absolutely nothing.
    As opposed to most reinforcement learning environments, in grid2op, doing nothing is often
    the best solution.
    """

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

    def __init__(self, env, action_space, name):
        BaseAgent.__init__(self, action_space)
        self.action_space = action_space
        self.env = env
        self.name = name

        bus_actions62_name = None
        bus_actions146_name = None
        bus_actions1255_name = None
        if "2021" in env.name:
            bus_actions62_name = "bus_actions62_2021.npy"
            bus_actions146_name = "bus_actions146_2021.npy"
            bus_actions1255_name = "bus_actions1255_2021.npy"
        elif "2020" in env.name:
            bus_actions62_name = "bus_actions62_2020.npy"
            bus_actions146_name = "bus_actions146_2020.npy"
            bus_actions1255_name = "bus_actions1255_2020.npy"
        else:
            assert False

        self.bus_actions62 = np.load(os.path.join("./data/", bus_actions62_name))
        self.bus_actions146 = np.load(os.path.join("./data/", bus_actions146_name))
        self.bus_actions_62_146 = np.concatenate((self.bus_actions62, self.bus_actions146), axis=0)
        self.bus_actions1255 = np.load(os.path.join("./data/", bus_actions1255_name))
        self.bus_actions_62_146_1255 = np.concatenate((self.bus_actions_62_146, self.bus_actions1255), axis=0)

    def act(self, observation, reward, done=False):
        global buckets
        global global_min_rho
        global start_time
        # print("--- %s seconds ---" % (time.time() - start_time))

        if observation.rho.max() < 0.999:
            no_action = self.action_space({})
            return no_action

        bucket_hash = bucket_hash_of_observation(observation)
        if bucket_hash not in buckets:
            buckets[bucket_hash] = {"visits": 1}
            # Action: List containing sorted actions, from best to worst. # NOTE: maybe we should update also according to metric of *how* mucho one action improved, not just if it is the best?
            buckets[bucket_hash] = {"sorted_actions": []}
        else:
            buckets[bucket_hash]["visits"] += 1

        o, _, d, info_simulate = observation.simulate(self.action_space({}))
        observation._obs_env._reset_to_orig_state()
        assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

        min_rho = o.rho.max() if not d else 9999
        if min_rho != 9999:
            print("min_rho:", min_rho)
            if min_rho > global_min_rho:
                global_min_rho = min_rho
            print("global_min_rho:", global_min_rho)
        print(
            "%s, heavy load, line-%d load is %.2f"
            % (str(observation.get_time_stamp()), observation.rho.argmax(), observation.rho.max())
        )

        # 1-depth simulation search of action with least rho.
        selected_action = self.action_space({})
        for action_vect in self.bus_actions62:
            action = self.action_space.from_vect(action_vect)
            is_legal = self.is_legal_bus_action(action, observation)
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

        print("Selected action: ")
        print(selected_action)

        print("Buckets:", buckets)

        start_time = time.time()
        return selected_action


def make_agent(env):
    my_agent = MyAgent(env, env.action_space, "nombreMiAgente")
    return my_agent
