from enum import Flag
from mmap import ALLOCATIONGRANULARITY
import copy
import pickle
import math
import sys
import random
import resource
from random import randrange, seed
from threading import current_thread
from grid2op import Observation
from lightsim2grid import LightSimBackend
import os
import time
import grid2op
import numpy as np
from multiprocessing import cpu_count
from grid2op.Environment import SingleEnvMultiProcess
from grid2op.Reward.BaseReward import BaseReward
from grid2op.Reward import RedispReward
from grid2op.Agent import BaseAgent
import tensorflow as tf
import tensorflow.keras as tfk
from scipy.optimize.optimize import bracket
from alarm import Alarm
from submission.my_agent import make_agent


if len(sys.argv) < 4:
    print("Not enough arguments. USAGE: <Eval/Train/EvalInTraining> <NumScenarios> <#cpus> <id_cpu>")
    exit()

assert str(sys.argv[1]) == "Eval" or str(sys.argv[1]) == "EvalInTraining"

EVAL_TRAINING_DATA = str(sys.argv[1]) == "EvalInTraining"

number_of_scenarios = int(sys.argv[2])
NUMBER_OF_CPUS = int(sys.argv[3])
CPU_ID = int(sys.argv[4])

assert CPU_ID < NUMBER_OF_CPUS


SEED = 0
random.seed(0)

env_train = grid2op.make("l2rpn_icaps_2021_large_train", backend=LightSimBackend(), reward_class=RedispReward)
env_val = grid2op.make("l2rpn_icaps_2021_large_val", backend=LightSimBackend(), reward_class=RedispReward)

env_val.chronics_handler.seed(SEED)
env_val.chronics_handler.shuffle()
env_train.chronics_handler.seed(SEED)
env_train.chronics_handler.shuffle()

episode_true_index = 0
episode_names = []
survived_timesteps = []
alarm_scores = []

if EVAL_TRAINING_DATA:
    env = env_train
else:
    env = env_val

agent = make_agent(env, "./submission/")
print("Total number of chronics:", len(env.chronics_handler.chronics_used))
for i in range(number_of_scenarios):
    while episode_true_index < i * NUMBER_OF_CPUS + CPU_ID:
        env.reset()
        episode_true_index += 1
    env_seed = i + SEED
    agent_seed = i + SEED
    env.seed(env_seed)
    obs = env.reset()
    ############### RUN SPECFIC EPISODE #################
    # env_train.chronics_handler.reset()
    # episode_seed = 126
    # episode_id = np.where(
    #    env_train.chronics_handler.real_data.subpaths
    #    == "/home/horacio/data_grid2op/l2rpn_icaps_2021_large_train/chronics/Scenario_august_238"
    # )[0][0]
    # print("episode_id:", episode_id)
    # env.seed(episode_seed)
    # env.set_id(episode_id)
    # env.reset()
    #####################################################
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Running episode:", i, "(", env.chronics_handler.get_name(), ")")
    episode_names.append(env.chronics_handler.get_name())
    done = False
    info = None
    timestep = 0
    reward = 0
    # ALARM >
    alarm = Alarm(env)
    disc_lines_before_cascade = []
    disc_lines_in_cascade = []
    # < ALARM
    while not done:
        act = agent.act(obs, reward, done)
        action_timestep = timestep
        obs, reward, done, info = env.step(act)
        timestep = env.nb_time_step
        if done:
            survived_timesteps.append(timestep)

        assert not obs.is_alarm_illegal[0]  # Only true if last alarm was illegal
        # ALARM >
        if done:
            disc_lines_in_cascade = list(np.where(info["disc_lines"] == 0)[0])
        else:
            disc_lines_before_cascade.append(list(np.where(info["disc_lines"] == 0)[0]))
            if (len(disc_lines_before_cascade)) > 4:
                disc_lines_before_cascade.pop(0)
        alarm_action = None
        if np.any(act.raise_alarm):
            alarm_action = act.raise_alarm
        if action_timestep > 0:
            alarm.update_timestep(action_timestep, alarm_action)
    # ALARM >
    we_won = len(info["exception"]) == 0
    if we_won:
        assert timestep == 8062
    alarm_score = alarm.compute_score(timestep, we_won, disc_lines_before_cascade, disc_lines_in_cascade)
    alarm_scores.append(alarm_score)
    print("ALARM SCORE:", alarm_score)
    # < ALARM
    print("Completed episode", i, ",number of timesteps:", timestep)

print("---------------------------")
print("Episodes:", episode_names)
print("Num timesteps", len(survived_timesteps), " survived timesteps:", survived_timesteps)
print("Alarm scores", alarm_scores)
average = 0
for survived_timestep in survived_timesteps:
    average += survived_timestep
average = average / len(survived_timesteps)
print("-> Average survived timesteps:", average)
average_alarm_score = 0
for alarm_score in alarm_scores:
    average_alarm_score += alarm_score
average_alarm_score = average_alarm_score / len(alarm_scores)
print("-> Average alarm score:", average_alarm_score)
GBmemory = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / (1024 * 1024)
print("Memory used (GB):", GBmemory)
print("Environment used:", "env_train" if env == env_train else "env_val", "Seed used:", SEED)
print("FINISH!!")
