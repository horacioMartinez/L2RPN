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

#################################################### from  v6_top500_unitary_actions.npz -------->
action14 = env.action_space()
action14.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.8, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action14)
# ---- END OF ACTION ---
action17 = env.action_space()
action17.redispatch = np.array([0, 0, 0, 10.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action17)
# ---- END OF ACTION ---
action24 = env.action_space()
action24.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action24)
# ---- END OF ACTION ---
action29 = env.action_space()
action29.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2.8, 0, 0])
actions.append(action29)
# ---- END OF ACTION ---
action32 = env.action_space()
action32.redispatch = np.array([0, 0, 0, -10.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action32)
# ---- END OF ACTION ---
action34 = env.action_space()
action34.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8.5, 0])
actions.append(action34)
# ---- END OF ACTION ---
action66 = env.action_space()
action66.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -8.5, 0])
actions.append(action66)
# ---- END OF ACTION ---
action77 = env.action_space()
action77.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action77)
# ---- END OF ACTION ---
action80 = env.action_space()
action80.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9.9])
actions.append(action80)
# ---- END OF ACTION ---
action91 = env.action_space()
action91.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4.3, 0, 0, 0, 0, 0])
actions.append(action91)
# ---- END OF ACTION ---
action112 = env.action_space()
action112.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6.375, 0])
actions.append(action112)
# ---- END OF ACTION ---
action157 = env.action_space()
action157.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2.8, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action157)
# ---- END OF ACTION ---
action167 = env.action_space()
action167.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.25, 0])
actions.append(action167)
# ---- END OF ACTION ---
action169 = env.action_space()
action169.redispatch = np.array([0, 0, 0, 7.7999997, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action169)
# ---- END OF ACTION ---
action177 = env.action_space()
action177.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.3, 0, 0, 0, 0, 0])
actions.append(action177)
# ---- END OF ACTION ---
action219 = env.action_space()
action219.redispatch = np.array([0, 0, 0, 5.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action219)
# ---- END OF ACTION ---
action224 = env.action_space()
action224.redispatch = np.array([0, 0, 0, -7.7999997, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action224)
# ---- END OF ACTION ---
action233 = env.action_space()
action233.redispatch = np.array([0, 0, 0, -5.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action233)
# ---- END OF ACTION ---
action276 = env.action_space()
action276.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -7.4249997])
actions.append(action276)
# ---- END OF ACTION ---
action278 = env.action_space()
action278.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action278)
# ---- END OF ACTION ---
action303 = env.action_space()
action303.redispatch = np.array([0.35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action303)
# ---- END OF ACTION ---
action307 = env.action_space()
action307.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -6.375, 0])
actions.append(action307)
# ---- END OF ACTION ---
action383 = env.action_space()
action383.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.95])
actions.append(action383)
# ---- END OF ACTION ---
action389 = env.action_space()
action389.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.4, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action389)
# ---- END OF ACTION ---
action397 = env.action_space()
action397.redispatch = np.array([0, 0, 0, -2.6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action397)
# ---- END OF ACTION ---
action399 = env.action_space()
action399.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2.1, 0, 0])
actions.append(action399)
# ---- END OF ACTION ---
action404 = env.action_space()
action404.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7.4249997])
actions.append(action404)
# ---- END OF ACTION ---
action409 = env.action_space()
action409.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.2250001, 0, 0, 0, 0, 0])
actions.append(action409)
# ---- END OF ACTION ---
action410 = env.action_space()
action410.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.125, 0])
actions.append(action410)
# ---- END OF ACTION ---
action411 = env.action_space()
action411.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4.95])
actions.append(action411)
# ---- END OF ACTION ---
action422 = env.action_space()
action422.redispatch = np.array([-1.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action422)
# ---- END OF ACTION ---
action426 = env.action_space()
action426.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action426)
# ---- END OF ACTION ---
action454 = env.action_space()
action454.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.1, 0, 0, 0, 0, 0, 0, 0, 0])
actions.append(action454)
# ---- END OF ACTION ---
action491 = env.action_space()
action491.redispatch = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.15, 0, 0, 0, 0, 0])
actions.append(action491)
# ---- END OF ACTION ---


# <------------------ from  v6_top500_unitary_actions.npz ####################################################

res = []
for i in range(0, len(actions)):
    vect = actions[i].to_vect()
    res.append(vect)
res = np.asarray(res)

print(res.shape)

np.save("v6_top500_unitary_actions_only_redispatch", res)

print("OK")
