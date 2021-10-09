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
from tensorflow.python.keras.layers.advanced_activations import LeakyReLU
from tensorflow.python.keras.models import Sequential
from tensorflow.keras.layers.experimental.preprocessing import Normalization


def build_model_1(input_data):
    norm_layer = Normalization()
    norm_layer.adapt(input_data)
    model = tfk.Sequential()
    model.add(norm_layer)
    model.add(tfk.layers.Dense(460, input_dim=694, activation="relu"))
    model.add(tfk.layers.Dense(140, activation="relu"))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def build_model_2(input_data):
    model = tfk.Sequential()
    model.add(tfk.layers.Dense(460, input_dim=694, activation="relu"))
    model.add(tfk.layers.Dense(140, activation="relu"))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def build_model_3(input_data):
    norm_layer = Normalization()
    norm_layer.adapt(input_data)
    model = tfk.Sequential()
    model.add(norm_layer)
    model.add(tfk.layers.Dense(460, input_dim=694, activation="relu"))
    model.add(tfk.layers.Dense(200, activation="relu"))
    model.add(tfk.layers.Dense(60, activation="relu"))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def build_model_4(input_data):
    norm_layer = Normalization()
    norm_layer.adapt(input_data)
    model = tfk.Sequential()
    model.add(norm_layer)
    model.add(tfk.layers.Dense(520, input_dim=694, activation="relu"))
    model.add(tfk.layers.Dense(360, activation="relu"))
    model.add(tfk.layers.Dense(180, activation="relu"))
    model.add(tfk.layers.Dense(40, activation="relu"))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def build_model_5(input_data):
    norm_layer = Normalization()
    norm_layer.adapt(input_data)
    model = tfk.Sequential()
    model.add(norm_layer)
    model.add(tfk.layers.Dense(520, input_dim=694))
    model.add(tfk.layers.LeakyReLU(alpha="0.01"))
    model.add(tfk.layers.Dense(360))
    model.add(tfk.layers.LeakyReLU(alpha="0.01"))
    model.add(tfk.layers.Dense(180))
    model.add(tfk.layers.LeakyReLU(alpha="0.01"))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tfk.layers.Dense(40))
    model.add(tfk.layers.LeakyReLU(alpha="0.01"))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def build_model_6(input_data):
    norm_layer = Normalization()
    norm_layer.adapt(input_data)
    model = tfk.Sequential()
    model.add(norm_layer)
    model.add(tfk.layers.Dense(520, input_dim=694, activation="relu"))
    model.add(tfk.layers.Dense(460, activation="relu"))
    model.add(tfk.layers.Dense(240, activation="relu"))
    model.add(tfk.layers.Dense(120, activation="relu"))
    model.add(tfk.layers.Dense(20, activation="relu"))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def build_model_7(input_data):
    # PPO
    norm_layer = Normalization()
    norm_layer.adapt(input_data)
    model = tfk.Sequential()
    model.add(norm_layer)
    model.add(tfk.layers.Dense(694, input_dim=694, activation="relu"))
    model.add(tfk.layers.Dense(694, activation="relu"))
    model.add(tfk.layers.Dense(694, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tfk.layers.Dense(694, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


if len(sys.argv) < 4:
    print("Not enough arguments. USAGE: <model_X> <Train/Eval> <epochs> <batch_size>")
    exit()


model_name = str(sys.argv[1])
assert str(sys.argv[2]) == "Train"
epochs = int(sys.argv[3])  # 300
batch_size = int(sys.argv[4])  # 64

with open("data/nn_training_data/nn_training_data-0.pkl", "rb") as f:
    training_data = pickle.load(f)

input_data = training_data["input_data"]
labels = training_data["labels"]
assert len(input_data[0]) == 694

if model_name == "model_1":
    model = build_model_1(input_data)
elif model_name == "model_2":
    model = build_model_2(input_data)
elif model_name == "model_3":
    model = build_model_3(input_data)
elif model_name == "model_4":
    model = build_model_4(input_data)
elif model_name == "model_5":
    model = build_model_5(input_data)
elif model_name == "model_6":
    model = build_model_6(input_data)
elif model_name == "model_7":
    model = build_model_7(input_data)
else:
    assert False

print("MODEL:", model_name)
model.summary()
tf.keras.utils.plot_model(model, "img/" + model_name + ".png", show_shapes=True)

# fit the keras model on the dataset
# Increase batch size in gpu !
model.fit(input_data, labels, epochs=epochs, batch_size=batch_size)

model.save("data/" + model_name + ".h5")
print("Saved model to disk")

_, accuracy = model.evaluate(input_data, labels)
print("Accuracy: %.2f" % (accuracy * 100))
