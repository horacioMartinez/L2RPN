from grid2op.Agent import BaseAgent
import inspect


def print_echo(expr):
    outer_locals = inspect.currentframe().f_back.f_locals
    result = eval(expr, globals(), outer_locals)
    print(expr, "=>", result, type(result))


class MyAgent(BaseAgent):
    """
    This is the most basic BaseAgent. It is purely passive, and does absolutely nothing.
    As opposed to most reinforcement learning environments, in grid2op, doing nothing is often
    the best solution.
    """

    def __init__(self, env, action_space, name):
        BaseAgent.__init__(self, action_space)
        self.env = env
        self.name = name

    def act(self, observation, reward, done=False):
        set_bus = self.action_space.get_all_unitary_topologies_set(self.action_space)
        set_line_status_actions = self.action_space.get_all_unitary_line_change(self.action_space)
        redispatch = self.action_space.get_all_unitary_redispatch(self.action_space)
        raise_alarm = self.action_space.get_all_unitary_alarm(self.action_space)
        print("---------")
        print("---------")
        print(len(set_bus))
        print(len(set_line_status_actions))
        print(len(redispatch))
        print(len(raise_alarm))
        print("---------")
        print("---------")
        #         self.dict_properties = {
        #     "set_line_status": act_sp.get_all_unitary_line_set,
        #     "change_line_status": act_sp.get_all_unitary_line_change,
        #     "set_bus": act_sp.get_all_unitary_topologies_set,
        #     "change_bus": act_sp.get_all_unitary_topologies_change,
        #     "redispatch": act_sp.get_all_unitary_redispatch,
        #     "set_storage": act_sp.get_all_unitary_storage,
        #     "curtail": act_sp.get_all_unitary_curtail,
        #     "curtail_mw": act_sp.get_all_unitary_curtail,
        #     "raise_alarm": act_sp.get_all_unitary_alarm,
        # }
        numberOfActionsIncludingIllegalOnes = self.action_space.size()
        print(numberOfActionsIncludingIllegalOnes)
        # doNothingActionVerifyngLegality = self.action_space({}, True, self.env)
        random_action = self.action_space.sample()
        print(random_action)
        return random_action


def make_agent(env):
    my_agent = MyAgent(env, env.action_space, "nombreMiAgente")
    return my_agent
