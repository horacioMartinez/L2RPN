from os import listdir
from os.path import isfile, join
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
from alarm import Alarm

# Podemos poner como reward cuanto aumenta el rho 7 episodios despues de sonar la alarma.
# O sera, que tan cerca esta de game over ??
# Podemos predecir la prob de que un episodio sea el anterior a uno de game over?

# No scientific notation
np.set_printoptions(suppress=True)


def generate_nn_training_data(episodes_data):
    # Data is the features (rho, etc)
    input_data = []
    labels = []  # Label is if we finish in 11 timesteps or less
    for episode_data in episodes_data:
        last_timestep = episode_data[len(episode_data) - 1]["timestep"]
        for timestep_data in episode_data:
            if timestep_data["done"]:
                continue
            current_timestep = timestep_data["timestep"]
            does_finish_in_11_or_less_timesteps = (last_timestep - current_timestep) <= 11
            features = []
            features.append(timestep_data["features"]["rho"])
            input_data.append(features)
            labels.append(does_finish_in_11_or_less_timesteps)

    return input_data, labels


def nn_alarm_action(timestep, last_alarm_trigger_timestep, feature_last_timestep_rho, env, features):
    assert timestep >= last_alarm_trigger_timestep

    # feature_actions_rho = features["actions_rho"]
    feature_rho = features["rho"]
    feature_line_status = features["line_status"]
    feature_month = features["month"]
    feature_day = features["day"]
    feature_day_of_week = features["day_of_week"]
    feature_hour_of_day = features["hour_of_day"]
    feature_minute_of_hour = features["minute_of_hour"]
    feature_timestep_overflow = features["timestep_overflow"]
    feature_time_before_cooldown_line = features["time_before_cooldown_line"]
    feature_time_before_cooldown_sub = features["time_before_cooldown_sub"]
    features_timesteps_since_last_attack = features["timesteps_since_last_attack"]
    feature_time_next_maintenance = features["time_next_maintence"]
    feature_under_attack = features["under_attack"]
    feature_attack_duration = features["opponent_attack_duration"]
    feature_timesteps_since_ongoing_attack_started = features["timesteps_since_ongoing_attack_started"]

    if feature_last_timestep_rho is None:
        feature_rho_difference = np.zeros_like(feature_rho)
    else:
        feature_rho_difference = feature_last_timestep_rho - feature_rho

    # Limit timesteps to 10 (because 11 is the max timesteps the alarm can wait to have a positive score)
    feature_time_before_cooldown_line[feature_time_before_cooldown_line > 10] = 11
    feature_time_before_cooldown_sub[feature_time_before_cooldown_sub > 10] = 11
    feature_time_next_maintenance[feature_time_next_maintenance > 10] = 99

    # print("feature_rho_difference:")
    # print(feature_rho_difference)
    # print("feature_rho")
    # print(feature_rho)
    # print("feature_line_status")
    # print(feature_line_status)
    # print("feature_month")
    # print(feature_month)
    # print("feature_day")
    # print(feature_day)
    # print("feature_day_of_week")
    # print(feature_day_of_week)
    # print("feature_hour_of_day")
    # print(feature_hour_of_day)
    # print("feature_minute_of_hour")
    # print(feature_minute_of_hour)
    # print("feature_timestep_overflow")
    # print(feature_timestep_overflow)
    # print("feature_time_before_cooldown_line")
    # print(feature_time_before_cooldown_line)
    # print("feature_time_before_cooldown_sub")
    # print(feature_time_before_cooldown_sub)
    # print("features_timesteps_since_last_attack")
    # print(features_timesteps_since_last_attack)
    # print("feature_time_next_maintenance")
    # print(feature_time_next_maintenance)
    # print("feature_under_attack")
    # print(feature_under_attack)
    # print("feature_attack_duration")
    # print(feature_attack_duration)
    # print("feature_timesteps_since_ongoing_attack_started")
    # print(feature_timesteps_since_ongoing_attack_started)

    return None


