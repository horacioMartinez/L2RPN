import grid2op
from grid2op.Agent import DoNothing
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
from grid2op.Runner import Runner

# env = grid2op.make(track, backend=BACKEND(), reward_class=RedispReward)
BACKEND = LightSimBackend

number_of_scenarios = 2


def scoreAgent(make_agent, competition):
    if competition == 2020:
        scoring_function = ScoreL2RPN2020
        track = "l2rpn_neurips_2020_track1_small"
    else:
        assert competition == 2021
        scoring_function = ScoreICAPS2021
        track = "l2rpn_icaps_2021_small"
    env = grid2op.make(track, backend=BACKEND())
    agent = make_agent(env)
    my_score = scoring_function(
        env,
        nb_scenario=number_of_scenarios,
        env_seeds=[i for i in range(number_of_scenarios)],
        agent_seeds=[i for i in range(number_of_scenarios)],
        verbose=2,
    )
    print("STARTING THE EVALUATION")
    result = my_score.get(
        agent,
        path_save=(
            "/home/horacio/git/competition/L2RPN/src/evaluation-output-data/"
            + agent.name
        ),
    )
    print("ENDING THE EVALUATION")

    if competition == 2020:
        print(result)
        return
    else:
        all_scores, time_steps_survived, total_timesteps = result
        for i in range(0, number_of_scenarios):
            print("---------")
            print("Sceneario ", i, ":")
            print("Total score: ", all_scores[i][0])
            print("Operational Score: ", all_scores[i][1])
            print("Alarm Score: ", all_scores[i][2])
            print("Time steps survived: ", time_steps_survived[i])
            print("Total time steps: ", total_timesteps[i])


# agent = make_Kait_agent(
#    env, "/home/horacio/git/competition/L2RPN/src/baseline_agents/Kait/"
# )
# agent = make_D3QN_agent(env)
# agent = make_DoNothingAttention_agent(env)
# agent = make_DoNothing_agent(env)


scoreAgent(make_DoNothing_agent, 2021)
# scoreAgent(make_PARL_agent, 2020)
