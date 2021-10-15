from os import listdir
from os.path import isfile, join
import gc
import copy
import pickle
import math
import sys
import random
import resource
from random import randrange, seed
from threading import current_thread
import os
import time
import numpy as np
from multiprocessing import cpu_count

np.set_printoptions(suppress=True)
np.set_printoptions(threshold=sys.maxsize)


def extract_timestep_features(timestep_data, previous_timestep_data):
    assert not timestep_data["done"]
    features = timestep_data["features"]

    processed_features = np.array([])

    feature_rho = features["rho"]
    feature_topo_vect = features["topo_vect"]
    feature_load_p = features["load_p"]
    feature_load_q = features["load_q"]
    feature_load_v = features["load_v"]
    feature_gen_p = features["gen_p"]
    feature_gen_q = features["gen_q"]
    feature_gen_v = features["gen_v"]
    feature_month = features["month"]
    feature_day = features["day"]
    feature_day_of_week = features["day_of_week"]
    feature_hour_of_day = features["hour_of_day"]
    feature_minute_of_hour = features["minute_of_hour"]
    feature_timestep_overflow = features["timestep_overflow"]
    feature_time_before_cooldown_line = features["time_before_cooldown_line"]
    feature_time_before_cooldown_sub = features["time_before_cooldown_sub"]
    feature_time_next_maintenance = features["time_next_maintence"]

    if previous_timestep_data is None:
        feature_rho_delta = np.zeros_like(feature_rho)
    else:
        feature_last_timestep_rho = previous_timestep_data["features"]["rho"]
        feature_rho_delta = feature_last_timestep_rho - feature_rho

    processed_features = (
        np.concatenate(
            (
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

    assert not np.isnan(processed_features).any()
    return processed_features


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


if len(sys.argv) < 3:
    print("Not enough arguments. USAGE: <Eval/Train> <NumScenarios (-1 for all)> <Raw/Balanced>")
    exit()

assert str(sys.argv[1]) == "Train" or str(sys.argv[1]) == "Eval"
TRAINING_DATA = str(sys.argv[1]) == "Train"

if TRAINING_DATA:
    EPISODES_DATA_PATH = "data/episodes_data"
else:
    EPISODES_DATA_PATH = "data/episodes_data_val"

number_of_scenarios = int(sys.argv[2])

assert str(sys.argv[3]) == "Raw" or str(sys.argv[3]) == "Balanced"
BALANCED = str(sys.argv[3]) == "Balanced"

random.seed(0)
np.random.seed(0)


episodes_data_files = [
    f for f in listdir(EPISODES_DATA_PATH) if (isfile(join(EPISODES_DATA_PATH, f)) and f != ".gitkeep")
]
random.shuffle(episodes_data_files)

EPISODES_CHUNK_SIZE = 2500
PREPROCESSES_CHUNK_SIZE = 500
if BALANCED:
    EPISODES_CHUNK_SIZE = 250000
    PREPROCESSES_CHUNK_SIZE = 500

episode_data_file_chunks = chunks(episodes_data_files, EPISODES_CHUNK_SIZE)

processed_scenarios = 0
chunk_index = 0
for episode_data_file_chunk in episode_data_file_chunks:
    if TRAINING_DATA:
        if BALANCED:
            prefix = "data/nn_training_data_balanced/nn_training_data-"
        else:
            prefix = "data/nn_training_data/nn_training_data-"
    else:
        if BALANCED:
            prefix = "data/nn_val_data_balanced/nn_val_data-"
        else:
            prefix = "data/nn_val_data/nn_val_data-"
    save_name = prefix + str(chunk_index) + ".pkl"
    chunk_index += 1
    if os.path.isfile(save_name):
        print(">>> FILE ALREADY EXISTS!!:", save_name)
        assert False

    processing_episode_data_file_chunks = chunks(episode_data_file_chunk, PREPROCESSES_CHUNK_SIZE)
    print("Processing chunk: ", chunk_index)
    input_data = []
    labels = []
    for processing_episode_data_file_chunk in processing_episode_data_file_chunks:
        episodes_data = []
        for episodes_data_file in processing_episode_data_file_chunk:
            if number_of_scenarios > 0 and processed_scenarios == number_of_scenarios:
                break
            try:
                with open(EPISODES_DATA_PATH + "/" + episodes_data_file, "rb") as f:
                    try:
                        episodes_data.append(pickle.load(f))
                    except EOFError:
                        print("error on file", episodes_data_file)
                        continue
            except EOFError:
                print("error on file", episodes_data_file)
                continue
            processed_scenarios += 1

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

        for i in range(0, len(episodes_data)):
            timesteps_data = episodes_data[i]
            last_timestep = timesteps_data[len(timesteps_data) - 1]["timestep"]

            if BALANCED:
                non_true_indexes = np.arange(len(timesteps_data) - 12)
                np.random.shuffle(non_true_indexes)
                non_true_indexes = non_true_indexes[:12]
                true_indexes = np.arange(len(timesteps_data) - 12, len(timesteps_data))
                balanced_indexes = [*non_true_indexes, *true_indexes]
            for j in range(0, len(timesteps_data)):
                if BALANCED:
                    if j not in balanced_indexes:
                        continue
                timestep_data = timesteps_data[j]
                if timestep_data["done"]:
                    continue
                previous_timestep_data = None
                if j > 0:
                    previous_timestep_data = timesteps_data[j - 1]
                current_timestep = timestep_data["timestep"]
                does_finish_in_11_or_less_timesteps = (last_timestep - current_timestep) <= 11
                input = extract_timestep_features(timestep_data, previous_timestep_data)
                input_data.append(input)
                labels.append(does_finish_in_11_or_less_timesteps)
            print("chunk_index: ", chunk_index)
            print("processed_scenarios:", processed_scenarios)
            print("Processed episode", i, "out of", len(episodes_data) - 1)
        # del episodes_data
        # gc.collect()

    input_data = np.array(input_data)
    labels = np.array(labels)

    indices = np.arange(len(input_data))

    np.random.shuffle(indices)

    shuffled_input_data = input_data[indices]
    shuffled_labels = labels[indices]

    data = {"input_data": shuffled_input_data, "labels": shuffled_labels}

    print("Saving NN training data to file:", save_name)
    with open(save_name, "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    del input_data
    del shuffled_input_data
    del labels
    del shuffled_labels
    del data
    gc.collect()

print("FINISH!")
