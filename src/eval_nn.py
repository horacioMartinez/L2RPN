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
import os
import time
import numpy as np
from multiprocessing import cpu_count
import tensorflow as tf
import tensorflow.keras as tfk
import tensorflow.keras.optimizers as tfko
import tensorflow.keras.layers as tfkl
import tensorflow.keras.activations as tfka

# load model
model = tfk.models.load_model("data/model-40.h5")
# summarize model.
model.summary()
# load dataset

with open("data/nn_val_data.pkl", "rb") as f:
    training_data = pickle.load(f)

input_data = training_data["input_data"]
labels = training_data["labels"]

rho_feature = []
for i in range(0, len(input_data)):
    rho_feature.append(input_data[i][0])

rho_feature = np.array(rho_feature)
labels = np.array(labels)

# evaluate the model
score = model.evaluate(rho_feature, labels, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], score[1] * 100))

accuracy_of_always_false = ((len(labels) - np.count_nonzero(labels)) / len(labels)) * 100
print("Accuracy of always picking False:", accuracy_of_always_false, "%")
