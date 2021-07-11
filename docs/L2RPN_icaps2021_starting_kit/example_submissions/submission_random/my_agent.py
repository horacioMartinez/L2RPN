
from grid2op.Agent import RandomAgent
from grid2op.Reward import ConstantReward

def make_agent(env, submission_dir):
    """
    This function will be used by codalab to create your agent. It should accept exactly an environment and a path
    to your submission directory and return a valid agent.
    """
    agent = RandomAgent(env.action_space)
    return agent
    
