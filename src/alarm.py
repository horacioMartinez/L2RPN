# Ver archivos:

# /home/horacio/git/competition/Grid2Op/grid2op/Reward/AlarmReward.py
# /home/horacio/git/competition/Grid2Op/grid2op/Reward/_AlarmScore.py

import numpy as np
import copy


class Alarm:
    """
    This reward is based on the "alarm feature" where the agent is asked to send information about potential issue
    on the grid.

    On this case, when the environment is in a "game over" state (eg it's the end) then the reward is computed
    the following way:

    - if the environment has been successfully manage until the end of the chronics, then 1.0 is returned
    - if no alarm has been raised, then -1.0 is return


    Examples
    ---------
    You can use this reward in any environment with:

    .. code-block:

        import grid2op
        from grid2op.Reward import AlarmReward

        # then you create your environment with it:
        NAME_OF_THE_ENVIRONMENT = "rte_case14_realistic"
        env = grid2op.make(NAME_OF_THE_ENVIRONMENT,reward_class=AlarmReward)
        # and do a step with a "do nothing" action
        obs = env.reset()
        obs, reward, done, info = env.step(env.action_space())
        # the reward is computed with the AlarmReward class


    """

    def __init__(self, env):
        self.env = env

        self.total_time_steps = 0.0
        self.reward_min = -2.0
        self.reward_max = 1.0

        self.n_line = env.n_line
        self.total_time_steps = env.max_episode_duration()
        self.best_time = env.parameters.ALARM_BEST_TIME
        self.window_size = env.parameters.ALARM_WINDOW_SIZE
        if not env._has_attention_budget:
            raise Exception(
                'Impossible to use the "AlarmReward" with an environment for which this feature '
                'is disabled. Please make sure "env._has_attention_budget" is set to ``True`` or '
                "change the reward class with `grid2op.make(..., reward_class=AnyOtherReward)`"
            )

        self.mult_for_right_zone = 2

        self.window_disconnection = 4  # timesteps back to search for disconnected lines
        self.last_processed_timestep = 0
        starting_budget = 2.0
        self.budget = starting_budget
        self.alarm_cost = 1.0
        self.budget_per_ts = 1.0 / (12 * 16)
        self.max_budget = 3.0
        self.triggered_alarms = []

    def is_legal(self, timestep):
        assert timestep >= self.last_processed_timestep
        new_budget = self.budget + (timestep - self.last_processed_timestep) * self.budget_per_ts
        if new_budget < self.alarm_cost:
            return False
        return True

    def trigger_alarm(self, timestep, alarm_action):
        assert self.is_legal(timestep)
        self.budget = self.budget + ((timestep - self.last_processed_timestep) * self.budget_per_ts)
        if self.budget > self.max_budget:
            self.budget = self.max_budget
        self.last_processed_timestep = timestep
        self.budget -= self.alarm_cost
        self.triggered_alarms.append((timestep, copy.deepcopy(alarm_action)))
        assert self.budget >= 0

    def _tmp_score_time(self, step_alarm, step_game_over):
        """
        compute the "temporal" score.

        Should give a number between 0 and 1
        """
        if step_game_over - step_alarm > self.best_time + self.window_size:
            # alarm too soon
            res = 0
        elif step_game_over - step_alarm < self.best_time - self.window_size:
            # alarm too late
            res = 0
        else:
            # square function such that: it gives 1 if step_game_over - step_alarm equals self.best_time
            # and 0 if  step_game_over - step_alarm = self.best_time + self.window_size or
            # if step_game_over - step_alarm self.best_time - self.window_size
            dist_to_game_over = step_game_over - step_alarm
            dist_to_best = dist_to_game_over - self.best_time

            # set it to 0 for the extreme case
            polynom = (dist_to_best - self.window_size) * (dist_to_best + self.window_size)
            # scale it such that it is 1 for dist_to_best == 0 (ie step_game_over - step_alarm == self.best_time)
            res = -polynom / self.window_size ** 2
        return res

    def _mult_for_zone(self, alarm, lines_disconnected_first):
        """compute the multiplicative factor that increases the score if the right zone is predicted"""
        res = 1.0

        if np.sum(alarm) > 1:  # if we have more than one zone in the alarm, we cannot discrtiminate, no bonus points
            return res

        # extract the zones they belong too
        zones_these_lines = set()
        zone_for_each_lines = self.env.alarms_lines_area
        for line_id in lines_disconnected_first:
            print("line_id:", line_id)
            line_name = self.env.name_line[line_id]
            for zone_name in zone_for_each_lines[line_name]:
                zones_these_lines.add(zone_name)

        # now retrieve the id of the zones in which a powerline has been disconnected
        list_zone_names = list(zones_these_lines)
        list_zone_ids = np.where(np.isin(self.env.alarms_area_names, list_zone_names))[0]
        # and finally, award some extra points if one of the zone, containing one of the powerline disconnected
        # by protection is in the alarm
        if np.any(alarm[list_zone_ids]):
            res *= self.mult_for_right_zone
        return res

    def _points_for_alarm(self, step_alarm, alarm, step_game_over, disc_lines):
        """how much points are given for this specific alarm"""
        score = self.reward_min
        score_for_time = self._tmp_score_time(step_alarm, step_game_over)
        if score_for_time != 0:
            # alarm is in the right time window
            score = score_for_time
            score *= self._mult_for_zone(alarm, disc_lines) / self.mult_for_right_zone
        return score

    #     if not done:
    #         disc_lines_before_cascade.append(list(np.where(info["disc_lines"]==0)[0]))
    #     else:
    #         disc_lines_in_cascade=list(np.where(info["disc_lines"]==0)[0])
    def compute_score(self, timestep, won, disconnected_lines_before_game_over, disconnected_lines_at_game_over):
        step_game_over = timestep
        if won:
            assert timestep == 8062
            return self.reward_max

        if len(self.triggered_alarms) == 0:
            # no alarm have been sent, so it's the minimum
            return self.reward_min

        if len(disconnected_lines_at_game_over) == 0:
            # game over is not caused by the tripping of a powerline
            return self.reward_min

        assert len(disconnected_lines_before_game_over) <= self.window_disconnection
        combined_disconnected_lines_before_game_over = np.concatenate(disconnected_lines_before_game_over).astype(int)
        if len(combined_disconnected_lines_before_game_over) > 0:
            disconnect_lines_to_consider = combined_disconnected_lines_before_game_over
        else:
            disconnect_lines_to_consider = disconnected_lines_at_game_over

        # so now i can consider the alarms.
        best_score = self.reward_min
        for alarm in self.triggered_alarms:
            score = self._points_for_alarm(
                *alarm, step_game_over=step_game_over, disc_lines=disconnect_lines_to_consider
            )
            if score > best_score:
                best_score = score
        return best_score
