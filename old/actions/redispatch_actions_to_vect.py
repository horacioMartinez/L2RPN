import sys
import numpy as np
import time
import grid2op
from lightsim2grid.LightSimBackend import LightSimBackend


# env = grid2op.make(track, backend=BACKEND(), reward_class=RedispReward)
start_time = time.time()
BACKEND = LightSimBackend

# track = "l2rpn_icaps_2021_small"
track = "l2rpn_neurips_2020_track1_small"

env = grid2op.make(track, backend=BACKEND())

actions = []

#################################################### from  redispatch_actions.npz -------->
action0 = env.action_space()
action0.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.8, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action0)
# ---- END OF ACTION ---
action1 = env.action_space()
action1.redispatch = np.array([0, 0, 0, 10.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action1)
# ---- END OF ACTION ---
action2 = env.action_space()
action2.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action2)
# ---- END OF ACTION ---
action3 = env.action_space()
action3.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2.8, 0, 0])
actions.append(action3)
# ---- END OF ACTION ---
action4 = env.action_space()
action4.redispatch = np.array([0, 0, 0, -10.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action4)
# ---- END OF ACTION ---
action5 = env.action_space()
action5.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8.5, 0])
actions.append(action5)
# ---- END OF ACTION ---
action6 = env.action_space()
action6.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8.5, 0])
actions.append(action6)
# ---- END OF ACTION ---
action7 = env.action_space()
action7.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action7)
# ---- END OF ACTION ---
action8 = env.action_space()
action8.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9.9])
actions.append(action8)
# ---- END OF ACTION ---
action9 = env.action_space()
action9.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4.3, 0, 0, 0, 0, 0])
actions.append(action9)
# ---- END OF ACTION ---
action10 = env.action_space()
action10.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6.375, 0])
actions.append(action10)
# ---- END OF ACTION ---
action11 = env.action_space()
action11.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2.8, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action11)
# ---- END OF ACTION ---
action12 = env.action_space()
action12.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.25, 0])
actions.append(action12)
# ---- END OF ACTION ---
action13 = env.action_space()
action13.redispatch = np.array([0, 0, 0, 7.7999997, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action13)
# ---- END OF ACTION ---
action14 = env.action_space()
action14.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.3, 0, 0, 0, 0, 0])
actions.append(action14)
# ---- END OF ACTION ---
action15 = env.action_space()
action15.redispatch = np.array([0, 0, 0, 5.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action15)
# ---- END OF ACTION ---
action16 = env.action_space()
action16.redispatch = np.array([0, 0, 0, -7.7999997, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action16)
# ---- END OF ACTION ---
action17 = env.action_space()
action17.redispatch = np.array([0, 0, 0, -5.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action17)
# ---- END OF ACTION ---
action18 = env.action_space()
action18.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -7.4249997])
actions.append(action18)
# ---- END OF ACTION ---
action19 = env.action_space()
action19.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action19)
# ---- END OF ACTION ---
action20 = env.action_space()
action20.redispatch = np.array([0.35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action20)
# ---- END OF ACTION ---
action21 = env.action_space()
action21.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -6.375, 0])
actions.append(action21)
# ---- END OF ACTION ---
action22 = env.action_space()
action22.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.95])
actions.append(action22)
# ---- END OF ACTION ---
action23 = env.action_space()
action23.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.4, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action23)
# ---- END OF ACTION ---
action24 = env.action_space()
action24.redispatch = np.array([0, 0, 0, -2.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action24)
# ---- END OF ACTION ---


# <------------------ from  redispatch_actions.npz ####################################################

res = []
for i in range(0, len(actions)):
    vect = actions[i].to_vect()
    res.append(vect)
res = np.asarray(res)

print(res.shape)

np.save("redispatch_actions", res)

print("OK")
