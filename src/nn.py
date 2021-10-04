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

# >>>>>> Should i map rho of 0 to 99 (To make it clean that higher rho is worse) ???
# >>>>>> Should i normalize inputs ???

with open("data/nn_training_data.pkl", "rb") as f:
    training_data = pickle.load(f)

input_data = training_data["input_data"]
labels = training_data["labels"]

rho_feature = []
for i in range(0, len(input_data)):
    rho_feature.append(input_data[i][0])

rho_feature = np.array(rho_feature)
labels = np.array(labels)
# Usar shuffle=True para mezclar los datos!

model = tfk.Sequential()
# rho 59 dims
model.add(tfk.layers.Dense(20, input_dim=59, activation="relu"))
model.add(tfk.layers.Dense(8, activation="relu"))
model.add(tfk.layers.Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# fit the keras model on the dataset
model.fit(rho_feature, labels, epochs=150, batch_size=100)

model.save("model.h5")
print("Saved model to disk")

_, accuracy = model.evaluate(rho_feature, labels)
print("Accuracy: %.2f" % (accuracy * 100))


#     input_shape = (self.observation_size * self.num_frames,)
#     input_layer = tfk.Input(shape = input_shape, name="input_obs")
#     lay1 = tfkl.Dense(self.observation_size * 2, name="fc_1")(input_layer)
#     lay1 = tfka.relu(lay1, alpha=0.01) #leaky_relu

#     lay2 = tfkl.Dense(self.observation_size, name="fc_2")(lay1)
#     lay2 = tfka.relu(lay2, alpha=0.01) #leaky_relu

#     lay3 = tfkl.Dense(896, name="fc_3")(lay2)
#     lay3 = tfka.relu(lay3, alpha=0.01) #leaky_relu

#     lay4 = tfkl.Dense(512, name="fc_4")(lay3)
#     lay4 = tfka.relu(lay4, alpha=0.01) #leaky_relu

#     advantage = tfkl.Dense(384, name="fc_adv")(lay4)
#     advantage = tfka.relu(advantage, alpha=0.01) #leaky_relu
#     advantage = tfkl.Dense(self.action_size, name="adv")(advantage)
#     advantage_mean = tf.math.reduce_mean(advantage,
#                                          axis=1, keepdims=True,
#                                          name="adv_mean")
#     advantage = tfkl.subtract([advantage, advantage_mean],
#                               name="adv_subtract")

#     value = tfkl.Dense(384, name="fc_val")(lay4)
#     value = tfka.relu(value, alpha=0.01) #leaky_relu
#     value = tfkl.Dense(1, name="val")(value)

#     Q = tf.math.add(value, advantage, name="Qout")

#     self.model = tfk.Model(inputs=[input_layer], outputs=[Q],
#                            name=self.__class__.__name__)

#     # Backwards pass
#     self.schedule = tfko.schedules.InverseTimeDecay(self.lr,
#                                                     self.lr_decay_steps,
#                                                     self.lr_decay_rate)
#     self.optimizer = tfko.Adam(learning_rate=self.schedule, clipnorm=1.0)

# def train_on_batch(self, x, y_true, sample_weight):
#     with tf.GradientTape() as tape:
#         # Get y_pred for batch
#         y_pred = self.model(x)

#         # Compute loss for each sample in the batch
#         batch_loss = self._batch_loss(y_true, y_pred)

#         # Apply samples weights
#         tf_sample_weight = tf.convert_to_tensor(sample_weight,
#                                                 dtype=tf.float32)
#         batch_loss = tf.math.multiply(batch_loss, tf_sample_weight)

#         # Compute mean scalar loss
#         loss = tf.math.reduce_mean(batch_loss)

#     # Compute gradients
#     grads = tape.gradient(loss, self.model.trainable_variables)

#     # Apply gradients
#     grad_pairs = zip(grads, self.model.trainable_variables)
#     self.optimizer.apply_gradients(grad_pairs)

#     # Store LR
#     self.train_lr = self.optimizer._decayed_lr('float32').numpy()
#     # Return loss scalar
#     return loss.numpy()

# def _batch_loss(self, y_true, y_pred):
#     sq_error = tf.math.square(y_true - y_pred, name="sq_error")

#     # We store it because that's the priorities vector
#     # for importance update
#     batch_sq_error = tf.math.reduce_sum(sq_error, axis=1,
#                                         name="batch_sq_error")
#     # Stored as numpy array since we are in eager mode
#     self.batch_sq_error = batch_sq_error.numpy()

#     return batch_sq_error

# def random_move(self):
#     opt_policy = np.random.randint(0, self.action_size)

#     return opt_policy

# def predict_move(self, data):
#     model_input = data.reshape(1, self.observation_size * self.num_frames)
#     q_actions = self.model.predict(model_input, batch_size = 1)
#     opt_policy = np.argmax(q_actions)

#     return opt_policy, q_actions[0]

# def update_target_hard(self, target_model):
#     this_weights = self.model.get_weights()
#     target_model.set_weights(this_weights)

# def update_target_soft(self, target_model, tau=1e-2):
#     tau_inv = 1.0 - tau
#     # Get parameters to update
#     target_params = target_model.trainable_variables
#     main_params = self.model.trainable_variables

#     # Update each param
#     for i, var in enumerate(target_params):
#         var_persist = var.value() * tau_inv
#         var_update = main_params[i].value() * tau
#         # Poliak averaging
#         var.assign(var_update + var_persist)

# def save_network(self, path):
#     # Saves model at specified path as h5 file
#     self.model.save(path)
#     print("Successfully saved model at: {}".format(path))

# def load_network(self, path):
#     # Load from a model.h5 file
#     self.model.load_weights(path)
#     print("Successfully loaded network from: {}".format(path))
