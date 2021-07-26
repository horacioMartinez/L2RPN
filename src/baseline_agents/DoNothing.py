# Debugear objeto:
# from pprint import pprint
# pprint(vars(gridPlot))
# pprint(dir(gridPlot))

# from .my_agent import make_agent

import numpy as np
import grid2op
from grid2op.Runner import Runner
from grid2op.Parameters import Parameters
from grid2op.Agent.BaseAgent import BaseAgent
from grid2op.Reward import RedispReward
from grid2op.PlotGrid import PlotMatplot
from lightsim2grid.LightSimBackend import LightSimBackend

# Split training de evaluation data con train_val_split_random. (https://grid2op.readthedocs.io/en/latest/environment.html#grid2op.Environment.Environment.train_val_split_random)
from grid2op.utils import ScoreICAPS2021


class DoNothing(BaseAgent):
    """
    Do nothing agent of grid2op, as a lowerbond baseline for l2rpn competition.
    """

    def __init__(self, action_space, observation_space, name, **kwargs):
        super().__init__(action_space)
        self.name = name

    def act(self, observation, reward, done):
        # Just return an empty action aka. "do nothing"
        return self.action_space({})

    def reset(self, observation):
        # No internal states to reset
        pass

    def load(self, path):
        # Nothing to load
        pass

    def save(self, path):
        # Nothing to save
        pass


class DoNothing_Attention_Agent(BaseAgent):
    """
    This is the most basic BaseAgent. It is purely passive, and does absolutely nothing.
    As opposed to most reinforcement learning environments, in grid2op, doing nothing is often
    the best solution.
    """

    def __init__(self, action_space, alarms_lines_area, alarms_area_names):
        BaseAgent.__init__(self, action_space)
        self.alarms_lines_area = alarms_lines_area
        self.alarms_area_names = alarms_area_names

    def act(self, observation, reward, done=False):
        """
        As better explained in the document of :func:`grid2op.BaseAction.update` or
        :func:`grid2op.BaseAction.ActionSpace.__call__`.
        The preferred way to make an object of type action is to call :func:`grid2op.BaseAction.ActionSpace.__call__`
        with the dictionary representing the action. In this case, the action is "do nothing" and it is represented by
        the empty dictionary.
        Parameters
        ----------
        observation: :class:`grid2op.Observation.Observation`
            The current observation of the :class:`grid2op.Environment.Environment`
        reward: ``float``
            The current reward. This is the reward obtained by the previous action
        done: ``bool``
            Whether the episode has ended or not. Used to maintain gym compatibility
        Returns
        -------
        res: :class:`grid2op.Action.Action`
            The action chosen by the bot / controller / agent.
        """
        res = self.action_space({})
        if np.max(observation.rho) >= 1:
            zones_alert = self.get_region_alert(observation)
            print(zones_alert)
            res = self.action_space({"raise_alarm": zones_alert})
            print(res)
        # print(res)
        return res

    def get_region_alert(self, observation):
        # extract the zones they belong too
        zones_these_lines = set()
        zone_for_each_lines = self.alarms_lines_area

        lines_overloaded = np.where(observation.rho >= 1)[0].tolist()  # obs.rho>0.6
        # print(lines_overloaded)
        for line_id in lines_overloaded:
            line_name = observation.name_line[line_id]
            for zone_name in zone_for_each_lines[line_name]:
                zones_these_lines.add(zone_name)

        zones_these_lines = list(zones_these_lines)
        zones_ids_these_lines = [
            self.alarms_area_names.index(zone) for zone in zones_these_lines
        ]
        return zones_ids_these_lines


def make_DoNothing_agent(env):
    agent = DoNothing(env.action_space, env.observation_space, "nombreAleatorio")
    return agent


def make_DoNothingAttention_agent(env):
    agent = DoNothing_Attention_Agent(
        env.action_space, env.alarms_lines_area, env.alarms_area_names
    )
    return agent


# BACKEND = LightSimBackend
# print(grid2op.__version__)
# env = grid2op.make(
#     "l2rpn_icaps_2021_small", backend=BACKEND(), reward_class=RedispReward
# )

# obs = env.reset()
# plot_helper = PlotMatplot(env.observation_space, width=1920, height=1080, line_id=False)
# gridPlot = plot_helper.plot_layout()

# print("Saving grid plot to grid.png")
# gridPlot.savefig("grid.png")


# agent = DoNothing_Attention_Agent(env.action_space, env.alarms_lines_area)
# agent = DoNothing(env.action_space, env.alarms_lines_area, "doNothingAgentName")

# runner = Runner(**env.get_params_for_runner(), agentClass=None, agentInstance=agent)

# id_chonic = 1
# res_episode = runner.run_one_episode(
#     detailed_output=True,
#     indx=id_chonic,
#     env_seed=1572415299,
#     path_save="res_alert",
#     agent_seed=1708891582,
# )

# name_chron, cum_reward, nb_timestep, episode_data = res_episode

# print("Number of timesteps before end of episode: " + str(nb_timestep))
# print(
#     "time_since_last_alarm is: "
#     + str(episode_data.observations[nb_timestep - 2].time_since_last_alarm[0] + 2)
# )
# print("Attention reward is: " + str(cum_reward))
