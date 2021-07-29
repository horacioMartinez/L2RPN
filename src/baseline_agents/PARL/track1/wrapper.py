from .rl_agent import RLAgent


def make_PARL_agent(env):
    agent = RLAgent(env.action_space)
    agent.load("/home/horacio/git/competition/trained-models/PARL/saved_files")
    return agent