def naive_alarm_action(timestep, last_alarm_trigger_timestep, env, rho):
    assert timestep >= last_alarm_trigger_timestep
    if rho.max() < 1.1:
        return None
    if timestep - last_alarm_trigger_timestep < 7:
        return None
    alarms_lines_area = env.alarms_lines_area
    alarms_area_names = env.alarms_area_names
    zone_for_each_lines = alarms_lines_area
    line_most_overloaded = np.argmax(rho)
    line_name = env.name_line[line_most_overloaded]
    # Some lines are in more than one area, which one to chose ?
    zone_name = zone_for_each_lines[line_name][0]
    #'east' = 0, 'middle' = 1, 'west' = 2
    zone_index = [alarms_area_names.index(zone_name)]
    alarm_action = env.action_space({"raise_alarm": zone_index})
    return alarm_action


if len(sys.argv) < 1:
    print("Not enough arguments. USAGE: <NumScenarios>")
    exit()

number_of_scenarios = int(sys.argv[1])

random.seed(0)
MAX_MEMORY_GB = 32
start_time = time.time()
MAX_BATCH_ITERATIONS = 1000000
NUM_CORE = cpu_count()
# SEED = CPU_ID
SEED = 0
print("CPU counts：%d" % NUM_CORE)

env_train = grid2op.make("l2rpn_icaps_2021_large_train", backend=LightSimBackend(), reward_class=RedispReward)

env_train.chronics_handler.seed(SEED)
env_train.chronics_handler.shuffle()
env = env_train
env.seed(SEED)
# obs = env.reset()
env.reset()

EPISODES_DATA_PATH = "data/episodes_data"

episodes_data_files = [f for f in listdir(EPISODES_DATA_PATH) if isfile(join(EPISODES_DATA_PATH, f))]
random.shuffle(episodes_data_files)

episodes_data = []
aux = 0
for episodes_data_file in episodes_data_files:
    if aux == number_of_scenarios:
        break
    with open(EPISODES_DATA_PATH + "/" + episodes_data_file, "rb") as f:
        episodes_data.append(pickle.load(f))
    aux += 1

episode_data_index = 0
alarm_scores = []
episode_names = []
number_of_alarm_failures_due_to_action_leading_to_game_over = 0
number_of_alarm_failures_due_to_no_info_in_previous_timesteps = 0

# Remove scenarios where we win
filtered_array = []
for i in range(0, len(episodes_data)):
    last_timestep_data = episodes_data[i][len(episodes_data[i]) - 1]
    assert last_timestep_data["done"]
    we_won = last_timestep_data["we_won"]
    if we_won:
        continue
    filtered_array.append(episodes_data[i])
print("Filtered out", len(episodes_data) - len(filtered_array), "because we won")
episodes_data = filtered_array
#

# Remove scenarios where our actions lead to game over. (Theres nothing we can do about this !):
filtered_array = []
for i in range(0, len(episodes_data)):
    last_timestep_data = episodes_data[i][len(episodes_data[i]) - 1]
    assert last_timestep_data["done"]
    we_won = last_timestep_data["we_won"]
    if not we_won:
        disc_lines_in_cascade = last_timestep_data["disc_lines_in_cascade"]
        if len(disc_lines_in_cascade) == 0:
            number_of_alarm_failures_due_to_action_leading_to_game_over += 1
            continue
    filtered_array.append(episodes_data[i])
print("Filtered out", len(episodes_data) - len(filtered_array), "due to our action leading to game over")
episodes_data = filtered_array
#

RHO_THRESHOLD_VISIT = 0.0

