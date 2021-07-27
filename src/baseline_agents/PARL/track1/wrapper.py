from .rl_agent import RLAgent


def make_PARL_agent(env):
    agent = RLAgent(env.action_space)
    return agent
