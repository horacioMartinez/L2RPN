from .ExpertAgent import ExpertAgent


def make_expert_agent(env):
    agent = ExpertAgent(
        env.action_space, env.observation_space, "Template", "IEEE118_R2"
    )
    return agent
