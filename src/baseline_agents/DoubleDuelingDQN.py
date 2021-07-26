import grid2op
from l2rpn_baselines.DoubleDuelingDQN import train
from l2rpn_baselines.DoubleDuelingDQN import evaluate
from l2rpn_baselines.PandapowerOPFAgent import evaluate as evaluatePanda
from grid2op.Reward import RedispReward
from lightsim2grid.LightSimBackend import LightSimBackend
from l2rpn_baselines.DoubleDuelingDQN.DoubleDuelingDQN import (
    DoubleDuelingDQN as D3QNAgent,
)


def make_D3QN_agent(env):
    load_path = "/home/horacio/git/competition/trained-models/DoubleDuelingDQN/DoubleDuelingDQN.h5"
    agent = D3QNAgent(env.observation_space, env.action_space, is_training=False)
    agent.load(load_path)
    return agent


# BACKEND = LightSimBackend
# env = grid2op.make(
#    "l2rpn_icaps_2021_small", backend=BACKEND(), reward_class=RedispReward
# )
# res = train(
#    env, save_path="/home/horacio/git/competition/DoubleDuelingDQN", iterations=100
# )
# res = evaluate(
#    env,
#    load_path="/home/horacio/git/competition/DoubleDuelingDQN/DoubleDuelingDQN.h5",
#    nb_episode=10,
# )


# def evaluate(env,
#              load_path=None,
#              logs_path=DEFAULT_LOGS_DIR,
#              nb_episode=DEFAULT_NB_EPISODE,
#              nb_process=DEFAULT_NB_PROCESS,
#              max_steps=DEFAULT_MAX_STEPS,
#              num_frames=DEFAULT_NUM_FRAMES,
#              verbose=DEFAULT_VERBOSE,
#              save_gif=False):

#     # Set config
#     D3QNConfig.N_FRAMES = num_frames
#     D3QNConfig.VERBOSE = verbose

#     # Limit gpu usage
#     physical_devices = tf.config.list_physical_devices('GPU')
#     if len(physical_devices):
#         tf.config.experimental.set_memory_growth(physical_devices[0], True)

#     runner_params = env.get_params_for_runner()
#     runner_params["verbose"] = verbose

#     # Create agent
#     agent = D3QNAgent(env.observation_space,
#                       env.action_space,
#                       is_training=False)

#     # Load weights from file
#     agent.load(load_path)

#     # Build runner
#     runner = Runner(**runner_params,
#                     agentClass=None,
#                     agentInstance=agent)

#     # Print model summary
#     if verbose:
#         stringlist = []
#         agent.Qmain.model.summary(print_fn=lambda x: stringlist.append(x))
#         short_model_summary = "\n".join(stringlist)
#         print(short_model_summary)

#     # Run
#     os.makedirs(logs_path, exist_ok=True)
#     res = runner.run(path_save=logs_path,
#                      nb_episode=nb_episode,
#                      nb_process=nb_process,
#                      max_iter=max_steps,
#                      pbar=verbose)

#     # Print summary
#     if verbose:
#         print("Evaluation summary:")
#         for _, chron_name, cum_reward, nb_time_step, max_ts in res:
#             msg_tmp = "chronics at: {}".format(chron_name)
#             msg_tmp += "\ttotal reward: {:.6f}".format(cum_reward)
#             msg_tmp += "\ttime steps: {:.0f}/{:.0f}".format(nb_time_step,
#                                                             max_ts)
#             print(msg_tmp)

#     if save_gif:
#         save_log_gif(logs_path, res)

#     return res
