from copy import copy
import os
from random import randrange, uniform
import json
import datetime
import time
import inspect
import numpy as np
import sys
import pickle
import os.path

from numpy import ma
from numpy.core.numeric import NaN

# Create buckets!

# First try: normalized? rho of each line, max rho?. Bus for each load/gen/line_or/line_ex. If line disconnected line_or and line_ex in bus -1.

RHO_BUCKET_STEP_PERCENTAGE = 0.15
MIN_RHO = 0.4
MAX_RHO = 5

# NUM_LINES = 59
TOPOLOGY_VECTOR_LENGTH = 177

# Bus is -1/1/2

# DO: Load/Save buckets from disk


class Buckets:
    def __init__(self, save_name):
        self.initialized = False
        self.num_actions = -1
        self.save_name = save_name

    def save_buckets_to_disk(self):
        print("Saving buckets to file:", self.save_name)
        with open(self.save_name, "wb") as f:
            pickle.dump(self.buckets_, f, pickle.HIGHEST_PROTOCOL)
        print("Saved buckets to", self.save_name)

    def load_buckets_from_disk(self):
        with open(self.save_name, "rb") as f:
            return pickle.load(f)

    def generate_rho_buckets_ceilings(self):
        bucket_ceilings = [MIN_RHO]
        while bucket_ceilings[-1] < MAX_RHO:
            bucket_ceilings.append(bucket_ceilings[-1] + bucket_ceilings[-1] * RHO_BUCKET_STEP_PERCENTAGE)
        return bucket_ceilings

    def num_rho_buckets(self):
        bucket_ceilings = self.generate_rho_buckets_ceilings()
        return len(bucket_ceilings) + 1  # Last bucket is > max

    def rho_to_bucket(self, rho):
        bucket_ceilings = self.generate_rho_buckets_ceilings()
        for i in range(0, len(bucket_ceilings)):
            if bucket_ceilings[i] > rho:
                return i
        return len(bucket_ceilings)

    def bus_to_bucket(self, bus):
        assert bus == -1 or bus == 1 or bus == 2
        if bus == -1:
            return 0
        return bus  # Maybe we should encode 1 as 0 since it is more common ??.

    def bucket_hash_of_observation(self, observation):
        lines_rho = observation.rho
        rho_buckets = []
        for line_rho in lines_rho:
            rho_buckets.append(self.rho_to_bucket(line_rho))

        topology_vector = observation.topo_vect
        assert len(topology_vector) == TOPOLOGY_VECTOR_LENGTH

        bus_buckets = []
        for bus in topology_vector:
            bus_buckets.append(self.bus_to_bucket(bus))

        hash = "".join(map(str, rho_buckets + bus_buckets))
        return hash

    def initalize(self, all_actions):
        self.initialized = True
        self.num_actions = len(all_actions)
        if os.path.isfile(self.save_name):
            self.buckets_ = self.load_buckets_from_disk()
            print("Loaded buckets from", self.save_name)
            assert np.array_equal(self.buckets_["actions"], all_actions)
        else:
            self.buckets_ = {}
            self.buckets_["actions"] = all_actions

    def initialzie_bucket(self, bucket_hash):
        self.buckets_[bucket_hash] = {"action_values": np.array([0.0] * self.num_actions)}

    def get_actions_sorted_by_value(self, observation):
        action_index = -1
        bucket_hash = self.bucket_hash_of_observation(observation)
        assert self.initialized

        if bucket_hash not in self.buckets_:
            return np.array([])

        # Indices of actions sorted by values (Biggest values first)
        sorted_action_indexes = np.flip(np.argsort(self.buckets_[bucket_hash]["action_values"]))

        return sorted_action_indexes

    def initialzie_working_memory_bucket(self, bucket_hash):
        self.working_memory[bucket_hash] = {"action_values": np.array([0.0] * self.num_actions)}
        if bucket_hash in self.buckets_:
            np.copyto(self.working_memory[bucket_hash]["action_values"], self.buckets_[bucket_hash]["action_values"])

    def init_learning_batch(self):
        self.working_memory = {}

    def finalize_learning_batch(self, winner_buckets_hashes, winner_action_indexes):
        for bucket_hash in self.working_memory:
            if bucket_hash not in self.buckets_:
                self.initialzie_bucket(bucket_hash)
            # Normalize batch values between -1 and 1
            assert np.isfinite(self.working_memory[bucket_hash]["action_values"]).all()
            assert np.isfinite(np.abs(self.working_memory[bucket_hash]["action_values"]).all())

            max_abs_val = np.max(np.abs(self.working_memory[bucket_hash]["action_values"]), axis=0)
            if max_abs_val == 0:
                return
            self.working_memory[bucket_hash]["action_values"] /= max_abs_val
            self.buckets_[bucket_hash]["action_values"] += self.working_memory[bucket_hash]["action_values"]

        if len(winner_buckets_hashes) == 0:
            #######
            # print("Final bucket hashes -------------> :")
            # for bucket_hash in self.working_memory:
            # print(bucket_hash)
            # with np.printoptions(threshold=np.inf):
            # print(self.buckets_[bucket_hash]["action_values"])
            #######
            return

        assert len(winner_buckets_hashes) == len(winner_action_indexes)
        for i in range(0, len(winner_buckets_hashes)):
            self.buckets_[winner_buckets_hashes[i]]["action_values"][winner_action_indexes[i]] += 100

        #######
        # print("Final bucket hashes -------------> :")
        # for bucket_hash in self.working_memory:
        # print(bucket_hash)
        # with np.printoptions(threshold=np.inf):
        # print(self.buckets_[bucket_hash]["action_values"])
        #######

    def update_bucket_action_values_Q_Learning(self, action_index, bucket_hash, post_bucket_hash, reward):
        # Q-learning:
        # Q(St,At) <- Q(St,At) + alpha(Rt+1 + gamma*max_a(Q(St+1,a)) - Q(St,At))
        ALPHA = 0.1
        GAMMA = 0.6

        assert self.initialized
        if bucket_hash not in self.working_memory:
            self.initialzie_working_memory_bucket(bucket_hash)
        max_post_action_value = 0
        if post_bucket_hash != None:
            if post_bucket_hash not in self.working_memory:
                self.initialzie_working_memory_bucket(post_bucket_hash)
            # Maximum value excluding 0 because actiosn with value 0 may be invalid (Even though thats not necessarilly the case...)
            masked_array = np.ma.masked_equal(self.working_memory[post_bucket_hash]["action_values"], 0.0, copy=False)
            max_post_action_value = 0.0
            if masked_array.count() > 0:
                max_post_action_value = np.max(masked_array)
        # print("----------")
        # print(bucket_hash)
        old_action_value = self.working_memory[bucket_hash]["action_values"][action_index]
        new_action_value = old_action_value + ALPHA * (reward + GAMMA * max_post_action_value - old_action_value)

        self.working_memory[bucket_hash]["action_values"][action_index] = new_action_value

    #      with np.printoptions(threshold=np.inf):
    #           print(bucket_hash)
    #            print(self.working_memory[bucket_hash]["action_values"])

    def select_action_Q_Learning(self, observation, banned_actions_indexes):
        EPSILON = 0.05

        action_index = -1
        bucket_hash = self.bucket_hash_of_observation(observation)
        assert self.initialized
        if bucket_hash not in self.working_memory:
            self.initialzie_working_memory_bucket(bucket_hash)
        assert len(banned_actions_indexes) < len(self.working_memory[bucket_hash]["action_values"])
        while True:
            if uniform(0, 1) < EPSILON:  # Explore action space
                action_index = randrange(len(self.working_memory[bucket_hash]["action_values"]))
            else:
                action_index = np.argmax(self.working_memory[bucket_hash]["action_values"])  # Exploit learned values
            if action_index not in banned_actions_indexes:
                return action_index
