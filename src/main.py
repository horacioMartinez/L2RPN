import sys
import math
import time
import grid2op
import numpy as np
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
from baseline_agents.PARL.track1.wrapper import make_PARL_agent  # First place
from baseline_agents.ExpertAgent.wrapper import make_expert_agent
from baseline_agents.L2RPN_NIPS_2020_a_PPO_Solution.submission.wrapper import make_PPO_agent  # Second place
from grid2op.Runner import Runner
from grid2op.Episode import EpisodeReplay

from submission.my_agent import make_agent as make_agent_submission
from my_agent import make_agent
from alarm import Alarm

# env = grid2op.make(track, backend=BACKEND(), reward_class=RedispReward)
start_time = time.time()
BACKEND = LightSimBackend


def scoreAgent(make_agent, competition, number_of_scenarios, saveGif):
    if competition == 2020:
        scoring_function = ScoreL2RPN2020
        track = "l2rpn_neurips_2020_track1_small"
    else:
        assert competition == 2021
        scoring_function = ScoreICAPS2021
        # track = "l2rpn_icaps_2021_small"
        track = "l2rpn_icaps_2021_large_val"
    env = grid2op.make(track, backend=BACKEND())
    agent = make_agent(env, "./submission/")
    my_score = scoring_function(
        env,
        nb_scenario=number_of_scenarios,
        env_seeds=[i for i in range(number_of_scenarios)],
        agent_seeds=[i for i in range(number_of_scenarios)],
        verbose=2,
    )
    # # TEST ALARM SCORE >
    # for i in range(number_of_scenarios):
    #     env.seed(i)
    #     obs = env.reset()
    #     done = False
    #     info = None
    #     timestep = 0
    #     reward = 0
    #     below_rho_threshold = True
    #     alarm = Alarm(env)
    #     disc_lines_before_cascade = []
    #     disc_lines_in_cascade = []
    #     while not done:
    #         # def act(self, observation, reward, done=False):

    #         act = agent.act(obs, reward, False)
    #         obs, reward, done, info = env.step(act)
    #         timestep = env.nb_time_step
    #         if done:
    #             print(info)
    #         assert not obs.is_alarm_illegal[0]  # Only true if last alarm was illegal
    #         if done:
    #             disc_lines_in_cascade = list(np.where(info["disc_lines"] == 0)[0])
    #         else:
    #             disc_lines_before_cascade.append(list(np.where(info["disc_lines"] == 0)[0]))
    #             if (len(disc_lines_before_cascade)) > 4:
    #                 disc_lines_before_cascade.pop(0)
    #         alarm_action = None
    #         if np.any(act.raise_alarm):
    #             alarm_action = act.raise_alarm
    #         alarm.update_timestep(timestep, alarm_action)
    #         # if not done:
    #         # assert math.isclose(alarm.budget, obs.attention_budget, rel_tol=1e-3)
    #     we_won = len(info["exception"]) == 0
    #     if we_won:
    #         assert timestep == 8062
    #     alarm_score = alarm.compute_score(timestep, we_won, disc_lines_before_cascade, disc_lines_in_cascade)
    #     print("ALARM SCORE:", alarm_score)
    #     print("Completed episode", i, ",number of timesteps:", timestep)
    # exit(0)
    # # < TEST ALARM SCORE
    print("STARTING THE EVALUATION")
    path_save = "/home/horacio/git/competition/L2RPN/src/evaluation-output-data/" + agent.name
    result = my_score.get(agent, path_save, nb_process=1)
    print("ENDING THE EVALUATION")

    if competition == 2020:
        all_scores, time_steps_survived, total_timesteps = result
        averageTotalScore = 0
        averageTimestepsSurvived = 0
        print("Sceneario:Total score,TS survived/total TS")
        text = ""
        for i in range(0, number_of_scenarios):
            text += str(i) + ": ["
            text += f"{all_scores[i]:.1f}" + ","
            text += str(time_steps_survived[i]) + "/" + str(total_timesteps[i])
            text += "]"
            if i < number_of_scenarios - 1:
                text += " | "
            averageTotalScore += all_scores[i]
            averageTimestepsSurvived += time_steps_survived[i]
        print(text)
        print("---------")
        print("Average results >")
        print("Number of scenarios:", number_of_scenarios)
        print("Average score: ", averageTotalScore / number_of_scenarios)
        print("Average time steps survived: ", averageTimestepsSurvived / number_of_scenarios)
    else:
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

    if hasattr(agent, "end"):
        agent.end()

    if saveGif:
        for episode_id in range(0, number_of_scenarios):
            meta_data_dn = my_score.stat_dn.get_metadata()
            this_ep_nm = meta_data_dn[f"{episode_id}"]["scenario_name"]
            gif_name = this_ep_nm
            print("Creating {}.gif".format(gif_name))
            plot_epi = EpisodeReplay(path_save)
            plot_epi.replay_episode(episode_id=this_ep_nm, gif_name=gif_name, display=False)


# agent = make_Kait_agent(
#    env, "/home/horacio/git/competition/L2RPN/src/baseline_agents/Kait/"
# )
# agent = make_D3QN_agent(env)
# agent = make_DoNothingAttention_agent(env)
# agent = make_DoNothing_agent(env)

if len(sys.argv) < 3:
    print("Not enough arguments. USAGE: <AgentName> <NumScenarios> <Year>")
    exit()

selectedAgent = str(sys.argv[1])
number_of_scenarios = int(sys.argv[2])
year = int(sys.argv[3])

print("--- %s seconds ---" % (time.time() - start_time))

print("Using agent", selectedAgent)
if selectedAgent == "DoNothing":
    scoreAgent(make_DoNothing_agent, year, number_of_scenarios, False)
elif selectedAgent == "Expert":
    scoreAgent(make_expert_agent, year, number_of_scenarios, True)
elif selectedAgent == "PARL":
    scoreAgent(make_PARL_agent, year, number_of_scenarios, False)
elif selectedAgent == "PPO":
    scoreAgent(make_PPO_agent, year, number_of_scenarios, False)
elif selectedAgent == "Mio":
    scoreAgent(make_agent, year, number_of_scenarios, False)
elif selectedAgent == "Submission":
    scoreAgent(make_agent_submission, year, number_of_scenarios, False)
else:
    print("Unknown agent", selectedAgent)
    exit(0)

print("--- %s seconds ---" % (time.time() - start_time))
