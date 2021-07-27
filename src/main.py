import grid2op
from l2rpn_baselines.DoubleDuelingDQN import train
from l2rpn_baselines.DoubleDuelingDQN import evaluate
from l2rpn_baselines.PandapowerOPFAgent import evaluate as evaluatePanda
from grid2op.Reward import RedispReward
from grid2op.utils import ScoreICAPS2021
from grid2op.utils import ScoreL2RPN2020
from lightsim2grid.LightSimBackend import LightSimBackend
from baseline_agents.DoubleDuelingDQN import make_D3QN_agent
from baseline_agents.DoNothing import make_DoNothing_agent
from baseline_agents.DoNothing import make_DoNothingAttention_agent
from baseline_agents.Kait.submission import make_agent as make_Kait_agent
from baseline_agents.PARL.track1.wrapper import make_PARL_agent

BACKEND = LightSimBackend

# track = "l2rpn_icaps_2021_small"
track = "l2rpn_neurips_2020_track1_small"

# env = grid2op.make(track, backend=BACKEND(), reward_class=RedispReward)
env = grid2op.make(track, backend=BACKEND())

number_of_scenarios = 2


def scoreAgent(agent):
    scoring_function = ScoreL2RPN2020
    # scoring_function = ScoreICAPS2021
    my_score = scoring_function(
        env,
        nb_scenario=number_of_scenarios,
        env_seeds=[0 for _ in range(number_of_scenarios)],
        agent_seeds=[0 for _ in range(number_of_scenarios)],
        verbose=2,
    )
    print("STARTING_THE_EVALUATION")
    all_scores, time_steps_survived, total_timesteps = my_score.get(
        agent,
        path_save=(
            "/home/horacio/git/competition/L2RPN/src/evaluation-output-data/"
            + agent.name
        ),
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


agent = make_Kait_agent(
    env, "/home/horacio/git/competition/L2RPN/src/baseline_agents/Kait/"
)
# agent = make_D3QN_agent(env)
# agent = make_DoNothingAttention_agent(env)
# agent = make_DoNothing_agent(env)
agent = make_PARL_agent(
    env
)  # Requires track l2rpn_neurips_2020 and scoring function ScoreL2RPN2020

scoreAgent(agent)
