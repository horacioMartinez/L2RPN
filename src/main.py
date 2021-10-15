import sys
import math
import time
import grid2op
import numpy as np
from grid2op.utils import ScoreICAPS2021
from lightsim2grid.LightSimBackend import LightSimBackend
from grid2op.Episode import EpisodeReplay
from my_agent import make_agent
from alarm import Alarm

# env = grid2op.make(track, backend=BACKEND(), reward_class=RedispReward)
start_time = time.time()
BACKEND = LightSimBackend


def scoreAgent(make_agent, number_of_scenarios, saveGif):
    scoring_function = ScoreICAPS2021
    track = "l2rpn_icaps_2021_large_val"
    env = grid2op.make(track, backend=BACKEND())
    agent = make_agent(env, "./")
    my_score = scoring_function(
        env,
        nb_scenario=number_of_scenarios,
        env_seeds=[i for i in range(number_of_scenarios)],
        agent_seeds=[i for i in range(number_of_scenarios)],
        verbose=2,
    )
    print("STARTING THE EVALUATION")
    path_save = "./evaluation-output-data/" + agent.name
    result = my_score.get(agent, path_save, nb_process=1)
    print("ENDING THE EVALUATION")

    all_scores, time_steps_survived, total_timesteps = result
    averageTotalScore = 0
    averageOpScore = 0
    averageAlarmScore = 0
    averageTimestepsSurvived = 0
    print("Sceneario:Total score,Operational score,Alarm score,TS survived/total TS")
    text = ""
    for i in range(0, number_of_scenarios):
        text += str(i) + ": ["
        text += f"{all_scores[i][0]:.1f}" + ","
        text += f"{all_scores[i][1]:.1f}" + ","
        text += f"{all_scores[i][2]:.1f}" + ","
        text += str(time_steps_survived[i]) + "/" + str(total_timesteps[i])
        text += "]"
        if i < number_of_scenarios - 1:
            text += " | "
        averageTotalScore += all_scores[i][0]
        averageOpScore += all_scores[i][1]
        averageAlarmScore += all_scores[i][2]
        averageTimestepsSurvived += time_steps_survived[i]
    print(text)
    print("---------")
    print("Average results >")
    print("Number of scenarios:", number_of_scenarios)
    print("Average score:", averageTotalScore / number_of_scenarios)
    print("Average operational score:", averageOpScore / number_of_scenarios)
    print("Average alarm score:", averageAlarmScore / number_of_scenarios)
    print("Average time steps survived:", averageTimestepsSurvived / number_of_scenarios)

    if saveGif:
        for episode_id in range(0, number_of_scenarios):
            meta_data_dn = my_score.stat_dn.get_metadata()
            this_ep_nm = meta_data_dn[f"{episode_id}"]["scenario_name"]
            gif_name = this_ep_nm
            print("Creating {}.gif".format(gif_name))
            plot_epi = EpisodeReplay(path_save)
            plot_epi.replay_episode(episode_id=this_ep_nm, gif_name=gif_name, display=False)


if len(sys.argv) < 1:
    print("Not enough arguments. USAGE: <NumScenarios>")
    exit()

number_of_scenarios = int(sys.argv[1])

scoreAgent(make_agent, number_of_scenarios, False)
print("--- %s seconds ---" % (time.time() - start_time))
