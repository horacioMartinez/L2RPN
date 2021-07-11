
from grid2op.Agent import BaseAgent

class MyAgent(BaseAgent):
    """
    The template to be used to create an agent: any controller of the power grid is expected to be a subclass of this
    grid2op.Agent.BaseAgent.
    """
    def __init__(self, action_space):
        """Initialize a new agent."""
        BaseAgent.__init__(self, action_space=action_space)

    def act(self, observation, reward, done):
        """The action that your agent will choose depending on the observation, the reward, and whether the state is terminal"""
        # do nothing for example (with the empty dictionary) :
        return self.action_space({})
    
def make_agent(env, this_directory_path):
    my_agent = MyAgent(env.action_space)
    return my_agent
