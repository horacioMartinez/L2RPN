from grid2op.Agent import BaseAgent
from grid2op.Reward import BaseReward


class MyAgent(BaseAgent):
    """
    The template to be used to create an agent: any controller of the power grid is expected to be a daughter of this
    class.
    """
    def __init__(self, action_space):
        """Initialize a new agent."""
        BaseAgent.__init__(self, action_space=action_space)

    def act(self, observation, reward, done):
        return self.action_space({})


class reward(BaseReward):
    """
    if you want to control the reward used by the envrionment when your agent is being assessed, you need
    to provide a class with that specific name that define the reward you want.

    It is important that this file has the exact name "reward" all lowercase, we apologize for the python convention :-/
    """
    def __init__(self):
        # CAREFULL, USING THIS REWARD WILL PROBABLY HAVE LITTLE INTEREST...
        # You can look at the grid2op documentation to have example on definition of rewards
        # https://grid2op.readthedocs.io/en/v0.9.0/reward.html
        BaseReward.__init__(self)

    def __call__(self, action, env, has_error, is_done, is_illegal, is_ambiguous):
        # CAREFULL, USING THIS REWARD WILL PROBABLY HAVE LITTLE INTEREST...
        # You can look at the grid2op documentation to have example on definition of rewards
        # https://grid2op.readthedocs.io/en/latest/reward.html
        return 1.0


def make_agent(env, submission_dir):
    """
    This function will be used by codalab to create your agent. It should accept exactly an environment and a path
    to your sudmission directory and return a valid agent.
    """
    res = MyAgent(env.action_space)
    return res
