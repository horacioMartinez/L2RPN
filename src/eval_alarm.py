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
import tensorflow as tf
import tensorflow.keras as tfk

# Podemos poner como reward cuanto aumenta el rho 7 episodios despues de sonar la alarma.
# O sera, que tan cerca esta de game over ??
# Podemos predecir la prob de que un episodio sea el anterior a uno de game over?

# No scientific notation
np.set_printoptions(suppress=True)


def nn_alarm_action(
    timestep, last_alarm_trigger_timestep, env, feature_last_timestep_rho, features, disc_lines_before_cascade
):
    assert timestep >= last_alarm_trigger_timestep
    feature_rho = features["rho"]
    some_line_disconnected = not np.all(features["topo_vect"] != -1)
    if feature_rho.max() < 0.9 or not some_line_disconnected:
        return None

    # feature_actions_rho = features["actions_rho"]
    feature_topo_vect = features["topo_vect"]
    feature_load_p = features["load_p"]
    feature_load_q = features["load_q"]
    feature_load_v = features["load_v"]
    feature_gen_p = features["gen_p"]
    feature_gen_q = features["gen_q"]
    feature_gen_v = features["gen_v"]
    feature_time_before_cooldown_line = features["time_before_cooldown_line"]
    feature_month = features["month"]
    feature_day = features["day"]
    feature_day_of_week = features["day_of_week"]
    feature_hour_of_day = features["hour_of_day"]
    feature_minute_of_hour = features["minute_of_hour"]
    feature_timestep_overflow = features["timestep_overflow"]
    feature_time_before_cooldown_line = features["time_before_cooldown_line"]
    feature_time_before_cooldown_sub = features["time_before_cooldown_sub"]
    feature_time_next_maintenance = features["time_next_maintence"]

    if feature_last_timestep_rho is None:
        feature_rho_delta = np.zeros_like(feature_rho)
    else:
        feature_rho_delta = feature_last_timestep_rho - feature_rho
    processed_features = (
        np.concatenate(
            (
                # [feature_under_attack],
                # [feature_attack_duration],
                # [feature_timesteps_since_last_attack],
                # [feature_timesteps_since_ongoing_attack_started],
                feature_topo_vect,
                feature_load_p,
                feature_load_q,
                feature_load_v,
                feature_gen_p,
                feature_gen_q,
                feature_gen_v,
                feature_rho,
                feature_rho_delta,
                feature_timestep_overflow,
                feature_time_before_cooldown_line,
                feature_time_before_cooldown_sub,
                feature_time_next_maintenance,
                [feature_month],
                [feature_day],
                [feature_day_of_week],
                [feature_hour_of_day],
                [feature_minute_of_hour],
            )
        )
        .flatten()
        .astype(np.float32)
    )

    prediction = model.predict(np.array([processed_features]))[0]
    print("ALARM PREDICTION:", prediction)

    return None


def calculate_zone_for_alarm(env, rho, disc_lines_before_cascade):
    alarms_lines_area = env.alarms_lines_area
    alarms_area_names = env.alarms_area_names
    zone_for_each_lines = alarms_lines_area

    ####### from disc_lines_before_cascade
    combined_disc_lines_before_cascade = np.concatenate(disc_lines_before_cascade).astype(int)
    if len(combined_disc_lines_before_cascade) > 0:
        print("disc_lines_before_cascade:", disc_lines_before_cascade)
        print("combined_disc_lines_before_cascade:", combined_disc_lines_before_cascade)
        last_disconnected_line = combined_disc_lines_before_cascade[len(combined_disc_lines_before_cascade) - 1]
        print("last_disconnected_line:", last_disconnected_line)
        line_name = env.name_line[last_disconnected_line]
        zone_name = zone_for_each_lines[line_name][0]
        zone_index = [alarms_area_names.index(zone_name)]
        return zone_index
    ########

    # From line most overloaded
    line_most_overloaded = np.argmax(rho)
    line_name = env.name_line[line_most_overloaded]
    zone_name = zone_for_each_lines[line_name][0]
    zone_index = [alarms_area_names.index(zone_name)]
    return zone_index


