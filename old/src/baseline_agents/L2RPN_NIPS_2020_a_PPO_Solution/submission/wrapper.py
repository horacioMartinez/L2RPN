from .my_agent import MyAgent


def make_PPO_agent(env):
    agent = MyAgent(
        env.action_space,
        env,
        "/home/horacio/git/competition/L2RPN/src/baseline_agents/L2RPN_NIPS_2020_a_PPO_Solution/submission",
    )
    return agent
