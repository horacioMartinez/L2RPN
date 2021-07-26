import grid2op
from l2rpn_baselines.DoubleDuelingDQN import train
from l2rpn_baselines.DoubleDuelingDQN import evaluate
from l2rpn_baselines.PandapowerOPFAgent import evaluate as evaluatePanda
from grid2op.Reward import RedispReward
from grid2op.utils import ScoreICAPS2021
from lightsim2grid.LightSimBackend import LightSimBackend
from baseline_agents.DoubleDuelingDQN import make_D3QN_agent
from baseline_agents.DoNothing import make_DoNothing_agent
from baseline_agents.DoNothing import make_DoNothingAttention_agent

BACKEND = LightSimBackend
env = grid2op.make(
    "l2rpn_icaps_2021_small", backend=BACKEND(), reward_class=RedispReward
)

number_of_scenarios = 2


def scoreAgent(agent):
    my_score = ScoreICAPS2021(
        env,
        nb_scenario=number_of_scenarios,
        env_seeds=[0 for _ in range(number_of_scenarios)],
        agent_seeds=[0 for _ in range(number_of_scenarios)],
        verbose=2,
    )
    print("STARTING_THE_EVALUATION")
    all_scores, time_steps_survived, total_timesteps = my_score.get(
        agent,
        path_save="/home/horacio/git/competition/L2RPN/src/evaluation-output-data",
    )
    print("ENDING_THE_EVALUATION")

    for i in range(0, number_of_scenarios):
        print("---------")
        print("Sceneario ", i, ":")
        print("Total score: ", all_scores[i][0])
        print("Operational Score: ", all_scores[i][1])
        print("Alarm Score: ", all_scores[i][2])
        print("Time steps survived: ", time_steps_survived[i])
        print("Total time steps: ", total_timesteps[i])


# agent = make_D3QN_agent(env)
# agent = make_DoNothingAttention_agent(env)

agent = make_DoNothing_agent(env)

scoreAgent(agent)