def naive_alarm_action(timestep, last_alarm_trigger_timestep, env, rho, disc_lines_before_cascade):
    assert timestep >= last_alarm_trigger_timestep
    if rho.max() < 1.1:
        return None
    if timestep - last_alarm_trigger_timestep < 7:
        return None

    zone_index = calculate_zone_for_alarm(env, rho, disc_lines_before_cascade)
    alarm_action = env.action_space({"raise_alarm": zone_index})
    return alarm_action


if len(sys.argv) < 2:
    print("Not enough arguments. USAGE: <NumScenarios> <model_name>")
    exit()

number_of_scenarios = int(sys.argv[1])

model_name = str(sys.argv[2])
if model_name != "naive":
    model = tfk.models.load_model(os.path.join("./data/model/" + model_name + ".tf"))


SEED = 0
random.seed(SEED)

env = grid2op.make("l2rpn_icaps_2021_large_val", backend=LightSimBackend(), reward_class=RedispReward)
env.seed(SEED)
env.reset()

EPISODES_DATA_PATH = "data/episodes_data_val"

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

episode_data_index = 0
alarm_scores = []
episode_names = []

for episode_data in episodes_data:
    episode_name = episodes_data_files[episode_data_index].split("-", 1)[-1].split(".", 1)[0]
    episode_names.append(episode_name)
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
        disc_lines_before_cascade = features["disc_lines_before_cascade"]

        feature_last_timestep_rho = None
        if current_data_index > 0:
            last_timestep_data = episode_data[current_data_index - 1]
            if last_timestep_data["timestep"] == timestep - 1:
                feature_last_timestep_rho = last_timestep_data["features"]["rho"]

        alarm_is_legal = alarm.budget >= alarm.alarm_cost
        valid_actions = []
        raise_alarm_vect = None
        rho = features["rho"]
        if alarm_is_legal:
            valid_actions = [
                env.action_space({"raise_alarm": 0}),
                env.action_space({"raise_alarm": 1}),
                env.action_space({"raise_alarm": 2}),
            ]
            # alarm_action = None
            # alarm_action = valid_actions[0]
            if model_name == "naive":
                alarm_action = naive_alarm_action(
                    timestep, last_alarm_trigger_timestep, env, rho, disc_lines_before_cascade
                )
            else:
                alarm_action = nn_alarm_action(
                    timestep,
                    last_alarm_trigger_timestep,
                    env,
                    feature_last_timestep_rho,
                    features,
                    disc_lines_before_cascade,
                )
            # alarm_action = None
            if alarm_action != None:
                raise_alarm_vect = alarm_action.raise_alarm
                last_alarm_trigger_timestep = timestep

        alarm.update_timestep(timestep, raise_alarm_vect)
        # print(feature_rho)
    print(
        "<<<<<<<<<<<<<<<<<< DONE EPISODE:",
        episode_data_index + 1,
        "of",
        len(episodes_data),
        " Alarm score:",
        alarm_scores[len(alarm_scores) - 1],
    )
    episode_data_index += 1

print("Num episodes:", len(episode_names))
print("Episodes:", episode_names)
print("Alarm scores", alarm_scores)
average_alarm_score = 0
for alarm_score in alarm_scores:
    average_alarm_score += alarm_score
average_alarm_score = average_alarm_score / len(alarm_scores)
print("-> Average alarm score:", average_alarm_score)
print(
    "number_of_alarm_failures_due_to_no_info_in_previous_timesteps:",
    number_of_alarm_failures_due_to_no_info_in_previous_timesteps,
)
print(
    "number_of_alarm_failures_due_to_action_leading_to_game_over:",
    number_of_alarm_failures_due_to_action_leading_to_game_over,
)

print("FINISH!")
