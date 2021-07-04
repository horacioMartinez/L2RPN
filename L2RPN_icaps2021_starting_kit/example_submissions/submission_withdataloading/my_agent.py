from l2rpn_baselines.
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

    
def make_agent(env, submission_dir):
    """
    This function will be used by codalab to create your agent. It should accept exactly an environment and a path
    to your sudmission directory and return a valid agent.
    """
    res = MyAgent(env.action_space)
    import pandas as pd
    import os
    pd.read_csv(os.path.join(submission_dir, "weights", "test.csv"))
    return res
