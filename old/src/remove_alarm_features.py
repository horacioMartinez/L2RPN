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

if len(sys.argv) < 1:
    print("Not enough arguments. USAGE: <features_path>")
    exit()

features_path = str(sys.argv[1])


feature_files = [f for f in listdir(features_path) if isfile(join(features_path, f))]

for feature_file in feature_files:
    feature_file = features_path + feature_file
    with open(feature_file, "rb") as f:
        training_data = pickle.load(f)

    input_data = training_data["input_data"]
    labels = training_data["labels"]
    assert len(input_data[0]) == 694
    new_input_data = []
    print("Procesing file:", feature_file)
    for i in range(0, len(input_data)):
        alarm_feature_indexes = [0, 1, 2, 3]
        new_input_data.append(np.delete(input_data[i], alarm_feature_indexes))
    print(str(len(input_data)) + "/" + str(len(input_data)))
    new_input_data = np.array(new_input_data)
    assert len(new_input_data[0]) == 690
    training_data["input_data"] = new_input_data
    del input_data
    gc.collect()
    print("Saving new feature file:", feature_file)
    with open(feature_file, "wb") as f:
        pickle.dump(training_data, f, pickle.HIGHEST_PROTOCOL)


print("FINISH!")
