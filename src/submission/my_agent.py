import os
import time
import numpy as np
from grid2op.Agent import BaseAgent
import tensorflow as tf
import tensorflow.keras as tfk


class MyAgent(BaseAgent):
    def __init__(self, env, action_space, this_directory_path="./"):
        self.name = "agent1"
        self.ALARM_RHO_THRESHOLD = 0.0
        self.RHO_THRESHOLD = 1.0
        self.RHO_THRESHOLD_RECONNECT = 1.0

        BaseAgent.__init__(self, action_space)
        self.action_space = action_space
        self.do_nothing_action = action_space({})

        self.do_nothing_action_vect = np.array([self.do_nothing_action.to_vect()])
        self.bus_actions62 = np.load(os.path.join(this_directory_path, "data/bus_actions62_2021.npy"))
        self.bus_actions146 = np.load(os.path.join(this_directory_path, "data/bus_actions146_2021.npy"))
        self.bus_actions_62_146 = np.concatenate((self.bus_actions62, self.bus_actions146), axis=0)
        self.all_actions = np.concatenate((self.do_nothing_action_vect, self.bus_actions_62_146), axis=0)
        self.disc_lines_before_cascade = []
        self.last_alarm_trigger_timestep = -1

        model_name = "model_4-weights.02-0.9955"
        self.model = tfk.models.load_model(os.path.join(this_directory_path, "data/" + model_name + ".h5"))

        self.previous_rho_for_alarm = None

    def is_legal_bus_action(self, action, obs):
        adict = action.as_dict()
        # if "change_bus_vect" not in adict:
        # assert False
        substation_to_operate = int(adict["change_bus_vect"]["modif_subs_id"][0])
        if obs.time_before_cooldown_sub[substation_to_operate]:
            return False
        for line in [
            eval(key)
            for key, val in adict["change_bus_vect"][str(substation_to_operate)].items()
            if "line" in val["type"]
        ]:
            if obs.time_before_cooldown_line[line] or not obs.line_status[line]:
                return False
        return True

    def _reset_topology(self, observation):
        if np.max(observation.rho) < 0.95:
            offset = 0
            for sub_id, sub_elem_num in enumerate(observation.sub_info):
                sub_topo = self.sub_topo_dict[sub_id]

                if sub_id == 28:
                    sub28_topo = np.array([2, 1, 2, 1, 1])
                    if (
                        not np.all(sub_topo.astype(int) == sub28_topo.astype(int))
                        and observation.time_before_cooldown_sub[sub_id] == 0
                    ):
                        sub_id = 28
                        act = self.action_space({"set_bus": {"substations_id": [(sub_id, sub28_topo)]}})

                        (
                            obs_simulate,
                            reward_simulate,
                            done_simulate,
                            info_simulate,
                        ) = observation.simulate(act)
                        observation._obs_env._reset_to_orig_state()
                        # assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]
                        if not done_simulate and obs_simulate is not None and not any(np.isnan(obs_simulate.rho)):
                            if np.max(obs_simulate.rho) < 0.95:
                                return act
                    continue

                if np.any(sub_topo == 2) and observation.time_before_cooldown_sub[sub_id] == 0:
                    sub_topo = np.where(sub_topo == 2, 1, sub_topo)  # bus 2 to bus 1
                    sub_topo = np.where(sub_topo == -1, 0, sub_topo)  # don't do action in bus=-1
                    reconfig_sub = self.action_space({"set_bus": {"substations_id": [(sub_id, sub_topo)]}})

                    (
                        obs_simulate,
                        reward_simulate,
                        done_simulate,
                        info_simulate,
                    ) = observation.simulate(reconfig_sub)
                    observation._obs_env._reset_to_orig_state()

                    # assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

                    # if not done_simulate:
                    # assert np.any(obs_simulate.topo_vect != observation.topo_vect)  # have some impact

                    if not done_simulate and obs_simulate is not None and not any(np.isnan(obs_simulate.rho)):
                        if np.max(obs_simulate.rho) < 0.95:
                            return reconfig_sub

        if np.max(observation.rho) >= 1.0:
            sub_id = 28
            sub_topo = self.sub_topo_dict[sub_id]
            if np.any(sub_topo == 2) and observation.time_before_cooldown_sub[sub_id] == 0:
                sub28_topo = np.array([1, 1, 1, 1, 1])
                act = self.action_space({"set_bus": {"substations_id": [(sub_id, sub28_topo)]}})

                (
                    obs_simulate,
                    reward_simulate,
                    done_simulate,
                    info_simulate,
                ) = observation.simulate(act)
                observation._obs_env._reset_to_orig_state()
                # assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]
                if not done_simulate and obs_simulate is not None and not any(np.isnan(obs_simulate.rho)):
                    if np.max(obs_simulate.rho) < 0.99:
                        return act

    def _calc_sub_topo_dict(self, observation):
        offset = 0
        self.sub_topo_dict = {}
        for sub_id, sub_elem_num in enumerate(observation.sub_info):
            sub_topo = observation.topo_vect[offset : offset + sub_elem_num]
            offset += sub_elem_num
            self.sub_topo_dict[sub_id] = sub_topo

    def _reconnect_action(self, observation):
        disconnected = np.where(observation.line_status == False)[0].tolist()

        for line_id in disconnected:
            if observation.time_before_cooldown_line[line_id] == 0:
                action = self.action_space({"set_line_status": [(line_id, +1)]})
                simulation_obs, _, _, _ = observation.simulate(action)
                observation._obs_env._reset_to_orig_state()

                if (
                    np.max(observation.rho) < self.RHO_THRESHOLD_RECONNECT
                    and np.max(simulation_obs.rho) >= self.RHO_THRESHOLD_RECONNECT
                ):
                    continue

                return action

    def is_legal_action(self, action, observation):
        if action == self.do_nothing_action:
            return True
        return self.is_legal_bus_action(action, observation)

    def combine_actions(self, actionA, actionB, observation):
        if actionA == None:
            return actionB
        if actionB == None:
            return actionA
        combined_action = actionA + actionB
        (
            obs_simulate,
            reward_simulate,
            done_simulate,
            info_simulate,
        ) = observation.simulate(combined_action)
        observation._obs_env._reset_to_orig_state()
        # assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]
        return combined_action

    def calculate_zone_for_alarm(self, env, rho):
        alarms_lines_area = env.alarms_lines_area
        alarms_area_names = env.alarms_area_names
        zone_for_each_lines = alarms_lines_area

        ####### from disc_lines_before_cascade
        combined_disc_lines_before_cascade = np.concatenate(self.disc_lines_before_cascade).astype(int)
        if len(combined_disc_lines_before_cascade) > 0:
            last_disconnected_line = combined_disc_lines_before_cascade[len(combined_disc_lines_before_cascade) - 1]
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

    def naive_alarm_action(self, timestep, env, observation):
        rho = observation.rho
        alarm_budget = observation.attention_budget
        last_alarm_trigger_timestep = self.last_alarm_trigger_timestep

        BUDGET_INTERVALS = [[1.0, 2.5], [2.5, 3.0]]
        RHO_OR_PREDICTION_INTERVALS = [1.024, 1.024]
        MIN_DELTA_TIMESTEP = [5, 7]

        #######################################################
        # assert timestep >= last_alarm_trigger_timestep
        # assert alarm_budget >= 1.0
        # assert len(BUDGET_INTERVALS) == len(RHO_OR_PREDICTION_INTERVALS)
        # assert len(BUDGET_INTERVALS) == len(MIN_DELTA_TIMESTEP)
        found = False
        rho_or_prediction_threshold = -1
        min_delta = -1
        for i in range(0, len(BUDGET_INTERVALS)):
            budget_interval = BUDGET_INTERVALS[i]
            if budget_interval[0] <= alarm_budget <= budget_interval[1]:
                found = True
                rho_or_prediction_threshold = RHO_OR_PREDICTION_INTERVALS[i]
                min_delta = MIN_DELTA_TIMESTEP[i]
        # assert found
        if self.last_alarm_trigger_timestep > 0:
            if timestep - last_alarm_trigger_timestep < min_delta:
                return None

        if rho.max() < rho_or_prediction_threshold:  # and not some_line_disconnected:
            return None
        #######################################################

        zone_index = self.calculate_zone_for_alarm(env, rho)
        alarm_action = self.action_space({"raise_alarm": zone_index})
        return alarm_action

    def nn_alarm_action(self, timestep, env, observation):
        rho = observation.rho
        alarm_budget = observation.attention_budget
        last_alarm_trigger_timestep = self.last_alarm_trigger_timestep

        BUDGET_INTERVALS = [[1.0, 3]]
        RHO_OR_PREDICTION_INTERVALS = [0.2]
        MIN_DELTA_TIMESTEP = [5]

        #######################################################
        # assert timestep >= last_alarm_trigger_timestep
        # assert alarm_budget >= 1.0
        # assert len(BUDGET_INTERVALS) == len(RHO_OR_PREDICTION_INTERVALS)
        # assert len(BUDGET_INTERVALS) == len(MIN_DELTA_TIMESTEP)
        found = False
        rho_or_prediction_threshold = -1
        min_delta = -1
        trigger_index = -1
        for i in range(0, len(BUDGET_INTERVALS)):
            budget_interval = BUDGET_INTERVALS[i]
            if budget_interval[0] <= alarm_budget <= budget_interval[1]:
                found = True
                rho_or_prediction_threshold = RHO_OR_PREDICTION_INTERVALS[i]
                min_delta = MIN_DELTA_TIMESTEP[i]
                trigger_index = i
        # assert found
        if self.last_alarm_trigger_timestep > 0:
            if timestep - last_alarm_trigger_timestep < min_delta:
                return None
        #######################################################

        processed_features = self.extract_alarm_features(observation)
        prediction = self.model.predict(np.array([processed_features]))[0][0]
        if prediction < rho_or_prediction_threshold:
            return None
        zone_index = self.calculate_zone_for_alarm(env, rho)
        alarm_action = self.action_space({"raise_alarm": zone_index})
        return alarm_action

    def process_alarm_action(self, env, observation, current_time_step):
        # return self.naive_alarm_action(current_time_step, env, observation)
        # return self.nn_alarm_action(current_time_step, env, observation)
        now = time.time()
        time_delta = int(now - self.start_time)

        alarm_action = self.naive_alarm_action(current_time_step, env, observation)

        if alarm_action == None and time_delta < 175:
            alarm_action = self.nn_alarm_action(current_time_step, env, observation)
        return alarm_action

    def extract_alarm_features(self, obs):
        if self.previous_rho_for_alarm is None:
            feature_rho_delta = np.zeros_like(obs.rho)
        else:
            feature_rho_delta = self.previous_rho_for_alarm - obs.rho

        processed_features = np.array([])

        # feature_actions_rho = features["actions_rho"]
        feature_rho = obs.rho
        feature_topo_vect = obs.topo_vect
        feature_load_p = obs.load_p
        feature_load_q = obs.load_q
        feature_load_v = obs.load_v
        feature_gen_p = obs.gen_p
        feature_gen_q = obs.gen_q
        feature_gen_v = obs.gen_v
        feature_month = obs.month
        feature_day = obs.day
        feature_day_of_week = obs.day_of_week
        feature_hour_of_day = obs.hour_of_day
        feature_minute_of_hour = obs.minute_of_hour
        feature_timestep_overflow = obs.timestep_overflow
        feature_time_before_cooldown_line = obs.time_before_cooldown_line
        feature_time_before_cooldown_sub = obs.time_before_cooldown_sub
        feature_time_next_maintenance = obs.time_next_maintenance

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

        # assert not np.isnan(processed_features).any()
        # assert len(processed_features) == 690
        return processed_features

    def act(self, observation, reward, done):
        env = observation._obs_env
        current_time_step = env.nb_time_step
        if current_time_step < 1:
            self.last_alarm_trigger_timestep = -1
            self.disc_lines_before_cascade = []
            self.start_time = time.time()

        self.disc_lines_before_cascade.append(list(np.where(observation.line_status == False)[0]))
        if (len(self.disc_lines_before_cascade)) > 4:
            self.disc_lines_before_cascade.pop(0)
        self._calc_sub_topo_dict(observation)
        some_line_disconnected = not np.all(observation.topo_vect != -1)

        alarm_action = None
        alarm_is_legal = observation.attention_budget[0] >= 1.0
        if alarm_is_legal:
            alarm_action = self.process_alarm_action(env, observation, current_time_step)
            if alarm_action != None:
                self.last_alarm_trigger_timestep = current_time_step
        self.previous_rho_for_alarm = observation.rho

        if some_line_disconnected:
            action = self._reconnect_action(observation)
            if action is not None:
                return self.combine_actions(alarm_action, action, observation)

        below_rho_threshold = observation.rho.max() < self.RHO_THRESHOLD

        if below_rho_threshold:  # No overflow
            if not some_line_disconnected:
                action = self._reset_topology(observation)
                if action is not None:
                    return self.combine_actions(alarm_action, action, observation)
            _, _, done, _ = observation.simulate(self.do_nothing_action)
            observation._obs_env._reset_to_orig_state()
            action = self.do_nothing_action
            return self.combine_actions(alarm_action, action, observation)

        o, _, d, info_simulate = observation.simulate(self.do_nothing_action)
        observation._obs_env._reset_to_orig_state()
        # assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]

        min_rho = o.rho.max() if not d else 9999

        # 1-depth simulation search of action with least rho.
        selected_action = self.action_space({})
        min_rho = 99
        # count_disconnected_real = len(observation.rho) - np.count_nonzero(observation.rho)
        for action_vect in self.all_actions:
            # if count_disconnected_real >= 2:
            # continue
            action = self.action_space.from_vect(action_vect)
            is_legal = self.is_legal_action(action, observation)

            if not is_legal:
                continue

            obs, _, done, info_simulate = observation.simulate(action)
            observation._obs_env._reset_to_orig_state()
            # assert not info_simulate["is_illegal"] and not info_simulate["is_ambiguous"]
            if done:
                continue

            count_disconnected_sim = len(obs.rho) - np.count_nonzero(obs.rho)
            THRESHOLD_MAX_COUNT_DISCONNECTED_SIMUL = 2
            if count_disconnected_sim >= THRESHOLD_MAX_COUNT_DISCONNECTED_SIMUL:
                continue

            if obs.rho.max() < min_rho:
                min_rho = obs.rho.max()
                selected_action = action

        return self.combine_actions(alarm_action, selected_action, observation)


def make_agent(env, this_directory_path):
    my_agent = MyAgent(env, env.action_space, this_directory_path)
    return my_agent
