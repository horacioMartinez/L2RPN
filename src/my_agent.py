import os
import datetime
import time
import inspect
import numpy as np
import sys
from grid2op.Agent import BaseAgent

np.set_printoptions(threshold=sys.maxsize)


def print_echo(expr):
    outer_locals = inspect.currentframe().f_back.f_locals
    result = eval(expr, globals(), outer_locals)
    print(expr, "=>", result, type(result))


start_time = time.time()


class MyAgent(BaseAgent):
    """
    This is the most basic BaseAgent. It is purely passive, and does absolutely nothing.
    As opposed to most reinforcement learning environments, in grid2op, doing nothing is often
    the best solution.
    """

    def is_legal(self, action, obs):
        adict = action.as_dict()
        if "change_bus_vect" not in adict:
            return True
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
        global start_time
        # print("--- %s seconds ---" % (time.time() - start_time))

        if observation.rho.max() < 0.999:
            no_action = self.action_space({})
            return no_action

        o, _, d, _ = observation.simulate(self.action_space({}))
        min_rho = o.rho.max() if not d else 9999
        print(
            "%s, heavy load, line-%d load is %.2f"
            % (str(observation.get_time_stamp()), observation.rho.argmax(), observation.rho.max())
        )

        # 1-depth search
        selected_action = self.action_space({})
        for action_vect in self.bus_actions62:
            action = self.action_space.from_vect(action_vect)
            is_legal, reason = self.action_space._is_legal(action, self.env)
            if not is_legal:
                # skip it? Checking for legality in search is prob different
                raise reason
            obs, _, done, _ = observation.simulate(action)
            if done:
                continue
            if obs.rho.max() < min_rho:
                min_rho = obs.rho.max()
                selected_action = action

        print("Selected action: ")
        print(selected_action)

        start_time = time.time()
        return selected_action


def make_agent(env):
    my_agent = MyAgent(env, env.action_space, "nombreMiAgente")
    return my_agent
