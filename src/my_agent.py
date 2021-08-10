from grid2op.Agent import BaseAgent


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
        self.action_space()
        numberOfActionsIncludingIllegalOnes = self.action_space.size()
        print(numberOfActionsIncludingIllegalOnes)
        # doNothingActionVerifyngLegality = self.action_space({}, True, self.env)
        random_action = self.action_space.sample()
        print(random_action)
        return random_action


def make_agent(env):
    my_agent = MyAgent(env, env.action_space, "nombreMiAgente")
    return my_agent
