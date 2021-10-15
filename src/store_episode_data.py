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
from grid2op.Reward.BaseReward import BaseReward
from grid2op.Reward import RedispReward
from grid2op.Agent import BaseAgent
from scipy.optimize.optimize import bracket

from my_agent import MyAgent

np.set_printoptions(suppress=True)

EPISODE_INFORMATION_STORAGE_THRESHOLD = 0.0
episode_data = None
disc_lines_before_cascade = []
disc_lines_in_cascade = []


def extract_timestep_features_for_alarm(obs, done, timestep, disc_lines_before_cascade):
    if done:
        return None
    features = {}
    features["timestep"] = timestep
    features["disc_lines_before_cascade"] = disc_lines_before_cascade
    features["topo_vect"] = np.copy(obs.topo_vect)
    features["load_p"] = np.copy(obs.load_p)
    features["load_q"] = np.copy(obs.load_q)
    features["load_v"] = np.copy(obs.load_v)
    features["gen_p"] = np.copy(obs.gen_p)
    features["gen_q"] = np.copy(obs.gen_q)
    features["gen_v"] = np.copy(obs.gen_v)
    features["rho"] = np.copy(obs.rho)
    features["timestep_overflow"] = np.copy(obs.timestep_overflow)
    features["time_before_cooldown_line"] = np.copy(obs.time_before_cooldown_line)
    features["time_before_cooldown_sub"] = np.copy(obs.time_before_cooldown_sub)
    features["time_next_maintence"] = np.copy(obs.time_next_maintenance)
    features["year"] = obs.year
    features["month"] = obs.month
    features["day"] = obs.day  # 1,2,3,4,5, etc
    features["day_of_week"] = obs.day_of_week  # monday,tuesday,etc
    features["hour_of_day"] = obs.hour_of_day
    features["minute_of_hour"] = obs.minute_of_hour
    return features


def save_episode_data_to_disk(name, episode_seed):
    if TRAINING_DATA:
        prefix = "data/episodes_data"
    else:
        prefix = "data/episodes_data_val"

    save_name = prefix + "/episode_data-" + name + "-" + str(episode_seed) + ".pkl"
    if os.path.isfile(save_name):
        print("File already exists!!")
        assert False
    print("Saving episodes data to file:", save_name)
    with open(save_name, "wb") as f:
        pickle.dump(episode_data, f, pickle.HIGHEST_PROTOCOL)
    print("Saved episodes data to", save_name)


def store_information_for_alarm(episode_seed, env, obs, info, done, timestep):
    global episode_data
    global disc_lines_before_cascade
    global disc_lines_in_cascade

    episode_name = env.chronics_handler.get_name()
    if episode_data == None:
        print("BEGIN Storing information for episode: ", episode_name)
        assert timestep == 0
        episode_data = []
        disc_lines_before_cascade = []
        disc_lines_in_cascade = []
        return
    assert timestep > 0

    if done:
        disc_lines_in_cascade = list(np.where(info["disc_lines"] == 0)[0])
    else:
        disc_lines_before_cascade.append(list(np.where(info["disc_lines"] == 0)[0]))
        if (len(disc_lines_before_cascade)) > 4:
            disc_lines_before_cascade.pop(0)

    if not done and obs.rho.max() <= EPISODE_INFORMATION_STORAGE_THRESHOLD:
        return

    we_won = False
    if done:
        we_won = len(info["exception"]) == 0
        if we_won:
            assert timestep == 8062

    disc_lines_before_cascade_copy = copy.deepcopy(disc_lines_before_cascade)
    disc_lines_in_cascade_copy = []
    if done and not we_won:
        disc_lines_in_cascade_copy = copy.deepcopy(disc_lines_in_cascade)

    if not done:
        features = extract_timestep_features_for_alarm(obs, done, timestep, disc_lines_before_cascade_copy)

    if done:
        if we_won:
            timestep_information = {"timestep": timestep, "done": done, "we_won": we_won}
        else:
            timestep_information = {
                "timestep": timestep,
                "done": done,
                "we_won": we_won,
                "disc_lines_before_cascade": disc_lines_before_cascade_copy,
                "disc_lines_in_cascade": disc_lines_in_cascade_copy,
            }
    else:
        timestep_information = {
            "timestep": timestep,
            "features": features,
            "done": done,
        }

    episode_data.append(timestep_information)
    if done:
        save_episode_data_to_disk(episode_name, episode_seed)
        episode_data = None
        print("DONE Storing episode:", episode_name)


if len(sys.argv) < 4:
    print("Not enough arguments. USAGE: <Val/Train> <NumScenarios> <#cpus> <id_cpu> <SEED>")
    exit()

assert str(sys.argv[1]) == "Train" or str(sys.argv[1]) == "Val"
TRAINING_DATA = str(sys.argv[1]) == "Train"

number_of_scenarios = int(sys.argv[2])
NUMBER_OF_CPUS = int(sys.argv[3])
CPU_ID = int(sys.argv[4])
SEED = int(sys.argv[5])

assert CPU_ID < NUMBER_OF_CPUS
random.seed(0)

start_time = time.time()
MAX_BATCH_ITERATIONS = 1000000
NUM_CORE = cpu_count()
print("CPU counts：%d" % NUM_CORE)

env_train = grid2op.make("l2rpn_icaps_2021_large_train", backend=LightSimBackend(), reward_class=RedispReward)
env_val = grid2op.make("l2rpn_icaps_2021_large_val", backend=LightSimBackend(), reward_class=RedispReward)
agent = MyAgent(env_train, env_train.action_space, "./", False)

env_val.chronics_handler.seed(SEED)
env_val.chronics_handler.shuffle()
env_train.chronics_handler.seed(SEED)
env_train.chronics_handler.shuffle()

episode_true_index = 0
episode_names = []
survived_timesteps = []

if TRAINING_DATA:
    env = env_train
else:
    env = env_val

print("Total number of chronics:", len(env.chronics_handler.chronics_used))
total_actions_leading_to_game_over = 0
for i in range(number_of_scenarios):
    while episode_true_index < i * NUMBER_OF_CPUS + CPU_ID:
        env.reset()
        episode_true_index += 1
    env_seed = i + SEED
    agent_seed = i + SEED
    env.seed(env_seed)
    obs = env.reset()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Running episode:", i, "(", env.chronics_handler.get_name(), ")")
    episode_names.append(env.chronics_handler.get_name())
    done = False
    info = None
    timestep = 0
    reward = 0
    while not done:
        act = agent.act(obs, reward, done)
        store_information_for_alarm(env_seed, env, obs, info, done, timestep)
        obs, reward, done, info = env.step(act)
        under_attack = info["opponent_attack_line"] is not None and len(info["opponent_attack_line"]) > 0
        timestep = env.nb_time_step
        if done:
            survived_timesteps.append(timestep)
        assert not obs.is_alarm_illegal[0]  # Only true if last alarm was illegal
    store_information_for_alarm(env_seed, env, obs, info, done, timestep)
    print("Completed episode", i, ",number of timesteps:", timestep)

print("---------------------------")
print("Episodes:", episode_names)
print("Num timesteps", len(survived_timesteps), " survived timesteps:", survived_timesteps)
average = 0
for survived_timestep in survived_timesteps:
    average += survived_timestep
average = average / len(survived_timesteps)
print("-> Average survived timesteps:", average)
GBmemory = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / (1024 * 1024)

print("Memory used (GB):", GBmemory)
print("Environment used:", "env_train" if env == env_train else "env_val", "Seed used:", SEED)
