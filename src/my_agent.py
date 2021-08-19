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

actions_directory_path = (
    "/home/horacio/git/competition/L2RPN/src/baseline_agents/L2RPN_NIPS_2020_a_PPO_Solution/submission"
)


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

        self.actions62 = np.load(os.path.join(".", "bus_actions62.npy"))
        self.actions146 = np.load(os.path.join(".", "bus_actions146.npy"))
        self.actions = np.concatenate((self.actions62, self.actions146), axis=0)
        self.actions1255 = np.load(os.path.join(".", "bus_actions1255.npy"))
        # Son todas de change buffer y usan array2action
        # Actions62 + Action146 = 208 acciones
        # actions1255 son 1255 acciones adicionales que las usa por si no sirven las priemras 208 ?
        # self.actions contiene un array de arrays, donde cada uno de ellos es una accion encodeada como array.
        print("||||||||||||||||||||||||||||| >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        for action in self.actions:
            grid2opAction = self.action_space.from_vect(action)
            print(grid2opAction)
        print("-----------------------------------------------------------")
        for action in self.actions1255:
            grid2opAction = self.action_space.from_vect(action)
            print(grid2opAction)
        print("||||||||||||||||||||||||||||| <<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        exit()

    def act(self, observation, reward, done=False):
        global start_time
        print("--- %s seconds ---" % (time.time() - start_time))
        numberOfActionsIncludingIllegalOnes = self.action_space.size()
        print(numberOfActionsIncludingIllegalOnes)
        # doNothingActionVerifyngLegality = self.action_space({}, True, self.env)
        random_action = self.action_space.sample()
        print(random_action)
        start_time = time.time()
        return random_action


def make_agent(env):
    my_agent = MyAgent(env, env.action_space, "nombreMiAgente")
    return my_agent