for episode_data in episodes_data:
    episode_name = episodes_data_files[episode_data_index].split("-", 1)[-1].split(".", 1)[0]
    episode_names.append(episode_name)
    ###
    # if episode_name != "Scenario_august_238-126":
    # episode_data_index += 1
    # continue
    ###
    timestep = 0
    done = False
    data_index = 0
    alarm = Alarm(env)
    episode_data_timesteps_record = []
    last_alarm_trigger_timestep = 0
    while not done:
        timestep += 1
        episode_data_timestep = episode_data[data_index]["timestep"]
        if timestep < episode_data_timestep:
            alarm.update_timestep(timestep, None)
            continue
        assert timestep == episode_data_timestep

        timestep_data = episode_data[data_index]
        current_data_index = data_index
        data_index += 1

        #
        if not timestep_data["done"]:
            if timestep_data["features"]["rho"].max() < RHO_THRESHOLD_VISIT:
                alarm.update_timestep(timestep, None)
                continue
        #
        episode_data_timesteps_record.append(episode_data_timestep)

        done = timestep_data["done"]
        if done:
            we_won = timestep_data["we_won"]
            if not we_won:
                disc_lines_before_cascade = timestep_data["disc_lines_before_cascade"]
                disc_lines_in_cascade = timestep_data["disc_lines_in_cascade"]
            alarm_score = alarm.compute_score(timestep, we_won, disc_lines_before_cascade, disc_lines_in_cascade)

            if not we_won:
                if len(disc_lines_in_cascade) == 0:
                    assert alarm_score == -200
                    number_of_alarm_failures_due_to_action_leading_to_game_over += 1
                elif episode_data_timestep - 7 not in episode_data_timesteps_record:
                    number_of_alarm_failures_due_to_no_info_in_previous_timesteps += 1

            print("Episode:", episode_name, " ALARM SCORE:", alarm_score)
            alarm_scores.append(alarm_score)
            continue
        # Not done
        features = timestep_data["features"]

        feature_last_timestep_rho = None
        if current_data_index > 0:
            last_timestep_data = episode_data[current_data_index - 1]
            if last_timestep_data["timestep"] == timestep - 1:
                feature_last_timestep_rho = last_timestep_data["features"]["rho"]

        feature_timestep = features["timestep"]
        feature_disc_lines_before_cascade = features["disc_lines_before_cascade"]
        feature_actions_rho = features["actions_rho"]
        feature_rho = features["rho"]
        feature_topo_vect = features["topo_vect"]
        feature_line_status = features["line_status"]
        feature_load_p = features["load_p"]
        feature_load_q = features["load_q"]
        feature_load_v = features["load_v"]
        feature_gen_p = features["gen_p"]
        feature_gen_q = features["gen_q"]
        feature_gen_v = features["gen_v"]
        feature_year = features["year"]
        feature_month = features["month"]
        feature_day = features["day"]
        feature_day_of_week = features["day_of_week"]
        feature_hour_of_day = features["hour_of_day"]
        feature_minute_of_hour = features["minute_of_hour"]
        feature_timestep_overflow = features["timestep_overflow"]
        feature_time_before_cooldown_line = features["time_before_cooldown_line"]
        feature_time_before_cooldown_sub = features["time_before_cooldown_sub"]
        features_timesteps_since_last_attack = features["timesteps_since_last_attack"]
        feature_time_next_maintenance = features["time_next_maintence"]
        feature_under_attack = features["under_attack"]
        feature_attack_duration = features["opponent_attack_duration"]
        feature_timesteps_since_ongoing_attack_started = features["timesteps_since_ongoing_attack_started"]

        alarm_is_legal = alarm.budget >= alarm.alarm_cost
        valid_actions = []
        raise_alarm_vect = None
        if alarm_is_legal:
            valid_actions = [
                env.action_space({"raise_alarm": 0}),
                env.action_space({"raise_alarm": 1}),
                env.action_space({"raise_alarm": 2}),
            ]
            # alarm_action = None
            # alarm_action = valid_actions[0]
            # alarm_action = naive_alarm_action(timestep, last_alarm_trigger_timestep, env, feature_rho)
            alarm_action = nn_alarm_action(
                timestep, last_alarm_trigger_timestep, feature_last_timestep_rho, env, features
            )
            # alarm_action = None
            if alarm_action != None:
                raise_alarm_vect = alarm_action.raise_alarm
                last_alarm_trigger_timestep = timestep

        alarm.update_timestep(timestep, raise_alarm_vect)
        # print(feature_rho)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< DONE:", alarm_scores[len(alarm_scores) - 1])
    episode_data_index += 1

print("Num episodes:", len(episode_names))
print("Episodes:", episode_names)
print("Alarm scores", alarm_scores)
average_alarm_score = 0
for alarm_score in alarm_scores:
    average_alarm_score += alarm_score
average_alarm_score = average_alarm_score / len(alarm_scores)
print("-> Average alarm score:", average_alarm_score)
print("THIS NUMBERS SHOULD BE LOW! ->")
print(
    "number_of_alarm_failures_due_to_no_info_in_previous_timesteps:",
    number_of_alarm_failures_due_to_no_info_in_previous_timesteps,
)
print(
    "number_of_alarm_failures_due_to_action_leading_to_game_over:",
    number_of_alarm_failures_due_to_action_leading_to_game_over,
)

training_data = generate_nn_training_data(episodes_data)

print("FINISH!")
