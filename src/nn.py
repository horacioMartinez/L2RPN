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
    model.add(tfk.layers.Dense(460, input_dim=690, activation="relu"))
    model.add(tfk.layers.Dense(140, activation="relu"))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def build_model_2(input_data):
    model = tfk.Sequential()
    model.add(tfk.layers.Dense(460, input_dim=690, activation="relu"))
    model.add(tfk.layers.Dense(140, activation="relu"))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def build_model_3(input_data):
    norm_layer = Normalization()
    norm_layer.adapt(input_data)
    model = tfk.Sequential()
    model.add(norm_layer)
    model.add(tfk.layers.Dense(460, input_dim=690, activation="relu"))
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
    model.add(tfk.layers.Dense(520, input_dim=690, activation="relu"))
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
    model.add(tfk.layers.Dense(520, input_dim=690))
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
    model.add(tfk.layers.Dense(520, input_dim=690, activation="relu"))
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
    model.add(tfk.layers.Dense(690, input_dim=690, activation="relu"))
    model.add(tfk.layers.Dense(690, activation="relu"))
    model.add(tfk.layers.Dense(690, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tfk.layers.Dense(690, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tfk.layers.Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    return model


def eval_model(model_path, balanced):
    if balanced:
        data_path = "data/nn_val_data_balanced/nn_val_data-0.pkl"
    else:
        data_path = "data/nn_val_data/nn_val_data-0.pkl"

    print(model_path)
    model = tfk.models.load_model(model_path)
    model.summary()

    with open(data_path, "rb") as f:
        val_data = pickle.load(f)

    input_data = val_data["input_data"]
    labels = val_data["labels"]
    # evaluate the model
    score = model.evaluate(input_data, labels, verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], score[1] * 100))

    accuracy_of_always_false = ((len(labels) - np.count_nonzero(labels)) / len(labels)) * 100
    print("Accuracy of always picking False:", accuracy_of_always_false, "%")


if len(sys.argv) < 6:
    print("Not enough arguments. USAGE: <model_X> <Train/Eval> <Raw/Balanced> <epochs> <batch_size>")
    exit()

model_name = str(sys.argv[1])
EVAL = str(sys.argv[2]) == "Eval"
if not EVAL:
    assert str(sys.argv[2]) == "Train"
BALANCED = str(sys.argv[3]) == "Balanced"
if not BALANCED:
    assert str(sys.argv[3]) == "Raw"
epochs = int(sys.argv[4])  # 300
batch_size = int(sys.argv[5])  # 64

if BALANCED:
    model_path = "data/model/" + model_name + "-balanced" + ".tf"
else:
    model_path = "data/model/" + model_name + ".tf"

if EVAL:
    eval_model(model_path, BALANCED)
    exit()

if BALANCED:
    data_path = "data/nn_training_data_balanced/nn_training_data-0.pkl"
else:
    data_path = "data/nn_training_data/nn_training_data-0.pkl"

with open(data_path, "rb") as f:
    training_data = pickle.load(f)

input_data = training_data["input_data"]
labels = training_data["labels"]

if len(input_data[0]) == 694:
    print("REMOVE ALARM FEATURES !!")
assert len(input_data[0]) == 690

print("Building model..")
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
print("Model built OK..")

# model.summary()
# tf.keras.utils.plot_model(model, "img/" + model_name + ".png", show_shapes=True)

EPOCH_SAVE_INTERVAL = 100

model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=model_path,
    save_weights_only=False,
    monitor="accuracy",
    mode="max",
    save_best_only=True,
    save_freq="epoch",
    period=EPOCH_SAVE_INTERVAL,
)

SINGLE_FILE = True

if SINGLE_FILE:
    model.fit(input_data, labels, epochs=epochs, batch_size=batch_size, callbacks=[model_checkpoint_callback])
else:
    assert not BALANCED
    data_files = listdir("data/nn_training_data")
    for file in data_files:
        file_path = "data/nn_training_data/" + file
        print("File path", file_path)
        with open(file_path, "rb") as f:
            training_data = pickle.load(f)
        input_data = training_data["input_data"]
        labels = training_data["labels"]
        model.fit(input_data, labels, epochs=epochs, batch_size=batch_size, callbacks=[model_checkpoint_callback])

model.save(model_path)
print("Saved model to disk")

_, accuracy = model.evaluate(input_data, labels)
print("Accuracy: %.2f" % (accuracy * 100))
