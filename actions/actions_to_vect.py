import sys
import numpy as np
import time
import grid2op
from grid2op.utils import ScoreICAPS2021
from lightsim2grid.LightSimBackend import LightSimBackend


# env = grid2op.make(track, backend=BACKEND(), reward_class=RedispReward)
start_time = time.time()
BACKEND = LightSimBackend

scoring_function = ScoreICAPS2021
track = "l2rpn_icaps_2021_small"
env = grid2op.make(track, backend=BACKEND())

actions = []
action0 = env.action_space()
action0.gen_change_bus = [16]
action0.line_ex_change_bus = [42]
action0.line_ex_change_bus = [57]
actions.append(action0)
# ---- END OF ACTION ---
action1 = env.action_space()
action1.line_ex_change_bus = [42]
action1.line_ex_change_bus = [57]
actions.append(action1)
# ---- END OF ACTION ---
action2 = env.action_space()
action2.line_ex_change_bus = [57]
actions.append(action2)
# ---- END OF ACTION ---
action3 = env.action_space()
action3.gen_change_bus = [0]
action3.load_change_bus = [2]
action3.line_or_change_bus = [12]
actions.append(action3)
# ---- END OF ACTION ---
action4 = env.action_space()
action4.gen_change_bus = [16]
action4.line_ex_change_bus = [57]
actions.append(action4)
# ---- END OF ACTION ---
action5 = env.action_space()
action5.gen_change_bus = [11]
action5.gen_change_bus = [12]
action5.gen_change_bus = [13]
action5.load_change_bus = [24]
action5.line_or_change_bus = [34]
action5.line_or_change_bus = [37]
action5.line_or_change_bus = [38]
actions.append(action5)
# ---- END OF ACTION ---
action6 = env.action_space()
action6.line_or_change_bus = [34]
action6.line_or_change_bus = [38]
actions.append(action6)
# ---- END OF ACTION ---
action7 = env.action_space()
action7.line_or_change_bus = [34]
action7.line_or_change_bus = [37]
actions.append(action7)
# ---- END OF ACTION ---
action8 = env.action_space()
action8.gen_change_bus = [12]
action8.load_change_bus = [24]
action8.line_or_change_bus = [34]
action8.line_or_change_bus = [37]
action8.line_or_change_bus = [38]
actions.append(action8)
# ---- END OF ACTION ---
action9 = env.action_space()
action9.gen_change_bus = [5]
action9.gen_change_bus = [6]
action9.gen_change_bus = [7]
action9.gen_change_bus = [8]
action9.line_ex_change_bus = [18]
action9.line_ex_change_bus = [19]
action9.line_or_change_bus = [27]
action9.line_or_change_bus = [28]
action9.line_or_change_bus = [54]
actions.append(action9)
# ---- END OF ACTION ---
action10 = env.action_space()
action10.line_or_change_bus = [34]
action10.line_or_change_bus = [37]
action10.line_or_change_bus = [38]
actions.append(action10)
# ---- END OF ACTION ---
action11 = env.action_space()
action11.gen_change_bus = [12]
action11.line_or_change_bus = [32]
action11.line_or_change_bus = [34]
actions.append(action11)
# ---- END OF ACTION ---
action12 = env.action_space()
action12.line_ex_change_bus = [42]
action12.line_or_change_bus = [44]
action12.line_ex_change_bus = [57]
actions.append(action12)
# ---- END OF ACTION ---
action13 = env.action_space()
action13.load_change_bus = [17]
action13.line_ex_change_bus = [20]
action13.line_or_change_bus = [49]
actions.append(action13)
# ---- END OF ACTION ---
action14 = env.action_space()
action14.gen_change_bus = [12]
action14.line_or_change_bus = [34]
action14.line_or_change_bus = [37]
actions.append(action14)
# ---- END OF ACTION ---
action15 = env.action_space()
action15.line_ex_change_bus = [37]
action15.line_ex_change_bus = [39]
action15.line_or_change_bus = [41]
actions.append(action15)
# ---- END OF ACTION ---
action16 = env.action_space()
action16.gen_change_bus = [14]
action16.load_change_bus = [27]
action16.line_ex_change_bus = [37]
action16.line_ex_change_bus = [38]
action16.line_or_change_bus = [40]
actions.append(action16)
# ---- END OF ACTION ---
action17 = env.action_space()
action17.line_ex_change_bus = [20]
action17.line_or_change_bus = [54]
actions.append(action17)
# ---- END OF ACTION ---
action18 = env.action_space()
action18.gen_change_bus = [11]
action18.gen_change_bus = [12]
action18.load_change_bus = [24]
action18.line_or_change_bus = [34]
action18.line_or_change_bus = [37]
action18.line_or_change_bus = [38]
actions.append(action18)
# ---- END OF ACTION ---
action19 = env.action_space()
action19.gen_change_bus = [5]
action19.gen_change_bus = [6]
action19.gen_change_bus = [7]
action19.gen_change_bus = [8]
action19.line_or_change_bus = [22]
action19.line_or_change_bus = [23]
action19.line_or_change_bus = [27]
action19.line_or_change_bus = [28]
action19.line_or_change_bus = [48]
action19.line_or_change_bus = [49]
action19.line_or_change_bus = [54]
actions.append(action19)
# ---- END OF ACTION ---
action20 = env.action_space()
action20.load_change_bus = [17]
action20.line_ex_change_bus = [19]
action20.line_ex_change_bus = [20]
action20.line_or_change_bus = [27]
action20.line_or_change_bus = [54]
actions.append(action20)
# ---- END OF ACTION ---
action21 = env.action_space()
action21.line_or_change_bus = [32]
action21.line_or_change_bus = [34]
action21.line_or_change_bus = [38]
actions.append(action21)
# ---- END OF ACTION ---
action22 = env.action_space()
action22.load_change_bus = [17]
action22.line_ex_change_bus = [18]
action22.line_ex_change_bus = [19]
action22.line_ex_change_bus = [20]
action22.line_or_change_bus = [27]
actions.append(action22)
# ---- END OF ACTION ---
action23 = env.action_space()
action23.gen_change_bus = [11]
action23.load_change_bus = [24]
action23.line_or_change_bus = [34]
action23.line_or_change_bus = [37]
action23.line_or_change_bus = [38]
actions.append(action23)
# ---- END OF ACTION ---
action24 = env.action_space()
action24.load_change_bus = [17]
action24.line_ex_change_bus = [19]
action24.line_ex_change_bus = [20]
action24.line_or_change_bus = [28]
action24.line_or_change_bus = [54]
actions.append(action24)
# ---- END OF ACTION ---
action25 = env.action_space()
action25.load_change_bus = [22]
action25.line_ex_change_bus = [27]
action25.line_ex_change_bus = [28]
actions.append(action25)
# ---- END OF ACTION ---
action26 = env.action_space()
action26.gen_change_bus = [13]
action26.load_change_bus = [24]
action26.line_or_change_bus = [34]
action26.line_or_change_bus = [37]
action26.line_or_change_bus = [38]
actions.append(action26)
# ---- END OF ACTION ---
action27 = env.action_space()
action27.line_ex_change_bus = [2]
action27.line_ex_change_bus = [55]
actions.append(action27)
# ---- END OF ACTION ---
action28 = env.action_space()
action28.line_ex_change_bus = [38]
action28.line_ex_change_bus = [39]
action28.line_or_change_bus = [41]
actions.append(action28)
# ---- END OF ACTION ---
action29 = env.action_space()
action29.line_or_change_bus = [32]
action29.line_or_change_bus = [34]
action29.line_or_change_bus = [37]
actions.append(action29)
# ---- END OF ACTION ---
action30 = env.action_space()
action30.load_change_bus = [17]
action30.line_ex_change_bus = [18]
action30.line_ex_change_bus = [19]
action30.line_ex_change_bus = [20]
action30.line_or_change_bus = [28]
actions.append(action30)
# ---- END OF ACTION ---
action31 = env.action_space()
action31.gen_change_bus = [7]
action31.load_change_bus = [17]
action31.line_or_change_bus = [22]
action31.line_or_change_bus = [23]
action31.line_or_change_bus = [48]
action31.line_or_change_bus = [49]
actions.append(action31)
# ---- END OF ACTION ---
action32 = env.action_space()
action32.gen_change_bus = [5]
action32.gen_change_bus = [6]
action32.gen_change_bus = [7]
action32.gen_change_bus = [8]
action32.line_ex_change_bus = [18]
action32.line_ex_change_bus = [19]
action32.line_or_change_bus = [27]
action32.line_or_change_bus = [28]
action32.line_or_change_bus = [49]
action32.line_or_change_bus = [54]
actions.append(action32)
# ---- END OF ACTION ---
action33 = env.action_space()
action33.gen_change_bus = [12]
action33.line_or_change_bus = [34]
actions.append(action33)
# ---- END OF ACTION ---
action34 = env.action_space()
action34.gen_change_bus = [11]
action34.line_or_change_bus = [34]
actions.append(action34)
# ---- END OF ACTION ---
action35 = env.action_space()
action35.gen_change_bus = [5]
action35.gen_change_bus = [6]
action35.gen_change_bus = [7]
action35.gen_change_bus = [8]
action35.line_ex_change_bus = [19]
action35.line_or_change_bus = [22]
action35.line_or_change_bus = [23]
action35.line_or_change_bus = [27]
action35.line_or_change_bus = [48]
action35.line_or_change_bus = [49]
actions.append(action35)
# ---- END OF ACTION ---
action36 = env.action_space()
action36.line_or_change_bus = [32]
action36.line_or_change_bus = [34]
action36.line_or_change_bus = [37]
action36.line_or_change_bus = [38]
actions.append(action36)
# ---- END OF ACTION ---
action37 = env.action_space()
action37.line_ex_change_bus = [20]
action37.line_or_change_bus = [28]
actions.append(action37)
# ---- END OF ACTION ---
action38 = env.action_space()
action38.gen_change_bus = [11]
action38.gen_change_bus = [12]
action38.gen_change_bus = [13]
action38.line_ex_change_bus = [31]
action38.line_or_change_bus = [32]
actions.append(action38)
# ---- END OF ACTION ---
action39 = env.action_space()
action39.load_change_bus = [13]
action39.line_or_change_bus = [14]
action39.line_or_change_bus = [20]
actions.append(action39)
# ---- END OF ACTION ---
action40 = env.action_space()
action40.load_change_bus = [22]
action40.line_or_change_bus = [29]
action40.line_or_change_bus = [30]
actions.append(action40)
# ---- END OF ACTION ---
action41 = env.action_space()
action41.gen_change_bus = [12]
action41.line_or_change_bus = [34]
action41.line_or_change_bus = [38]
actions.append(action41)
# ---- END OF ACTION ---
action42 = env.action_space()
action42.load_change_bus = [17]
action42.line_ex_change_bus = [20]
action42.line_or_change_bus = [27]
action42.line_or_change_bus = [28]
action42.line_or_change_bus = [54]
actions.append(action42)
# ---- END OF ACTION ---
action43 = env.action_space()
action43.line_or_change_bus = [6]
action43.line_ex_change_bus = [55]
actions.append(action43)
# ---- END OF ACTION ---
action44 = env.action_space()
action44.gen_change_bus = [11]
action44.gen_change_bus = [12]
action44.line_or_change_bus = [34]
actions.append(action44)
# ---- END OF ACTION ---
action45 = env.action_space()
action45.gen_change_bus = [5]
action45.gen_change_bus = [6]
action45.gen_change_bus = [7]
action45.gen_change_bus = [8]
action45.line_ex_change_bus = [19]
action45.line_or_change_bus = [22]
action45.line_or_change_bus = [23]
action45.line_or_change_bus = [27]
action45.line_or_change_bus = [28]
action45.line_or_change_bus = [48]
action45.line_or_change_bus = [49]
actions.append(action45)
# ---- END OF ACTION ---
action46 = env.action_space()
action46.gen_change_bus = [12]
action46.line_ex_change_bus = [31]
action46.line_or_change_bus = [32]
action46.line_or_change_bus = [34]
action46.line_or_change_bus = [37]
action46.line_or_change_bus = [38]
actions.append(action46)
# ---- END OF ACTION ---
action47 = env.action_space()
action47.line_ex_change_bus = [31]
action47.line_or_change_bus = [32]
action47.line_or_change_bus = [34]
action47.line_or_change_bus = [37]
action47.line_or_change_bus = [38]
actions.append(action47)
# ---- END OF ACTION ---
action48 = env.action_space()
action48.line_ex_change_bus = [55]
actions.append(action48)
# ---- END OF ACTION ---
action49 = env.action_space()
action49.line_ex_change_bus = [31]
action49.line_or_change_bus = [34]
action49.line_or_change_bus = [37]
action49.line_or_change_bus = [38]
actions.append(action49)
# ---- END OF ACTION ---
action50 = env.action_space()
action50.gen_change_bus = [5]
action50.gen_change_bus = [8]
action50.line_ex_change_bus = [19]
action50.line_or_change_bus = [28]
action50.line_or_change_bus = [54]
actions.append(action50)
# ---- END OF ACTION ---
action51 = env.action_space()
action51.line_ex_change_bus = [31]
action51.line_or_change_bus = [32]
action51.line_or_change_bus = [37]
action51.line_or_change_bus = [38]
actions.append(action51)
# ---- END OF ACTION ---
action52 = env.action_space()
action52.gen_change_bus = [5]
action52.gen_change_bus = [6]
action52.gen_change_bus = [7]
action52.gen_change_bus = [8]
action52.line_ex_change_bus = [21]
action52.line_or_change_bus = [22]
action52.line_or_change_bus = [23]
action52.line_or_change_bus = [27]
action52.line_or_change_bus = [28]
action52.line_or_change_bus = [48]
action52.line_or_change_bus = [49]
action52.line_or_change_bus = [54]
actions.append(action52)
# ---- END OF ACTION ---
action53 = env.action_space()
action53.gen_change_bus = [14]
action53.load_change_bus = [27]
action53.line_or_change_bus = [40]
action53.line_or_change_bus = [41]
actions.append(action53)
# ---- END OF ACTION ---
action54 = env.action_space()
action54.line_ex_change_bus = [19]
action54.line_or_change_bus = [28]
action54.line_or_change_bus = [54]
actions.append(action54)
# ---- END OF ACTION ---
action55 = env.action_space()
action55.gen_change_bus = [13]
action55.load_change_bus = [24]
action55.line_or_change_bus = [37]
action55.line_or_change_bus = [38]
actions.append(action55)
# ---- END OF ACTION ---
action56 = env.action_space()
action56.line_or_change_bus = [32]
action56.line_or_change_bus = [34]
actions.append(action56)
# ---- END OF ACTION ---
action57 = env.action_space()
action57.gen_change_bus = [5]
action57.gen_change_bus = [6]
action57.gen_change_bus = [7]
action57.gen_change_bus = [8]
action57.line_ex_change_bus = [19]
action57.line_or_change_bus = [22]
action57.line_or_change_bus = [23]
action57.line_or_change_bus = [28]
action57.line_or_change_bus = [48]
action57.line_or_change_bus = [49]
action57.line_or_change_bus = [54]
actions.append(action57)
# ---- END OF ACTION ---
action58 = env.action_space()
action58.load_change_bus = [22]
action58.line_or_change_bus = [29]
action58.line_or_change_bus = [30]
action58.line_or_change_bus = [36]
actions.append(action58)
# ---- END OF ACTION ---
action59 = env.action_space()
action59.gen_change_bus = [5]
action59.gen_change_bus = [6]
action59.gen_change_bus = [7]
action59.gen_change_bus = [8]
action59.line_or_change_bus = [22]
action59.line_or_change_bus = [23]
action59.line_or_change_bus = [27]
action59.line_or_change_bus = [28]
action59.line_or_change_bus = [48]
action59.line_or_change_bus = [49]
actions.append(action59)
# ---- END OF ACTION ---
action60 = env.action_space()
action60.load_change_bus = [17]
action60.line_ex_change_bus = [20]
action60.line_or_change_bus = [49]
action60.line_or_change_bus = [54]
actions.append(action60)
# ---- END OF ACTION ---
action61 = env.action_space()
action61.gen_change_bus = [5]
action61.gen_change_bus = [6]
action61.gen_change_bus = [7]
action61.gen_change_bus = [8]
action61.line_ex_change_bus = [19]
action61.line_or_change_bus = [22]
action61.line_or_change_bus = [23]
action61.line_or_change_bus = [27]
action61.line_or_change_bus = [48]
action61.line_or_change_bus = [49]
action61.line_or_change_bus = [54]
actions.append(action61)
# ---- END OF ACTION ---
action62 = env.action_space()
action62.gen_change_bus = [2]
action62.gen_change_bus = [3]
action62.line_or_change_bus = [18]
action62.line_or_change_bus = [19]
actions.append(action62)
# ---- END OF ACTION ---
action63 = env.action_space()
action63.gen_change_bus = [5]
action63.gen_change_bus = [8]
action63.line_ex_change_bus = [18]
action63.line_ex_change_bus = [19]
action63.line_or_change_bus = [27]
action63.line_or_change_bus = [28]
action63.line_or_change_bus = [54]
actions.append(action63)
# ---- END OF ACTION ---
action64 = env.action_space()
action64.load_change_bus = [6]
action64.line_or_change_bus = [55]
actions.append(action64)
# ---- END OF ACTION ---
action65 = env.action_space()
action65.gen_change_bus = [19]
action65.load_change_bus = [30]
action65.line_or_change_bus = [58]
actions.append(action65)
# ---- END OF ACTION ---
action66 = env.action_space()
action66.gen_change_bus = [1]
action66.line_or_change_bus = [8]
action66.line_or_change_bus = [9]
actions.append(action66)
# ---- END OF ACTION ---
action67 = env.action_space()
action67.gen_change_bus = [20]
action67.load_change_bus = [31]
action67.line_ex_change_bus = [50]
action67.line_or_change_bus = [52]
actions.append(action67)
# ---- END OF ACTION ---
action68 = env.action_space()
action68.gen_change_bus = [2]
action68.gen_change_bus = [3]
action68.line_or_change_bus = [19]
actions.append(action68)
# ---- END OF ACTION ---
action69 = env.action_space()
action69.line_or_change_bus = [5]
action69.line_or_change_bus = [6]
actions.append(action69)
# ---- END OF ACTION ---
action70 = env.action_space()
action70.gen_change_bus = [5]
action70.gen_change_bus = [7]
action70.gen_change_bus = [8]
action70.line_ex_change_bus = [18]
action70.line_ex_change_bus = [19]
action70.line_or_change_bus = [27]
action70.line_or_change_bus = [28]
action70.line_or_change_bus = [54]
actions.append(action70)
# ---- END OF ACTION ---
action71 = env.action_space()
action71.load_change_bus = [20]
action71.line_or_change_bus = [25]
actions.append(action71)
# ---- END OF ACTION ---
action72 = env.action_space()
action72.gen_change_bus = [5]
action72.gen_change_bus = [6]
action72.gen_change_bus = [7]
action72.gen_change_bus = [8]
action72.line_ex_change_bus = [18]
action72.line_ex_change_bus = [19]
action72.line_or_change_bus = [27]
action72.line_or_change_bus = [28]
actions.append(action72)
# ---- END OF ACTION ---
action73 = env.action_space()
action73.line_or_change_bus = [41]
actions.append(action73)
# ---- END OF ACTION ---
action74 = env.action_space()
action74.gen_change_bus = [16]
action74.line_ex_change_bus = [42]
actions.append(action74)
# ---- END OF ACTION ---
action75 = env.action_space()
action75.gen_change_bus = [20]
action75.load_change_bus = [31]
action75.line_or_change_bus = [52]
actions.append(action75)
# ---- END OF ACTION ---
action76 = env.action_space()
action76.load_change_bus = [22]
action76.line_ex_change_bus = [28]
actions.append(action76)
# ---- END OF ACTION ---
action77 = env.action_space()
action77.gen_change_bus = [3]
action77.line_or_change_bus = [18]
action77.line_or_change_bus = [19]
actions.append(action77)
# ---- END OF ACTION ---
action78 = env.action_space()
action78.line_or_change_bus = [8]
action78.line_or_change_bus = [9]
actions.append(action78)
# ---- END OF ACTION ---
action79 = env.action_space()
action79.load_change_bus = [15]
action79.line_or_change_bus = [53]
actions.append(action79)
# ---- END OF ACTION ---
action80 = env.action_space()
action80.line_or_change_bus = [12]
actions.append(action80)
# ---- END OF ACTION ---
action81 = env.action_space()
action81.line_ex_change_bus = [2]
action81.line_or_change_bus = [5]
action81.line_or_change_bus = [6]
actions.append(action81)
# ---- END OF ACTION ---
action82 = env.action_space()
action82.load_change_bus = [13]
action82.line_or_change_bus = [14]
actions.append(action82)
# ---- END OF ACTION ---
action83 = env.action_space()
action83.gen_change_bus = [1]
action83.load_change_bus = [8]
action83.line_or_change_bus = [9]
actions.append(action83)
# ---- END OF ACTION ---
action84 = env.action_space()
action84.line_or_change_bus = [26]
actions.append(action84)
# ---- END OF ACTION ---
action85 = env.action_space()
action85.gen_change_bus = [14]
action85.load_change_bus = [27]
action85.line_ex_change_bus = [56]
actions.append(action85)
# ---- END OF ACTION ---
action86 = env.action_space()
action86.gen_change_bus = [20]
action86.load_change_bus = [31]
action86.line_ex_change_bus = [50]
actions.append(action86)
# ---- END OF ACTION ---
action87 = env.action_space()
action87.gen_change_bus = [9]
action87.load_change_bus = [22]
action87.line_ex_change_bus = [28]
actions.append(action87)
# ---- END OF ACTION ---
action88 = env.action_space()
action88.line_ex_change_bus = [42]
actions.append(action88)
# ---- END OF ACTION ---
action89 = env.action_space()
action89.gen_change_bus = [2]
action89.gen_change_bus = [3]
action89.load_change_bus = [10]
action89.line_or_change_bus = [18]
action89.line_or_change_bus = [19]
actions.append(action89)
# ---- END OF ACTION ---
action90 = env.action_space()
action90.gen_change_bus = [21]
action90.load_change_bus = [35]
action90.line_ex_change_bus = [54]
actions.append(action90)
# ---- END OF ACTION ---
action91 = env.action_space()
action91.load_change_bus = [19]
action91.line_or_change_bus = [35]
actions.append(action91)
# ---- END OF ACTION ---
action92 = env.action_space()
action92.load_change_bus = [2]
action92.line_or_change_bus = [12]
actions.append(action92)
# ---- END OF ACTION ---
action93 = env.action_space()
action93.line_ex_change_bus = [39]
actions.append(action93)
# ---- END OF ACTION ---
action94 = env.action_space()
action94.gen_change_bus = [3]
action94.line_or_change_bus = [19]
actions.append(action94)
# ---- END OF ACTION ---
action95 = env.action_space()
action95.line_or_change_bus = [1]
action95.load_change_bus = [4]
actions.append(action95)
# ---- END OF ACTION ---
action96 = env.action_space()
action96.gen_change_bus = [11]
action96.gen_change_bus = [12]
action96.gen_change_bus = [13]
action96.load_change_bus = [24]
action96.line_or_change_bus = [32]
action96.line_or_change_bus = [34]
actions.append(action96)
# ---- END OF ACTION ---
action97 = env.action_space()
action97.line_ex_change_bus = [2]
action97.line_or_change_bus = [5]
action97.line_ex_change_bus = [55]
actions.append(action97)
# ---- END OF ACTION ---
action98 = env.action_space()
action98.gen_change_bus = [3]
action98.line_ex_change_bus = [10]
action98.line_or_change_bus = [18]
action98.line_or_change_bus = [19]
actions.append(action98)
# ---- END OF ACTION ---
action99 = env.action_space()
action99.line_or_change_bus = [20]
actions.append(action99)
# ---- END OF ACTION ---
action100 = env.action_space()
action100.load_change_bus = [10]
action100.line_or_change_bus = [19]
actions.append(action100)
# ---- END OF ACTION ---
action101 = env.action_space()
action101.gen_change_bus = [7]
action101.load_change_bus = [17]
action101.line_ex_change_bus = [20]
action101.line_or_change_bus = [22]
action101.line_or_change_bus = [23]
action101.line_or_change_bus = [48]
action101.line_or_change_bus = [49]
actions.append(action101)
# ---- END OF ACTION ---
action102 = env.action_space()
action102.load_change_bus = [8]
action102.line_or_change_bus = [9]
actions.append(action102)
# ---- END OF ACTION ---
action103 = env.action_space()
action103.gen_change_bus = [0]
action103.load_change_bus = [3]
action103.line_or_change_bus = [4]
action103.line_or_change_bus = [12]
actions.append(action103)
# ---- END OF ACTION ---
action104 = env.action_space()
action104.line_ex_change_bus = [18]
action104.line_ex_change_bus = [19]
action104.line_or_change_bus = [27]
action104.line_or_change_bus = [28]
action104.line_or_change_bus = [54]
actions.append(action104)
# ---- END OF ACTION ---
action105 = env.action_space()
action105.gen_change_bus = [13]
action105.load_change_bus = [24]
action105.line_or_change_bus = [32]
action105.line_or_change_bus = [34]
actions.append(action105)
# ---- END OF ACTION ---
action106 = env.action_space()
action106.gen_change_bus = [8]
actions.append(action106)
# ---- END OF ACTION ---
action107 = env.action_space()
action107.gen_change_bus = [9]
action107.load_change_bus = [22]
action107.line_ex_change_bus = [27]
action107.line_ex_change_bus = [28]
action107.line_or_change_bus = [29]
action107.line_or_change_bus = [30]
action107.line_or_change_bus = [36]
actions.append(action107)
# ---- END OF ACTION ---
action108 = env.action_space()
action108.gen_change_bus = [19]
action108.load_change_bus = [30]
action108.line_ex_change_bus = [47]
action108.line_or_change_bus = [58]
actions.append(action108)
# ---- END OF ACTION ---
action109 = env.action_space()
action109.line_ex_change_bus = [37]
action109.line_ex_change_bus = [38]
action109.line_or_change_bus = [40]
action109.line_or_change_bus = [41]
actions.append(action109)
# ---- END OF ACTION ---
action110 = env.action_space()
action110.gen_change_bus = [3]
action110.load_change_bus = [10]
action110.line_or_change_bus = [18]
action110.line_or_change_bus = [19]
actions.append(action110)
# ---- END OF ACTION ---
action111 = env.action_space()
action111.gen_change_bus = [14]
action111.load_change_bus = [27]
action111.line_ex_change_bus = [37]
action111.line_ex_change_bus = [38]
action111.line_or_change_bus = [40]
action111.line_or_change_bus = [41]
actions.append(action111)
# ---- END OF ACTION ---
action112 = env.action_space()
action112.load_change_bus = [2]
actions.append(action112)
# ---- END OF ACTION ---
action113 = env.action_space()
action113.gen_change_bus = [0]
action113.line_or_change_bus = [12]
actions.append(action113)
# ---- END OF ACTION ---
action114 = env.action_space()
action114.gen_change_bus = [5]
action114.gen_change_bus = [8]
action114.line_ex_change_bus = [18]
action114.line_ex_change_bus = [19]
action114.line_or_change_bus = [27]
action114.line_or_change_bus = [28]
actions.append(action114)
# ---- END OF ACTION ---
action115 = env.action_space()
action115.gen_change_bus = [17]
action115.line_ex_change_bus = [44]
action115.line_or_change_bus = [51]
actions.append(action115)
# ---- END OF ACTION ---
action116 = env.action_space()
action116.gen_change_bus = [17]
action116.gen_change_bus = [18]
action116.load_change_bus = [29]
action116.line_or_change_bus = [51]
actions.append(action116)
# ---- END OF ACTION ---
action117 = env.action_space()
action117.gen_change_bus = [3]
actions.append(action117)
# ---- END OF ACTION ---
action118 = env.action_space()
action118.gen_change_bus = [7]
action118.load_change_bus = [17]
action118.line_or_change_bus = [22]
action118.line_or_change_bus = [23]
action118.line_or_change_bus = [28]
action118.line_or_change_bus = [48]
action118.line_or_change_bus = [49]
actions.append(action118)
# ---- END OF ACTION ---
action119 = env.action_space()
action119.gen_change_bus = [1]
actions.append(action119)
# ---- END OF ACTION ---
action120 = env.action_space()
action120.gen_change_bus = [20]
action120.line_ex_change_bus = [50]
action120.line_or_change_bus = [52]
actions.append(action120)
# ---- END OF ACTION ---
action121 = env.action_space()
action121.load_change_bus = [35]
action121.line_ex_change_bus = [54]
actions.append(action121)
# ---- END OF ACTION ---
action122 = env.action_space()
action122.line_or_change_bus = [32]
actions.append(action122)
# ---- END OF ACTION ---
action123 = env.action_space()
action123.gen_change_bus = [3]
action123.load_change_bus = [10]
action123.line_or_change_bus = [19]
actions.append(action123)
# ---- END OF ACTION ---
action124 = env.action_space()
action124.gen_change_bus = [11]
action124.gen_change_bus = [12]
action124.gen_change_bus = [13]
action124.load_change_bus = [24]
action124.line_or_change_bus = [37]
action124.line_or_change_bus = [38]
actions.append(action124)
# ---- END OF ACTION ---
action125 = env.action_space()
action125.gen_change_bus = [11]
action125.gen_change_bus = [12]
action125.line_or_change_bus = [37]
action125.line_or_change_bus = [38]
actions.append(action125)
# ---- END OF ACTION ---
action126 = env.action_space()
action126.line_or_change_bus = [47]
actions.append(action126)
# ---- END OF ACTION ---
action127 = env.action_space()
action127.line_ex_change_bus = [50]
action127.line_or_change_bus = [52]
actions.append(action127)
# ---- END OF ACTION ---
action128 = env.action_space()
action128.gen_change_bus = [13]
action128.line_or_change_bus = [37]
action128.line_or_change_bus = [38]
actions.append(action128)
# ---- END OF ACTION ---
action129 = env.action_space()
action129.gen_change_bus = [11]
action129.gen_change_bus = [12]
action129.line_or_change_bus = [32]
action129.line_or_change_bus = [34]
action129.line_or_change_bus = [37]
action129.line_or_change_bus = [38]
actions.append(action129)
# ---- END OF ACTION ---
action130 = env.action_space()
action130.line_ex_change_bus = [4]
action130.line_ex_change_bus = [55]
actions.append(action130)
# ---- END OF ACTION ---
action131 = env.action_space()
action131.line_or_change_bus = [34]
actions.append(action131)
# ---- END OF ACTION ---
action132 = env.action_space()
action132.line_or_change_bus = [19]
actions.append(action132)
# ---- END OF ACTION ---
action133 = env.action_space()
action133.gen_change_bus = [11]
action133.gen_change_bus = [12]
action133.line_or_change_bus = [37]
actions.append(action133)
# ---- END OF ACTION ---
action134 = env.action_space()
action134.load_change_bus = [10]
actions.append(action134)
# ---- END OF ACTION ---
action135 = env.action_space()
action135.gen_change_bus = [19]
action135.load_change_bus = [30]
action135.line_ex_change_bus = [47]
actions.append(action135)
# ---- END OF ACTION ---
action136 = env.action_space()
action136.line_or_change_bus = [5]
action136.line_ex_change_bus = [55]
actions.append(action136)
# ---- END OF ACTION ---
action137 = env.action_space()
action137.gen_change_bus = [16]
actions.append(action137)
# ---- END OF ACTION ---
action138 = env.action_space()
action138.line_ex_change_bus = [37]
action138.line_ex_change_bus = [38]
actions.append(action138)
# ---- END OF ACTION ---
action139 = env.action_space()
action139.gen_change_bus = [20]
action139.line_ex_change_bus = [50]
actions.append(action139)
# ---- END OF ACTION ---
action140 = env.action_space()
action140.gen_change_bus = [16]
action140.line_or_change_bus = [44]
actions.append(action140)
# ---- END OF ACTION ---
action141 = env.action_space()
action141.gen_change_bus = [14]
action141.load_change_bus = [27]
action141.line_ex_change_bus = [39]
action141.line_ex_change_bus = [56]
actions.append(action141)
# ---- END OF ACTION ---
action142 = env.action_space()
action142.gen_change_bus = [3]
action142.line_ex_change_bus = [10]
action142.line_or_change_bus = [19]
actions.append(action142)
# ---- END OF ACTION ---
action143 = env.action_space()
action143.gen_change_bus = [14]
action143.load_change_bus = [27]
action143.line_ex_change_bus = [37]
action143.line_ex_change_bus = [39]
action143.line_ex_change_bus = [56]
actions.append(action143)
# ---- END OF ACTION ---
action144 = env.action_space()
action144.line_ex_change_bus = [42]
action144.line_or_change_bus = [44]
actions.append(action144)
# ---- END OF ACTION ---
action145 = env.action_space()
action145.load_change_bus = [22]
action145.line_ex_change_bus = [27]
action145.line_ex_change_bus = [28]
action145.line_or_change_bus = [29]
action145.line_or_change_bus = [30]
action145.line_or_change_bus = [36]
actions.append(action145)
# ---- END OF ACTION ---
action146 = env.action_space()
action146.gen_change_bus = [14]
action146.line_ex_change_bus = [39]
action146.line_or_change_bus = [40]
action146.line_or_change_bus = [41]
action146.line_ex_change_bus = [56]
actions.append(action146)
# ---- END OF ACTION ---
action147 = env.action_space()
action147.line_or_change_bus = [36]
actions.append(action147)
# ---- END OF ACTION ---
action148 = env.action_space()
action148.gen_change_bus = [9]
action148.line_or_change_bus = [36]
actions.append(action148)
# ---- END OF ACTION ---
action149 = env.action_space()
action149.gen_change_bus = [21]
action149.load_change_bus = [33]
action149.load_change_bus = [34]
action149.load_change_bus = [36]
action149.line_ex_change_bus = [54]
actions.append(action149)
# ---- END OF ACTION ---
action150 = env.action_space()
action150.gen_change_bus = [2]
action150.load_change_bus = [10]
actions.append(action150)
# ---- END OF ACTION ---
action151 = env.action_space()
action151.gen_change_bus = [13]
action151.load_change_bus = [24]
action151.line_or_change_bus = [32]
action151.line_or_change_bus = [34]
action151.line_or_change_bus = [37]
action151.line_or_change_bus = [38]
actions.append(action151)
# ---- END OF ACTION ---
action152 = env.action_space()
action152.load_change_bus = [31]
action152.line_ex_change_bus = [50]
action152.line_or_change_bus = [52]
actions.append(action152)
# ---- END OF ACTION ---
action153 = env.action_space()
action153.gen_change_bus = [3]
action153.load_change_bus = [10]
actions.append(action153)
# ---- END OF ACTION ---
action154 = env.action_space()
action154.load_change_bus = [10]
actions.append(action154)
# ---- END OF ACTION ---
action155 = env.action_space()
action155.load_change_bus = [2]
action155.load_change_bus = [3]
action155.line_or_change_bus = [4]
actions.append(action155)
# ---- END OF ACTION ---
action156 = env.action_space()
action156.load_change_bus = [13]
action156.line_or_change_bus = [20]
actions.append(action156)
# ---- END OF ACTION ---
action157 = env.action_space()
action157.line_or_change_bus = [13]
actions.append(action157)
# ---- END OF ACTION ---
action158 = env.action_space()
action158.gen_change_bus = [2]
action158.gen_change_bus = [3]
action158.load_change_bus = [10]
action158.line_or_change_bus = [18]
action158.line_or_change_bus = [19]
actions.append(action158)
# ---- END OF ACTION ---
action159 = env.action_space()
action159.gen_change_bus = [5]
action159.gen_change_bus = [6]
action159.gen_change_bus = [7]
action159.gen_change_bus = [8]
action159.line_ex_change_bus = [18]
action159.line_ex_change_bus = [19]
action159.line_or_change_bus = [22]
action159.line_or_change_bus = [23]
action159.line_or_change_bus = [27]
action159.line_or_change_bus = [28]
actions.append(action159)
# ---- END OF ACTION ---
action160 = env.action_space()
action160.gen_change_bus = [11]
actions.append(action160)
# ---- END OF ACTION ---
action161 = env.action_space()
action161.gen_change_bus = [10]
action161.load_change_bus = [23]
action161.line_or_change_bus = [31]
actions.append(action161)
# ---- END OF ACTION ---
action162 = env.action_space()
action162.line_or_change_bus = [5]
actions.append(action162)
# ---- END OF ACTION ---
action163 = env.action_space()
action163.gen_change_bus = [1]
action163.load_change_bus = [8]
actions.append(action163)
# ---- END OF ACTION ---
action164 = env.action_space()
action164.line_ex_change_bus = [37]
action164.line_ex_change_bus = [38]
action164.line_ex_change_bus = [39]
action164.line_or_change_bus = [40]
action164.line_or_change_bus = [41]
actions.append(action164)
# ---- END OF ACTION ---
action165 = env.action_space()
action165.line_or_change_bus = [44]
actions.append(action165)
# ---- END OF ACTION ---
action166 = env.action_space()
action166.line_or_change_bus = [44]
action166.line_ex_change_bus = [57]
actions.append(action166)
# ---- END OF ACTION ---
action167 = env.action_space()
action167.gen_change_bus = [2]
action167.line_or_change_bus = [19]
actions.append(action167)
# ---- END OF ACTION ---
action168 = env.action_space()
action168.load_change_bus = [8]
actions.append(action168)
# ---- END OF ACTION ---
action169 = env.action_space()
action169.gen_change_bus = [13]
action169.load_change_bus = [24]
actions.append(action169)
# ---- END OF ACTION ---
action170 = env.action_space()
action170.line_or_change_bus = [40]
action170.line_or_change_bus = [41]
actions.append(action170)
# ---- END OF ACTION ---
action171 = env.action_space()
action171.gen_change_bus = [6]
action171.gen_change_bus = [7]
action171.gen_change_bus = [8]
action171.line_ex_change_bus = [18]
action171.line_ex_change_bus = [19]
action171.line_or_change_bus = [27]
action171.line_or_change_bus = [28]
action171.line_or_change_bus = [54]
actions.append(action171)
# ---- END OF ACTION ---
action172 = env.action_space()
action172.gen_change_bus = [5]
action172.gen_change_bus = [8]
action172.line_ex_change_bus = [18]
action172.line_ex_change_bus = [19]
action172.line_ex_change_bus = [20]
action172.line_or_change_bus = [27]
action172.line_or_change_bus = [28]
actions.append(action172)
# ---- END OF ACTION ---
action173 = env.action_space()
action173.gen_change_bus = [20]
action173.line_or_change_bus = [52]
actions.append(action173)
# ---- END OF ACTION ---
action174 = env.action_space()
action174.gen_change_bus = [14]
actions.append(action174)
# ---- END OF ACTION ---
action175 = env.action_space()
action175.gen_change_bus = [9]
action175.load_change_bus = [22]
action175.line_ex_change_bus = [27]
action175.line_ex_change_bus = [28]
action175.line_or_change_bus = [36]
actions.append(action175)
# ---- END OF ACTION ---
action176 = env.action_space()
action176.gen_change_bus = [12]
actions.append(action176)
# ---- END OF ACTION ---
action177 = env.action_space()
action177.gen_change_bus = [11]
action177.gen_change_bus = [13]
action177.load_change_bus = [24]
action177.line_or_change_bus = [37]
action177.line_or_change_bus = [38]
actions.append(action177)
# ---- END OF ACTION ---
action178 = env.action_space()
action178.line_ex_change_bus = [27]
action178.line_or_change_bus = [29]
action178.line_or_change_bus = [30]
action178.line_or_change_bus = [36]
actions.append(action178)
# ---- END OF ACTION ---
action179 = env.action_space()
action179.load_change_bus = [13]
actions.append(action179)
# ---- END OF ACTION ---
action180 = env.action_space()
action180.load_change_bus = [20]
actions.append(action180)
# ---- END OF ACTION ---
action181 = env.action_space()
action181.line_or_change_bus = [5]
action181.line_or_change_bus = [6]
action181.line_ex_change_bus = [55]
actions.append(action181)
# ---- END OF ACTION ---
action182 = env.action_space()
action182.line_ex_change_bus = [7]
action182.load_change_bus = [8]
actions.append(action182)
# ---- END OF ACTION ---
action183 = env.action_space()
action183.gen_change_bus = [18]
action183.load_change_bus = [29]
action183.line_or_change_bus = [50]
actions.append(action183)
# ---- END OF ACTION ---
action184 = env.action_space()
action184.load_change_bus = [22]
action184.line_ex_change_bus = [28]
action184.line_or_change_bus = [29]
action184.line_or_change_bus = [30]
actions.append(action184)
# ---- END OF ACTION ---
action185 = env.action_space()
action185.line_or_change_bus = [6]
actions.append(action185)
# ---- END OF ACTION ---
action186 = env.action_space()
action186.line_or_change_bus = [57]
actions.append(action186)
# ---- END OF ACTION ---
action187 = env.action_space()
action187.load_change_bus = [14]
action187.line_or_change_bus = [16]
actions.append(action187)
# ---- END OF ACTION ---
action188 = env.action_space()
action188.gen_change_bus = [6]
action188.gen_change_bus = [7]
action188.line_ex_change_bus = [18]
action188.line_ex_change_bus = [19]
action188.line_or_change_bus = [27]
action188.line_or_change_bus = [28]
action188.line_or_change_bus = [54]
actions.append(action188)
# ---- END OF ACTION ---
action189 = env.action_space()
action189.load_change_bus = [24]
action189.line_or_change_bus = [32]
action189.line_or_change_bus = [34]
actions.append(action189)
# ---- END OF ACTION ---
action190 = env.action_space()
action190.load_change_bus = [31]
actions.append(action190)
# ---- END OF ACTION ---
action191 = env.action_space()
action191.gen_change_bus = [9]
action191.line_ex_change_bus = [27]
action191.line_or_change_bus = [36]
actions.append(action191)
# ---- END OF ACTION ---
action192 = env.action_space()
action192.gen_change_bus = [11]
action192.gen_change_bus = [12]
action192.gen_change_bus = [13]
action192.load_change_bus = [24]
action192.line_or_change_bus = [38]
actions.append(action192)
# ---- END OF ACTION ---
action193 = env.action_space()
action193.gen_change_bus = [13]
action193.line_or_change_bus = [32]
action193.line_or_change_bus = [34]
action193.line_or_change_bus = [37]
action193.line_or_change_bus = [38]
actions.append(action193)
# ---- END OF ACTION ---
action194 = env.action_space()
action194.gen_change_bus = [9]
action194.load_change_bus = [22]
action194.line_ex_change_bus = [27]
action194.line_ex_change_bus = [28]
action194.line_or_change_bus = [30]
actions.append(action194)
# ---- END OF ACTION ---
action195 = env.action_space()
action195.load_change_bus = [28]
action195.line_or_change_bus = [42]
actions.append(action195)
# ---- END OF ACTION ---
action196 = env.action_space()
action196.line_ex_change_bus = [37]
action196.line_ex_change_bus = [38]
action196.line_or_change_bus = [41]
actions.append(action196)
# ---- END OF ACTION ---
action197 = env.action_space()
action197.gen_change_bus = [14]
action197.line_ex_change_bus = [39]
actions.append(action197)
# ---- END OF ACTION ---
action198 = env.action_space()
action198.gen_change_bus = [6]
action198.gen_change_bus = [7]
action198.line_or_change_bus = [54]
actions.append(action198)
# ---- END OF ACTION ---
action199 = env.action_space()
action199.load_change_bus = [3]
action199.line_or_change_bus = [4]
actions.append(action199)
# ---- END OF ACTION ---
action200 = env.action_space()
action200.line_ex_change_bus = [47]
actions.append(action200)
# ---- END OF ACTION ---
action201 = env.action_space()
action201.gen_change_bus = [18]
action201.line_ex_change_bus = [44]
action201.line_or_change_bus = [51]
actions.append(action201)
# ---- END OF ACTION ---
action202 = env.action_space()
action202.load_change_bus = [8]
action202.line_or_change_bus = [9]
actions.append(action202)
# ---- END OF ACTION ---
action203 = env.action_space()
action203.gen_change_bus = [13]
action203.load_change_bus = [24]
action203.line_or_change_bus = [32]
action203.line_or_change_bus = [34]
action203.line_or_change_bus = [37]
actions.append(action203)
# ---- END OF ACTION ---
action204 = env.action_space()
action204.gen_change_bus = [17]
actions.append(action204)
# ---- END OF ACTION ---
action205 = env.action_space()
action205.gen_change_bus = [9]
action205.load_change_bus = [22]
action205.line_ex_change_bus = [28]
action205.line_or_change_bus = [36]
actions.append(action205)
# ---- END OF ACTION ---
action206 = env.action_space()
action206.gen_change_bus = [1]
action206.load_change_bus = [8]
action206.line_or_change_bus = [9]
actions.append(action206)
# ---- END OF ACTION ---
action207 = env.action_space()
action207.gen_change_bus = [5]
action207.gen_change_bus = [7]
action207.gen_change_bus = [8]
action207.line_ex_change_bus = [18]
action207.line_ex_change_bus = [19]
action207.line_or_change_bus = [27]
action207.line_or_change_bus = [28]
actions.append(action207)
# ---- END OF ACTION ---
action208 = env.action_space()
action208.load_change_bus = [17]
action208.line_ex_change_bus = [18]
action208.line_ex_change_bus = [19]
action208.line_ex_change_bus = [20]
action208.line_or_change_bus = [54]
actions.append(action208)
# ---- END OF ACTION ---
action209 = env.action_space()
action209.load_change_bus = [24]
actions.append(action209)
# ---- END OF ACTION ---
action210 = env.action_space()
action210.gen_change_bus = [2]
action210.gen_change_bus = [3]
action210.load_change_bus = [10]
action210.line_or_change_bus = [19]
actions.append(action210)
# ---- END OF ACTION ---
action211 = env.action_space()
action211.gen_change_bus = [12]
action211.line_ex_change_bus = [31]
action211.line_or_change_bus = [34]
action211.line_or_change_bus = [37]
action211.line_or_change_bus = [38]
actions.append(action211)
# ---- END OF ACTION ---
action212 = env.action_space()
action212.line_ex_change_bus = [39]
action212.line_or_change_bus = [40]
action212.line_or_change_bus = [41]
actions.append(action212)
# ---- END OF ACTION ---
action213 = env.action_space()
action213.load_change_bus = [17]
action213.line_ex_change_bus = [19]
action213.line_ex_change_bus = [20]
action213.line_ex_change_bus = [21]
action213.line_or_change_bus = [28]
action213.line_or_change_bus = [54]
actions.append(action213)
# ---- END OF ACTION ---
action214 = env.action_space()
action214.load_change_bus = [22]
action214.line_ex_change_bus = [28]
action214.line_or_change_bus = [29]
action214.line_or_change_bus = [30]
action214.line_or_change_bus = [36]
actions.append(action214)
# ---- END OF ACTION ---
action215 = env.action_space()
action215.gen_change_bus = [1]
action215.line_or_change_bus = [9]
actions.append(action215)
# ---- END OF ACTION ---
action216 = env.action_space()
action216.load_change_bus = [17]
actions.append(action216)
# ---- END OF ACTION ---
action217 = env.action_space()
action217.gen_change_bus = [2]
action217.gen_change_bus = [3]
action217.load_change_bus = [10]
action217.line_or_change_bus = [19]
actions.append(action217)
# ---- END OF ACTION ---
action218 = env.action_space()
action218.line_or_change_bus = [18]
actions.append(action218)
# ---- END OF ACTION ---
action219 = env.action_space()
action219.gen_change_bus = [21]
action219.load_change_bus = [34]
action219.load_change_bus = [35]
action219.load_change_bus = [36]
action219.line_ex_change_bus = [54]
actions.append(action219)
# ---- END OF ACTION ---
action220 = env.action_space()
action220.load_change_bus = [24]
action220.line_or_change_bus = [32]
action220.line_or_change_bus = [34]
action220.line_or_change_bus = [37]
action220.line_or_change_bus = [38]
actions.append(action220)
# ---- END OF ACTION ---
action221 = env.action_space()
action221.load_change_bus = [27]
actions.append(action221)
# ---- END OF ACTION ---
action222 = env.action_space()
action222.line_ex_change_bus = [38]
action222.line_or_change_bus = [41]
actions.append(action222)
# ---- END OF ACTION ---
action223 = env.action_space()
action223.load_change_bus = [17]
action223.line_or_change_bus = [22]
action223.line_or_change_bus = [23]
action223.line_or_change_bus = [28]
action223.line_or_change_bus = [48]
action223.line_or_change_bus = [49]
actions.append(action223)
# ---- END OF ACTION ---
action224 = env.action_space()
action224.gen_change_bus = [21]
action224.load_change_bus = [34]
action224.load_change_bus = [35]
action224.line_ex_change_bus = [54]
actions.append(action224)
# ---- END OF ACTION ---
action225 = env.action_space()
action225.gen_change_bus = [0]
action225.load_change_bus = [2]
actions.append(action225)
# ---- END OF ACTION ---
action226 = env.action_space()
action226.gen_change_bus = [14]
action226.load_change_bus = [27]
action226.line_ex_change_bus = [37]
action226.line_ex_change_bus = [38]
actions.append(action226)
# ---- END OF ACTION ---
action227 = env.action_space()
action227.gen_change_bus = [2]
action227.load_change_bus = [10]
action227.line_or_change_bus = [19]
actions.append(action227)
# ---- END OF ACTION ---
action228 = env.action_space()
action228.load_change_bus = [10]
action228.line_or_change_bus = [19]
actions.append(action228)
# ---- END OF ACTION ---
action229 = env.action_space()
action229.line_ex_change_bus = [39]
action229.line_or_change_bus = [40]
actions.append(action229)
# ---- END OF ACTION ---
action230 = env.action_space()
action230.line_or_change_bus = [54]
actions.append(action230)
# ---- END OF ACTION ---
action231 = env.action_space()
action231.gen_change_bus = [9]
action231.load_change_bus = [22]
action231.line_ex_change_bus = [27]
action231.line_ex_change_bus = [28]
actions.append(action231)
# ---- END OF ACTION ---
action232 = env.action_space()
action232.load_change_bus = [17]
action232.line_ex_change_bus = [20]
action232.line_or_change_bus = [22]
action232.line_or_change_bus = [49]
actions.append(action232)
# ---- END OF ACTION ---
action233 = env.action_space()
action233.line_ex_change_bus = [7]
action233.line_or_change_bus = [9]
actions.append(action233)
# ---- END OF ACTION ---
action234 = env.action_space()
action234.gen_change_bus = [14]
action234.load_change_bus = [27]
action234.line_ex_change_bus = [37]
action234.line_or_change_bus = [41]
actions.append(action234)
# ---- END OF ACTION ---
action235 = env.action_space()
action235.line_or_change_bus = [49]
actions.append(action235)
# ---- END OF ACTION ---
action236 = env.action_space()
action236.line_or_change_bus = [9]
actions.append(action236)
# ---- END OF ACTION ---
action237 = env.action_space()
action237.line_or_change_bus = [29]
action237.line_or_change_bus = [30]
action237.line_or_change_bus = [36]
actions.append(action237)
# ---- END OF ACTION ---
action238 = env.action_space()
action238.line_or_change_bus = [8]
actions.append(action238)
# ---- END OF ACTION ---
action239 = env.action_space()
action239.gen_change_bus = [16]
action239.line_ex_change_bus = [42]
action239.line_or_change_bus = [44]
actions.append(action239)
# ---- END OF ACTION ---
action240 = env.action_space()
action240.gen_change_bus = [9]
action240.load_change_bus = [22]
action240.line_or_change_bus = [29]
action240.line_or_change_bus = [30]
action240.line_or_change_bus = [36]
actions.append(action240)
# ---- END OF ACTION ---
action241 = env.action_space()
action241.line_ex_change_bus = [27]
action241.line_or_change_bus = [36]
actions.append(action241)
# ---- END OF ACTION ---
action242 = env.action_space()
action242.gen_change_bus = [19]
action242.line_ex_change_bus = [47]
action242.line_or_change_bus = [58]
actions.append(action242)
# ---- END OF ACTION ---
action243 = env.action_space()
action243.gen_change_bus = [11]
action243.load_change_bus = [24]
action243.line_or_change_bus = [32]
action243.line_or_change_bus = [34]
actions.append(action243)
# ---- END OF ACTION ---
action244 = env.action_space()
action244.load_change_bus = [19]
actions.append(action244)
# ---- END OF ACTION ---
action245 = env.action_space()
action245.gen_change_bus = [5]
action245.gen_change_bus = [6]
action245.gen_change_bus = [7]
action245.gen_change_bus = [8]
action245.line_ex_change_bus = [19]
action245.line_ex_change_bus = [21]
action245.line_or_change_bus = [23]
action245.line_or_change_bus = [27]
action245.line_or_change_bus = [28]
action245.line_or_change_bus = [48]
action245.line_or_change_bus = [49]
action245.line_or_change_bus = [54]
actions.append(action245)
# ---- END OF ACTION ---
action246 = env.action_space()
action246.load_change_bus = [17]
action246.line_ex_change_bus = [19]
action246.line_ex_change_bus = [20]
action246.line_ex_change_bus = [21]
action246.line_or_change_bus = [22]
action246.line_or_change_bus = [54]
actions.append(action246)
# ---- END OF ACTION ---
action247 = env.action_space()
action247.line_ex_change_bus = [37]
action247.line_ex_change_bus = [38]
action247.line_ex_change_bus = [39]
action247.line_or_change_bus = [41]
actions.append(action247)
# ---- END OF ACTION ---
action248 = env.action_space()
action248.line_ex_change_bus = [56]
actions.append(action248)
# ---- END OF ACTION ---
action249 = env.action_space()
action249.gen_change_bus = [1]
action249.line_or_change_bus = [8]
actions.append(action249)
# ---- END OF ACTION ---
action250 = env.action_space()
action250.gen_change_bus = [2]
action250.gen_change_bus = [3]
action250.line_or_change_bus = [18]
actions.append(action250)
# ---- END OF ACTION ---
action251 = env.action_space()
action251.gen_change_bus = [14]
action251.load_change_bus = [27]
actions.append(action251)
# ---- END OF ACTION ---
action252 = env.action_space()
action252.gen_change_bus = [2]
action252.line_ex_change_bus = [10]
action252.line_or_change_bus = [19]
actions.append(action252)
# ---- END OF ACTION ---
action253 = env.action_space()
action253.line_ex_change_bus = [2]
actions.append(action253)
# ---- END OF ACTION ---
action254 = env.action_space()
action254.gen_change_bus = [2]
action254.load_change_bus = [10]
action254.line_or_change_bus = [18]
actions.append(action254)
# ---- END OF ACTION ---
action255 = env.action_space()
action255.gen_change_bus = [5]
action255.gen_change_bus = [6]
action255.gen_change_bus = [7]
action255.gen_change_bus = [8]
action255.line_ex_change_bus = [19]
action255.line_or_change_bus = [23]
action255.line_or_change_bus = [27]
action255.line_or_change_bus = [28]
action255.line_or_change_bus = [48]
action255.line_or_change_bus = [49]
actions.append(action255)
# ---- END OF ACTION ---
action256 = env.action_space()
action256.line_ex_change_bus = [2]
action256.line_or_change_bus = [5]
action256.line_or_change_bus = [6]
action256.line_ex_change_bus = [55]
actions.append(action256)
# ---- END OF ACTION ---
action257 = env.action_space()
action257.line_ex_change_bus = [38]
action257.line_ex_change_bus = [39]
action257.line_or_change_bus = [40]
actions.append(action257)
# ---- END OF ACTION ---
action258 = env.action_space()
action258.line_ex_change_bus = [37]
action258.line_ex_change_bus = [39]
actions.append(action258)
# ---- END OF ACTION ---
action259 = env.action_space()
action259.gen_change_bus = [5]
action259.gen_change_bus = [6]
action259.gen_change_bus = [7]
action259.line_ex_change_bus = [18]
action259.line_ex_change_bus = [19]
action259.line_or_change_bus = [27]
action259.line_or_change_bus = [28]
action259.line_or_change_bus = [54]
actions.append(action259)
# ---- END OF ACTION ---
action260 = env.action_space()
action260.line_ex_change_bus = [19]
action260.line_or_change_bus = [22]
action260.line_or_change_bus = [23]
action260.line_or_change_bus = [27]
action260.line_or_change_bus = [28]
action260.line_or_change_bus = [48]
action260.line_or_change_bus = [49]
action260.line_or_change_bus = [54]
actions.append(action260)
# ---- END OF ACTION ---
action261 = env.action_space()
action261.gen_change_bus = [21]
action261.load_change_bus = [35]
action261.load_change_bus = [36]
action261.line_ex_change_bus = [54]
actions.append(action261)
# ---- END OF ACTION ---
action262 = env.action_space()
action262.gen_change_bus = [9]
action262.load_change_bus = [22]
action262.line_ex_change_bus = [27]
action262.line_ex_change_bus = [28]
action262.line_or_change_bus = [29]
action262.line_or_change_bus = [30]
actions.append(action262)
# ---- END OF ACTION ---
action263 = env.action_space()
action263.gen_change_bus = [11]
action263.gen_change_bus = [12]
action263.gen_change_bus = [13]
action263.load_change_bus = [24]
action263.line_or_change_bus = [34]
action263.line_or_change_bus = [37]
actions.append(action263)
# ---- END OF ACTION ---
action264 = env.action_space()
action264.gen_change_bus = [6]
action264.gen_change_bus = [7]
action264.gen_change_bus = [8]
action264.line_ex_change_bus = [18]
action264.line_ex_change_bus = [19]
action264.line_or_change_bus = [27]
action264.line_or_change_bus = [28]
actions.append(action264)
# ---- END OF ACTION ---
action265 = env.action_space()
action265.gen_change_bus = [9]
action265.load_change_bus = [22]
action265.line_or_change_bus = [29]
action265.line_or_change_bus = [30]
actions.append(action265)
# ---- END OF ACTION ---
action266 = env.action_space()
action266.line_ex_change_bus = [39]
action266.line_or_change_bus = [41]
actions.append(action266)
# ---- END OF ACTION ---
action267 = env.action_space()
action267.gen_change_bus = [9]
action267.load_change_bus = [22]
action267.line_ex_change_bus = [27]
actions.append(action267)
# ---- END OF ACTION ---
action268 = env.action_space()
action268.gen_change_bus = [14]
action268.line_ex_change_bus = [37]
action268.line_ex_change_bus = [38]
action268.line_or_change_bus = [41]
actions.append(action268)
# ---- END OF ACTION ---
action269 = env.action_space()
action269.gen_change_bus = [8]
action269.load_change_bus = [17]
action269.line_or_change_bus = [22]
action269.line_or_change_bus = [23]
action269.line_or_change_bus = [28]
action269.line_or_change_bus = [48]
action269.line_or_change_bus = [49]
actions.append(action269)
# ---- END OF ACTION ---
action270 = env.action_space()
action270.gen_change_bus = [5]
action270.gen_change_bus = [6]
action270.gen_change_bus = [7]
action270.gen_change_bus = [8]
action270.line_ex_change_bus = [21]
action270.line_or_change_bus = [23]
action270.line_or_change_bus = [27]
action270.line_or_change_bus = [28]
action270.line_or_change_bus = [48]
action270.line_or_change_bus = [49]
action270.line_or_change_bus = [54]
actions.append(action270)
# ---- END OF ACTION ---
action271 = env.action_space()
action271.load_change_bus = [17]
action271.line_ex_change_bus = [19]
action271.line_ex_change_bus = [20]
action271.line_or_change_bus = [27]
action271.line_or_change_bus = [28]
actions.append(action271)
# ---- END OF ACTION ---
action272 = env.action_space()
action272.gen_change_bus = [14]
action272.line_or_change_bus = [40]
action272.line_or_change_bus = [41]
actions.append(action272)
# ---- END OF ACTION ---
action273 = env.action_space()
action273.gen_change_bus = [11]
action273.gen_change_bus = [12]
action273.gen_change_bus = [13]
action273.load_change_bus = [24]
actions.append(action273)
# ---- END OF ACTION ---
action274 = env.action_space()
action274.gen_change_bus = [5]
action274.gen_change_bus = [6]
action274.gen_change_bus = [7]
action274.gen_change_bus = [8]
action274.load_change_bus = [17]
action274.line_ex_change_bus = [18]
action274.line_ex_change_bus = [19]
action274.line_ex_change_bus = [21]
action274.line_or_change_bus = [22]
action274.line_or_change_bus = [23]
action274.line_or_change_bus = [27]
action274.line_or_change_bus = [28]
action274.line_or_change_bus = [48]
action274.line_or_change_bus = [49]
action274.line_or_change_bus = [54]
actions.append(action274)
# ---- END OF ACTION ---
action275 = env.action_space()
action275.gen_change_bus = [2]
action275.gen_change_bus = [3]
action275.load_change_bus = [10]
actions.append(action275)
# ---- END OF ACTION ---
action276 = env.action_space()
action276.gen_change_bus = [16]
action276.line_or_change_bus = [44]
action276.line_ex_change_bus = [57]
actions.append(action276)
# ---- END OF ACTION ---
action277 = env.action_space()
action277.gen_change_bus = [12]
action277.load_change_bus = [24]
action277.line_or_change_bus = [32]
action277.line_or_change_bus = [34]
actions.append(action277)
# ---- END OF ACTION ---
action278 = env.action_space()
action278.line_or_change_bus = [40]
actions.append(action278)
# ---- END OF ACTION ---
action279 = env.action_space()
action279.gen_change_bus = [13]
action279.load_change_bus = [24]
action279.line_or_change_bus = [34]
actions.append(action279)
# ---- END OF ACTION ---
action280 = env.action_space()
action280.gen_change_bus = [5]
action280.gen_change_bus = [6]
action280.gen_change_bus = [7]
action280.gen_change_bus = [8]
action280.line_ex_change_bus = [19]
action280.line_ex_change_bus = [21]
action280.line_or_change_bus = [22]
action280.line_or_change_bus = [23]
action280.line_or_change_bus = [28]
action280.line_or_change_bus = [48]
action280.line_or_change_bus = [49]
action280.line_or_change_bus = [54]
actions.append(action280)
# ---- END OF ACTION ---
action281 = env.action_space()
action281.gen_change_bus = [9]
action281.line_or_change_bus = [29]
action281.line_or_change_bus = [30]
action281.line_or_change_bus = [36]
actions.append(action281)
# ---- END OF ACTION ---
action282 = env.action_space()
action282.gen_change_bus = [13]
action282.load_change_bus = [24]
action282.line_or_change_bus = [32]
actions.append(action282)
# ---- END OF ACTION ---
action283 = env.action_space()
action283.gen_change_bus = [14]
action283.line_ex_change_bus = [38]
action283.line_or_change_bus = [40]
action283.line_or_change_bus = [41]
actions.append(action283)
# ---- END OF ACTION ---
action284 = env.action_space()
action284.load_change_bus = [22]
action284.line_ex_change_bus = [27]
action284.line_or_change_bus = [29]
action284.line_or_change_bus = [30]
action284.line_or_change_bus = [36]
actions.append(action284)
# ---- END OF ACTION ---
action285 = env.action_space()
action285.gen_change_bus = [12]
action285.load_change_bus = [24]
action285.line_or_change_bus = [37]
action285.line_or_change_bus = [38]
actions.append(action285)
# ---- END OF ACTION ---
action286 = env.action_space()
action286.gen_change_bus = [7]
action286.line_or_change_bus = [54]
actions.append(action286)
# ---- END OF ACTION ---
action287 = env.action_space()
action287.gen_change_bus = [3]
action287.load_change_bus = [10]
action287.line_or_change_bus = [18]
action287.line_or_change_bus = [19]
actions.append(action287)
# ---- END OF ACTION ---
action288 = env.action_space()
action288.load_change_bus = [2]
action288.line_or_change_bus = [4]
action288.line_or_change_bus = [12]
actions.append(action288)
# ---- END OF ACTION ---
action289 = env.action_space()
action289.gen_change_bus = [2]
action289.gen_change_bus = [3]
action289.line_ex_change_bus = [10]
action289.line_or_change_bus = [19]
actions.append(action289)
# ---- END OF ACTION ---
action290 = env.action_space()
action290.gen_change_bus = [14]
action290.load_change_bus = [27]
action290.line_or_change_bus = [41]
actions.append(action290)
# ---- END OF ACTION ---
action291 = env.action_space()
action291.line_ex_change_bus = [37]
action291.line_ex_change_bus = [38]
action291.line_or_change_bus = [40]
actions.append(action291)
# ---- END OF ACTION ---
action292 = env.action_space()
action292.line_ex_change_bus = [37]
actions.append(action292)
# ---- END OF ACTION ---
action293 = env.action_space()
action293.gen_change_bus = [7]
action293.load_change_bus = [17]
action293.line_or_change_bus = [22]
action293.line_or_change_bus = [23]
action293.line_or_change_bus = [27]
action293.line_or_change_bus = [48]
action293.line_or_change_bus = [49]
actions.append(action293)
# ---- END OF ACTION ---
action294 = env.action_space()
action294.line_or_change_bus = [37]
actions.append(action294)
# ---- END OF ACTION ---
action295 = env.action_space()
action295.gen_change_bus = [9]
actions.append(action295)
# ---- END OF ACTION ---
action296 = env.action_space()
action296.gen_change_bus = [5]
action296.gen_change_bus = [8]
action296.line_ex_change_bus = [19]
action296.line_or_change_bus = [27]
action296.line_or_change_bus = [28]
action296.line_or_change_bus = [54]
actions.append(action296)
# ---- END OF ACTION ---
action297 = env.action_space()
action297.gen_change_bus = [13]
actions.append(action297)
# ---- END OF ACTION ---
action298 = env.action_space()
action298.load_change_bus = [22]
action298.line_ex_change_bus = [27]
actions.append(action298)
# ---- END OF ACTION ---
action299 = env.action_space()
action299.gen_change_bus = [3]
action299.load_change_bus = [10]
actions.append(action299)
# ---- END OF ACTION ---
action300 = env.action_space()
action300.load_change_bus = [22]
action300.line_ex_change_bus = [27]
action300.line_ex_change_bus = [28]
action300.line_or_change_bus = [30]
action300.line_or_change_bus = [36]
actions.append(action300)
# ---- END OF ACTION ---
action301 = env.action_space()
action301.gen_change_bus = [11]
action301.gen_change_bus = [12]
action301.load_change_bus = [24]
action301.line_or_change_bus = [32]
action301.line_or_change_bus = [34]
actions.append(action301)
# ---- END OF ACTION ---
action302 = env.action_space()
action302.gen_change_bus = [11]
action302.gen_change_bus = [12]
action302.load_change_bus = [24]
action302.line_or_change_bus = [32]
action302.line_or_change_bus = [34]
action302.line_or_change_bus = [37]
action302.line_or_change_bus = [38]
actions.append(action302)
# ---- END OF ACTION ---
action303 = env.action_space()
action303.gen_change_bus = [8]
action303.line_ex_change_bus = [18]
action303.line_ex_change_bus = [19]
action303.line_or_change_bus = [27]
action303.line_or_change_bus = [28]
action303.line_or_change_bus = [54]
actions.append(action303)
# ---- END OF ACTION ---
action304 = env.action_space()
action304.gen_change_bus = [14]
action304.load_change_bus = [27]
action304.line_ex_change_bus = [37]
action304.line_ex_change_bus = [38]
action304.line_or_change_bus = [40]
action304.line_ex_change_bus = [56]
actions.append(action304)
# ---- END OF ACTION ---
action305 = env.action_space()
action305.line_ex_change_bus = [37]
action305.line_ex_change_bus = [39]
action305.line_or_change_bus = [40]
action305.line_or_change_bus = [41]
actions.append(action305)
# ---- END OF ACTION ---
action306 = env.action_space()
action306.gen_change_bus = [12]
action306.line_or_change_bus = [34]
action306.line_or_change_bus = [37]
action306.line_or_change_bus = [38]
actions.append(action306)
# ---- END OF ACTION ---
action307 = env.action_space()
action307.load_change_bus = [30]
action307.line_ex_change_bus = [47]
actions.append(action307)
# ---- END OF ACTION ---
action308 = env.action_space()
action308.load_change_bus = [10]
action308.line_or_change_bus = [18]
actions.append(action308)
# ---- END OF ACTION ---
action309 = env.action_space()
action309.gen_change_bus = [7]
action309.load_change_bus = [17]
action309.line_ex_change_bus = [20]
action309.line_ex_change_bus = [21]
action309.line_or_change_bus = [22]
action309.line_or_change_bus = [23]
action309.line_or_change_bus = [48]
action309.line_or_change_bus = [49]
actions.append(action309)
# ---- END OF ACTION ---
action310 = env.action_space()
action310.gen_change_bus = [9]
action310.line_ex_change_bus = [28]
action310.line_or_change_bus = [36]
actions.append(action310)
# ---- END OF ACTION ---
action311 = env.action_space()
action311.load_change_bus = [22]
action311.line_ex_change_bus = [27]
action311.line_or_change_bus = [29]
action311.line_or_change_bus = [30]
actions.append(action311)
# ---- END OF ACTION ---
action312 = env.action_space()
action312.line_ex_change_bus = [38]
action312.line_or_change_bus = [40]
actions.append(action312)
# ---- END OF ACTION ---
action313 = env.action_space()
action313.gen_change_bus = [9]
action313.line_or_change_bus = [29]
actions.append(action313)
# ---- END OF ACTION ---
action314 = env.action_space()
action314.gen_change_bus = [12]
action314.load_change_bus = [24]
action314.line_or_change_bus = [32]
action314.line_or_change_bus = [34]
action314.line_or_change_bus = [37]
action314.line_or_change_bus = [38]
actions.append(action314)
# ---- END OF ACTION ---
action315 = env.action_space()
action315.line_or_change_bus = [30]
action315.line_or_change_bus = [36]
actions.append(action315)
# ---- END OF ACTION ---
action316 = env.action_space()
action316.gen_change_bus = [9]
action316.load_change_bus = [22]
action316.line_ex_change_bus = [27]
action316.line_or_change_bus = [29]
action316.line_or_change_bus = [30]
action316.line_or_change_bus = [36]
actions.append(action316)
# ---- END OF ACTION ---
action317 = env.action_space()
action317.load_change_bus = [17]
action317.line_ex_change_bus = [18]
action317.line_ex_change_bus = [19]
action317.line_ex_change_bus = [20]
action317.line_ex_change_bus = [21]
action317.line_or_change_bus = [27]
actions.append(action317)
# ---- END OF ACTION ---
action318 = env.action_space()
action318.gen_change_bus = [1]
action318.line_ex_change_bus = [7]
action318.load_change_bus = [8]
action318.line_or_change_bus = [9]
actions.append(action318)
# ---- END OF ACTION ---
action319 = env.action_space()
action319.gen_change_bus = [9]
action319.line_ex_change_bus = [27]
action319.line_or_change_bus = [29]
action319.line_or_change_bus = [30]
action319.line_or_change_bus = [36]
actions.append(action319)
# ---- END OF ACTION ---
action320 = env.action_space()
action320.line_or_change_bus = [28]
actions.append(action320)
# ---- END OF ACTION ---
action321 = env.action_space()
action321.line_ex_change_bus = [28]
action321.line_or_change_bus = [36]
actions.append(action321)
# ---- END OF ACTION ---
action322 = env.action_space()
action322.gen_change_bus = [11]
action322.gen_change_bus = [12]
action322.gen_change_bus = [13]
action322.line_or_change_bus = [37]
actions.append(action322)
# ---- END OF ACTION ---
action323 = env.action_space()
action323.gen_change_bus = [11]
action323.gen_change_bus = [12]
action323.gen_change_bus = [13]
action323.load_change_bus = [24]
action323.line_ex_change_bus = [31]
action323.line_or_change_bus = [32]
action323.line_or_change_bus = [34]
actions.append(action323)
# ---- END OF ACTION ---
action324 = env.action_space()
action324.gen_change_bus = [14]
action324.line_ex_change_bus = [37]
action324.line_or_change_bus = [40]
actions.append(action324)
# ---- END OF ACTION ---
action325 = env.action_space()
action325.line_ex_change_bus = [38]
actions.append(action325)
# ---- END OF ACTION ---
action326 = env.action_space()
action326.gen_change_bus = [14]
action326.line_or_change_bus = [40]
action326.line_or_change_bus = [41]
action326.line_ex_change_bus = [56]
actions.append(action326)
# ---- END OF ACTION ---
action327 = env.action_space()
action327.gen_change_bus = [14]
action327.load_change_bus = [27]
action327.line_ex_change_bus = [37]
action327.line_ex_change_bus = [38]
action327.line_ex_change_bus = [56]
actions.append(action327)
# ---- END OF ACTION ---
action328 = env.action_space()
action328.gen_change_bus = [12]
action328.line_or_change_bus = [32]
action328.line_or_change_bus = [34]
action328.line_or_change_bus = [37]
action328.line_or_change_bus = [38]
actions.append(action328)
# ---- END OF ACTION ---
action329 = env.action_space()
action329.gen_change_bus = [12]
action329.load_change_bus = [24]
action329.line_or_change_bus = [32]
action329.line_or_change_bus = [34]
action329.line_or_change_bus = [38]
actions.append(action329)
# ---- END OF ACTION ---
action330 = env.action_space()
action330.gen_change_bus = [5]
action330.gen_change_bus = [6]
action330.gen_change_bus = [7]
action330.gen_change_bus = [8]
action330.line_ex_change_bus = [19]
action330.line_ex_change_bus = [21]
action330.line_or_change_bus = [22]
action330.line_or_change_bus = [23]
action330.line_or_change_bus = [27]
action330.line_or_change_bus = [28]
action330.line_or_change_bus = [48]
action330.line_or_change_bus = [49]
actions.append(action330)
# ---- END OF ACTION ---
action331 = env.action_space()
action331.gen_change_bus = [14]
action331.line_ex_change_bus = [38]
actions.append(action331)
# ---- END OF ACTION ---
action332 = env.action_space()
action332.load_change_bus = [17]
action332.line_ex_change_bus = [18]
action332.line_ex_change_bus = [19]
action332.line_ex_change_bus = [20]
action332.line_ex_change_bus = [21]
action332.line_or_change_bus = [28]
actions.append(action332)
# ---- END OF ACTION ---
action333 = env.action_space()
action333.gen_change_bus = [2]
action333.load_change_bus = [10]
actions.append(action333)
# ---- END OF ACTION ---
action334 = env.action_space()
action334.line_or_change_bus = [32]
action334.line_or_change_bus = [37]
action334.line_or_change_bus = [38]
actions.append(action334)
# ---- END OF ACTION ---
action335 = env.action_space()
action335.gen_change_bus = [5]
action335.gen_change_bus = [6]
action335.gen_change_bus = [7]
action335.gen_change_bus = [8]
action335.line_ex_change_bus = [18]
action335.line_ex_change_bus = [19]
action335.line_or_change_bus = [22]
action335.line_or_change_bus = [23]
action335.line_or_change_bus = [27]
action335.line_or_change_bus = [28]
action335.line_or_change_bus = [54]
actions.append(action335)
# ---- END OF ACTION ---
action336 = env.action_space()
action336.gen_change_bus = [14]
action336.load_change_bus = [27]
action336.line_ex_change_bus = [37]
action336.line_or_change_bus = [40]
actions.append(action336)
# ---- END OF ACTION ---
action337 = env.action_space()
action337.gen_change_bus = [8]
action337.load_change_bus = [17]
actions.append(action337)
# ---- END OF ACTION ---
action338 = env.action_space()
action338.gen_change_bus = [9]
action338.load_change_bus = [22]
actions.append(action338)
# ---- END OF ACTION ---
action339 = env.action_space()
action339.gen_change_bus = [5]
action339.line_ex_change_bus = [18]
action339.line_ex_change_bus = [19]
action339.line_or_change_bus = [27]
action339.line_or_change_bus = [28]
action339.line_or_change_bus = [54]
actions.append(action339)
# ---- END OF ACTION ---
action340 = env.action_space()
action340.line_ex_change_bus = [37]
action340.line_or_change_bus = [40]
actions.append(action340)
# ---- END OF ACTION ---
action341 = env.action_space()
action341.line_ex_change_bus = [31]
action341.line_or_change_bus = [34]
action341.line_or_change_bus = [38]
actions.append(action341)
# ---- END OF ACTION ---
action342 = env.action_space()
action342.gen_change_bus = [11]
action342.gen_change_bus = [12]
action342.gen_change_bus = [13]
action342.line_or_change_bus = [32]
action342.line_or_change_bus = [34]
action342.line_or_change_bus = [37]
action342.line_or_change_bus = [38]
actions.append(action342)
# ---- END OF ACTION ---
action343 = env.action_space()
action343.gen_change_bus = [8]
action343.load_change_bus = [17]
action343.line_ex_change_bus = [20]
action343.line_or_change_bus = [22]
action343.line_or_change_bus = [23]
action343.line_or_change_bus = [48]
action343.line_or_change_bus = [49]
actions.append(action343)
# ---- END OF ACTION ---
action344 = env.action_space()
action344.gen_change_bus = [19]
action344.line_or_change_bus = [58]
actions.append(action344)
# ---- END OF ACTION ---
action345 = env.action_space()
action345.gen_change_bus = [1]
action345.line_ex_change_bus = [7]
action345.load_change_bus = [8]
action345.line_or_change_bus = [9]
actions.append(action345)
# ---- END OF ACTION ---
action346 = env.action_space()
action346.gen_change_bus = [11]
action346.gen_change_bus = [12]
action346.gen_change_bus = [13]
action346.load_change_bus = [24]
action346.line_or_change_bus = [32]
action346.line_or_change_bus = [34]
action346.line_or_change_bus = [37]
action346.line_or_change_bus = [38]
actions.append(action346)
# ---- END OF ACTION ---
action347 = env.action_space()
action347.gen_change_bus = [11]
action347.gen_change_bus = [12]
action347.gen_change_bus = [13]
action347.line_or_change_bus = [37]
action347.line_or_change_bus = [38]
actions.append(action347)
# ---- END OF ACTION ---
action348 = env.action_space()
action348.line_ex_change_bus = [2]
action348.line_or_change_bus = [5]
actions.append(action348)
# ---- END OF ACTION ---
action349 = env.action_space()
action349.gen_change_bus = [3]
action349.line_or_change_bus = [18]
actions.append(action349)
# ---- END OF ACTION ---
action350 = env.action_space()
action350.line_ex_change_bus = [38]
action350.line_or_change_bus = [40]
action350.line_or_change_bus = [41]
actions.append(action350)
# ---- END OF ACTION ---
action351 = env.action_space()
action351.gen_change_bus = [11]
action351.gen_change_bus = [12]
action351.load_change_bus = [24]
actions.append(action351)
# ---- END OF ACTION ---
action352 = env.action_space()
action352.line_or_change_bus = [37]
action352.line_or_change_bus = [38]
actions.append(action352)
# ---- END OF ACTION ---
action353 = env.action_space()
action353.gen_change_bus = [14]
action353.load_change_bus = [27]
action353.line_ex_change_bus = [37]
action353.line_ex_change_bus = [38]
action353.line_or_change_bus = [41]
actions.append(action353)
# ---- END OF ACTION ---
action354 = env.action_space()
action354.line_ex_change_bus = [28]
action354.line_or_change_bus = [29]
action354.line_or_change_bus = [30]
action354.line_or_change_bus = [36]
actions.append(action354)
# ---- END OF ACTION ---
action355 = env.action_space()
action355.gen_change_bus = [3]
action355.load_change_bus = [10]
action355.line_or_change_bus = [19]
actions.append(action355)
# ---- END OF ACTION ---
action356 = env.action_space()
action356.gen_change_bus = [2]
action356.gen_change_bus = [3]
action356.load_change_bus = [10]
action356.line_or_change_bus = [18]
actions.append(action356)
# ---- END OF ACTION ---
action357 = env.action_space()
action357.gen_change_bus = [5]
action357.gen_change_bus = [8]
action357.load_change_bus = [17]
action357.line_or_change_bus = [22]
action357.line_or_change_bus = [23]
action357.line_or_change_bus = [28]
action357.line_or_change_bus = [48]
action357.line_or_change_bus = [49]
actions.append(action357)
# ---- END OF ACTION ---
action358 = env.action_space()
action358.line_or_change_bus = [39]
actions.append(action358)
# ---- END OF ACTION ---
action359 = env.action_space()
action359.gen_change_bus = [14]
action359.load_change_bus = [27]
action359.line_ex_change_bus = [37]
action359.line_ex_change_bus = [39]
action359.line_or_change_bus = [40]
actions.append(action359)
# ---- END OF ACTION ---
action360 = env.action_space()
action360.gen_change_bus = [13]
action360.load_change_bus = [24]
action360.line_or_change_bus = [34]
action360.line_or_change_bus = [38]
actions.append(action360)
# ---- END OF ACTION ---
action361 = env.action_space()
action361.gen_change_bus = [5]
action361.gen_change_bus = [7]
action361.gen_change_bus = [8]
action361.line_ex_change_bus = [18]
action361.line_ex_change_bus = [19]
action361.line_ex_change_bus = [20]
action361.line_or_change_bus = [27]
action361.line_or_change_bus = [28]
actions.append(action361)
# ---- END OF ACTION ---
action362 = env.action_space()
action362.gen_change_bus = [14]
action362.load_change_bus = [27]
action362.line_ex_change_bus = [38]
action362.line_ex_change_bus = [39]
action362.line_ex_change_bus = [56]
actions.append(action362)
# ---- END OF ACTION ---
action363 = env.action_space()
action363.gen_change_bus = [14]
action363.load_change_bus = [27]
action363.line_ex_change_bus = [37]
action363.line_ex_change_bus = [39]
actions.append(action363)
# ---- END OF ACTION ---
action364 = env.action_space()
action364.gen_change_bus = [21]
action364.load_change_bus = [33]
action364.load_change_bus = [35]
action364.load_change_bus = [36]
action364.line_ex_change_bus = [54]
actions.append(action364)
# ---- END OF ACTION ---
action365 = env.action_space()
action365.load_change_bus = [33]
action365.line_ex_change_bus = [54]
actions.append(action365)
# ---- END OF ACTION ---
action366 = env.action_space()
action366.load_change_bus = [6]
actions.append(action366)
# ---- END OF ACTION ---
action367 = env.action_space()
action367.gen_change_bus = [14]
action367.line_ex_change_bus = [37]
action367.line_ex_change_bus = [39]
actions.append(action367)
# ---- END OF ACTION ---
action368 = env.action_space()
action368.load_change_bus = [36]
action368.line_ex_change_bus = [54]
actions.append(action368)
# ---- END OF ACTION ---
action369 = env.action_space()
action369.gen_change_bus = [11]
action369.gen_change_bus = [12]
action369.gen_change_bus = [13]
actions.append(action369)
# ---- END OF ACTION ---
action370 = env.action_space()
action370.line_ex_change_bus = [27]
action370.line_or_change_bus = [30]
action370.line_or_change_bus = [36]
actions.append(action370)
# ---- END OF ACTION ---
action371 = env.action_space()
action371.gen_change_bus = [21]
action371.load_change_bus = [34]
action371.load_change_bus = [36]
action371.line_ex_change_bus = [54]
actions.append(action371)
# ---- END OF ACTION ---
action372 = env.action_space()
action372.gen_change_bus = [3]
action372.load_change_bus = [10]
action372.line_or_change_bus = [18]
actions.append(action372)
# ---- END OF ACTION ---
action373 = env.action_space()
action373.gen_change_bus = [5]
action373.gen_change_bus = [6]
action373.gen_change_bus = [7]
action373.gen_change_bus = [8]
action373.line_ex_change_bus = [19]
action373.line_ex_change_bus = [21]
action373.line_or_change_bus = [23]
action373.line_or_change_bus = [27]
action373.line_or_change_bus = [28]
action373.line_or_change_bus = [48]
action373.line_or_change_bus = [49]
actions.append(action373)
# ---- END OF ACTION ---
action374 = env.action_space()
action374.load_change_bus = [27]
action374.line_ex_change_bus = [37]
action374.line_ex_change_bus = [38]
action374.line_or_change_bus = [40]
action374.line_or_change_bus = [41]
action374.line_ex_change_bus = [56]
actions.append(action374)
# ---- END OF ACTION ---
action375 = env.action_space()
action375.gen_change_bus = [2]
action375.load_change_bus = [10]
action375.line_or_change_bus = [19]
actions.append(action375)
# ---- END OF ACTION ---
action376 = env.action_space()
action376.line_ex_change_bus = [7]
action376.load_change_bus = [8]
action376.line_or_change_bus = [9]
actions.append(action376)
# ---- END OF ACTION ---
action377 = env.action_space()
action377.line_ex_change_bus = [2]
action377.line_or_change_bus = [6]
action377.line_ex_change_bus = [55]
actions.append(action377)
# ---- END OF ACTION ---
action378 = env.action_space()
action378.gen_change_bus = [14]
action378.load_change_bus = [27]
action378.line_ex_change_bus = [37]
action378.line_ex_change_bus = [38]
action378.line_ex_change_bus = [39]
action378.line_ex_change_bus = [56]
actions.append(action378)
# ---- END OF ACTION ---
action379 = env.action_space()
action379.load_change_bus = [22]
action379.line_ex_change_bus = [27]
action379.line_ex_change_bus = [28]
action379.line_or_change_bus = [30]
actions.append(action379)
# ---- END OF ACTION ---
action380 = env.action_space()
action380.load_change_bus = [17]
action380.line_or_change_bus = [49]
actions.append(action380)
# ---- END OF ACTION ---
action381 = env.action_space()
action381.gen_change_bus = [5]
action381.gen_change_bus = [6]
action381.gen_change_bus = [7]
action381.gen_change_bus = [8]
action381.line_ex_change_bus = [19]
action381.line_or_change_bus = [22]
action381.line_or_change_bus = [23]
action381.line_or_change_bus = [28]
action381.line_or_change_bus = [48]
action381.line_or_change_bus = [49]
actions.append(action381)
# ---- END OF ACTION ---
action382 = env.action_space()
action382.gen_change_bus = [13]
action382.line_or_change_bus = [34]
action382.line_or_change_bus = [38]
actions.append(action382)
# ---- END OF ACTION ---
action383 = env.action_space()
action383.load_change_bus = [31]
action383.line_ex_change_bus = [49]
action383.line_ex_change_bus = [58]
actions.append(action383)
# ---- END OF ACTION ---
action384 = env.action_space()
action384.gen_change_bus = [2]
action384.line_or_change_bus = [18]
actions.append(action384)
# ---- END OF ACTION ---
action385 = env.action_space()
action385.line_ex_change_bus = [31]
action385.line_or_change_bus = [32]
action385.line_or_change_bus = [34]
action385.line_or_change_bus = [37]
actions.append(action385)
# ---- END OF ACTION ---
action386 = env.action_space()
action386.gen_change_bus = [5]
action386.gen_change_bus = [8]
action386.line_or_change_bus = [22]
action386.line_or_change_bus = [23]
action386.line_or_change_bus = [27]
action386.line_or_change_bus = [28]
action386.line_or_change_bus = [48]
action386.line_or_change_bus = [49]
actions.append(action386)
# ---- END OF ACTION ---
action387 = env.action_space()
action387.line_ex_change_bus = [18]
action387.line_ex_change_bus = [19]
action387.line_or_change_bus = [27]
action387.line_or_change_bus = [28]
actions.append(action387)
# ---- END OF ACTION ---
action388 = env.action_space()
action388.gen_change_bus = [5]
action388.gen_change_bus = [8]
action388.load_change_bus = [17]
action388.line_ex_change_bus = [19]
action388.line_or_change_bus = [22]
action388.line_or_change_bus = [23]
action388.line_or_change_bus = [28]
action388.line_or_change_bus = [48]
action388.line_or_change_bus = [49]
action388.line_or_change_bus = [54]
actions.append(action388)
# ---- END OF ACTION ---
action389 = env.action_space()
action389.line_ex_change_bus = [47]
action389.line_or_change_bus = [58]
actions.append(action389)
# ---- END OF ACTION ---
action390 = env.action_space()
action390.load_change_bus = [3]
action390.line_or_change_bus = [4]
action390.line_or_change_bus = [12]
actions.append(action390)
# ---- END OF ACTION ---
action391 = env.action_space()
action391.load_change_bus = [29]
action391.line_or_change_bus = [50]
action391.line_or_change_bus = [51]
actions.append(action391)
# ---- END OF ACTION ---
action392 = env.action_space()
action392.gen_change_bus = [5]
action392.gen_change_bus = [8]
action392.line_or_change_bus = [28]
action392.line_or_change_bus = [54]
actions.append(action392)
# ---- END OF ACTION ---
action393 = env.action_space()
action393.line_or_change_bus = [58]
actions.append(action393)
# ---- END OF ACTION ---
action394 = env.action_space()
action394.gen_change_bus = [21]
action394.load_change_bus = [33]
action394.load_change_bus = [36]
action394.line_ex_change_bus = [54]
actions.append(action394)
# ---- END OF ACTION ---
action395 = env.action_space()
action395.line_or_change_bus = [53]
actions.append(action395)
# ---- END OF ACTION ---
action396 = env.action_space()
action396.gen_change_bus = [14]
action396.load_change_bus = [27]
action396.line_ex_change_bus = [37]
action396.line_ex_change_bus = [38]
action396.line_ex_change_bus = [39]
action396.line_or_change_bus = [41]
actions.append(action396)
# ---- END OF ACTION ---
action397 = env.action_space()
action397.gen_change_bus = [11]
action397.line_or_change_bus = [32]
action397.line_or_change_bus = [34]
actions.append(action397)
# ---- END OF ACTION ---
action398 = env.action_space()
action398.gen_change_bus = [5]
action398.gen_change_bus = [8]
action398.load_change_bus = [17]
action398.line_or_change_bus = [22]
action398.line_or_change_bus = [23]
action398.line_or_change_bus = [48]
action398.line_or_change_bus = [49]
actions.append(action398)
# ---- END OF ACTION ---
action399 = env.action_space()
action399.gen_change_bus = [5]
action399.gen_change_bus = [8]
actions.append(action399)
# ---- END OF ACTION ---
action400 = env.action_space()
action400.load_change_bus = [34]
action400.load_change_bus = [35]
actions.append(action400)
# ---- END OF ACTION ---
action401 = env.action_space()
action401.gen_change_bus = [8]
action401.line_or_change_bus = [54]
actions.append(action401)
# ---- END OF ACTION ---
action402 = env.action_space()
action402.gen_change_bus = [12]
action402.load_change_bus = [24]
action402.line_or_change_bus = [32]
action402.line_or_change_bus = [34]
action402.line_or_change_bus = [37]
actions.append(action402)
# ---- END OF ACTION ---
action403 = env.action_space()
action403.gen_change_bus = [11]
action403.gen_change_bus = [12]
action403.gen_change_bus = [13]
action403.load_change_bus = [24]
action403.line_or_change_bus = [34]
action403.line_or_change_bus = [38]
actions.append(action403)
# ---- END OF ACTION ---
action404 = env.action_space()
action404.line_or_change_bus = [38]
actions.append(action404)
# ---- END OF ACTION ---
action405 = env.action_space()
action405.gen_change_bus = [14]
action405.load_change_bus = [27]
action405.line_ex_change_bus = [37]
action405.line_ex_change_bus = [38]
action405.line_ex_change_bus = [39]
action405.line_or_change_bus = [40]
action405.line_ex_change_bus = [56]
actions.append(action405)
# ---- END OF ACTION ---
action406 = env.action_space()
action406.load_change_bus = [33]
action406.load_change_bus = [34]
action406.line_ex_change_bus = [54]
actions.append(action406)
# ---- END OF ACTION ---
action407 = env.action_space()
action407.gen_change_bus = [1]
action407.line_ex_change_bus = [7]
action407.load_change_bus = [8]
actions.append(action407)
# ---- END OF ACTION ---
action408 = env.action_space()
action408.gen_change_bus = [9]
action408.load_change_bus = [22]
action408.line_ex_change_bus = [28]
action408.line_or_change_bus = [29]
action408.line_or_change_bus = [30]
actions.append(action408)
# ---- END OF ACTION ---
action409 = env.action_space()
action409.line_ex_change_bus = [49]
action409.line_or_change_bus = [52]
actions.append(action409)
# ---- END OF ACTION ---
action410 = env.action_space()
action410.load_change_bus = [22]
action410.line_ex_change_bus = [27]
action410.line_ex_change_bus = [28]
action410.line_or_change_bus = [36]
actions.append(action410)
# ---- END OF ACTION ---
action411 = env.action_space()
action411.load_change_bus = [17]
action411.line_ex_change_bus = [19]
action411.line_ex_change_bus = [20]
action411.line_ex_change_bus = [21]
action411.line_or_change_bus = [27]
action411.line_or_change_bus = [54]
actions.append(action411)
# ---- END OF ACTION ---
action412 = env.action_space()
action412.gen_change_bus = [14]
action412.load_change_bus = [27]
action412.line_ex_change_bus = [39]
action412.line_or_change_bus = [40]
action412.line_ex_change_bus = [56]
actions.append(action412)
# ---- END OF ACTION ---
action413 = env.action_space()
action413.line_ex_change_bus = [7]
action413.line_or_change_bus = [8]
actions.append(action413)
# ---- END OF ACTION ---
action414 = env.action_space()
action414.gen_change_bus = [5]
action414.gen_change_bus = [6]
action414.gen_change_bus = [8]
action414.line_ex_change_bus = [18]
action414.line_ex_change_bus = [19]
action414.line_or_change_bus = [27]
action414.line_or_change_bus = [28]
actions.append(action414)
# ---- END OF ACTION ---
action415 = env.action_space()
action415.gen_change_bus = [11]
action415.load_change_bus = [24]
action415.line_or_change_bus = [34]
actions.append(action415)
# ---- END OF ACTION ---
action416 = env.action_space()
action416.gen_change_bus = [5]
action416.gen_change_bus = [8]
action416.load_change_bus = [17]
action416.line_ex_change_bus = [18]
action416.line_ex_change_bus = [19]
action416.line_or_change_bus = [27]
action416.line_or_change_bus = [28]
action416.line_or_change_bus = [54]
actions.append(action416)
# ---- END OF ACTION ---
action417 = env.action_space()
action417.gen_change_bus = [9]
action417.line_ex_change_bus = [27]
action417.line_or_change_bus = [29]
action417.line_or_change_bus = [30]
actions.append(action417)
# ---- END OF ACTION ---
action418 = env.action_space()
action418.load_change_bus = [24]
action418.line_or_change_bus = [32]
action418.line_or_change_bus = [34]
action418.line_or_change_bus = [37]
actions.append(action418)
# ---- END OF ACTION ---
action419 = env.action_space()
action419.line_or_change_bus = [15]
action419.line_or_change_bus = [16]
actions.append(action419)
# ---- END OF ACTION ---
action420 = env.action_space()
action420.gen_change_bus = [9]
action420.load_change_bus = [22]
action420.line_ex_change_bus = [27]
action420.line_or_change_bus = [36]
actions.append(action420)
# ---- END OF ACTION ---
action421 = env.action_space()
action421.gen_change_bus = [14]
action421.line_ex_change_bus = [37]
action421.line_ex_change_bus = [38]
action421.line_or_change_bus = [40]
actions.append(action421)
# ---- END OF ACTION ---
action422 = env.action_space()
action422.load_change_bus = [24]
action422.line_ex_change_bus = [31]
action422.line_or_change_bus = [32]
action422.line_or_change_bus = [34]
actions.append(action422)
# ---- END OF ACTION ---
action423 = env.action_space()
action423.gen_change_bus = [14]
action423.line_ex_change_bus = [37]
actions.append(action423)
# ---- END OF ACTION ---
action424 = env.action_space()
action424.gen_change_bus = [13]
action424.line_ex_change_bus = [31]
action424.line_or_change_bus = [32]
actions.append(action424)
# ---- END OF ACTION ---
action425 = env.action_space()
action425.gen_change_bus = [12]
action425.gen_change_bus = [13]
action425.load_change_bus = [24]
action425.line_or_change_bus = [34]
action425.line_or_change_bus = [37]
action425.line_or_change_bus = [38]
actions.append(action425)
# ---- END OF ACTION ---
action426 = env.action_space()
action426.gen_change_bus = [8]
action426.load_change_bus = [17]
action426.line_ex_change_bus = [18]
action426.line_ex_change_bus = [19]
action426.line_or_change_bus = [22]
action426.line_or_change_bus = [23]
action426.line_or_change_bus = [27]
action426.line_or_change_bus = [28]
action426.line_or_change_bus = [48]
action426.line_or_change_bus = [49]
action426.line_or_change_bus = [54]
actions.append(action426)
# ---- END OF ACTION ---
action427 = env.action_space()
action427.gen_change_bus = [14]
action427.load_change_bus = [27]
action427.line_ex_change_bus = [38]
action427.line_ex_change_bus = [56]
actions.append(action427)
# ---- END OF ACTION ---
action428 = env.action_space()
action428.line_ex_change_bus = [27]
actions.append(action428)
# ---- END OF ACTION ---
action429 = env.action_space()
action429.gen_change_bus = [5]
action429.gen_change_bus = [8]
action429.load_change_bus = [17]
action429.line_ex_change_bus = [18]
action429.line_ex_change_bus = [19]
action429.line_or_change_bus = [22]
action429.line_or_change_bus = [23]
action429.line_or_change_bus = [27]
action429.line_or_change_bus = [28]
action429.line_or_change_bus = [48]
action429.line_or_change_bus = [49]
action429.line_or_change_bus = [54]
actions.append(action429)
# ---- END OF ACTION ---
action430 = env.action_space()
action430.load_change_bus = [31]
action430.line_ex_change_bus = [49]
actions.append(action430)
# ---- END OF ACTION ---
action431 = env.action_space()
action431.line_ex_change_bus = [37]
action431.line_ex_change_bus = [39]
action431.line_or_change_bus = [40]
actions.append(action431)
# ---- END OF ACTION ---
action432 = env.action_space()
action432.line_ex_change_bus = [31]
action432.line_or_change_bus = [32]
action432.line_or_change_bus = [34]
actions.append(action432)
# ---- END OF ACTION ---
action433 = env.action_space()
action433.line_ex_change_bus = [2]
action433.line_or_change_bus = [6]
actions.append(action433)
# ---- END OF ACTION ---
action434 = env.action_space()
action434.line_ex_change_bus = [20]
action434.line_or_change_bus = [27]
actions.append(action434)
# ---- END OF ACTION ---
action435 = env.action_space()
action435.gen_change_bus = [1]
action435.line_ex_change_bus = [7]
action435.load_change_bus = [8]
actions.append(action435)
# ---- END OF ACTION ---
action436 = env.action_space()
action436.gen_change_bus = [5]
action436.gen_change_bus = [6]
action436.gen_change_bus = [7]
action436.gen_change_bus = [8]
action436.line_ex_change_bus = [18]
action436.line_ex_change_bus = [19]
action436.line_ex_change_bus = [20]
action436.line_or_change_bus = [27]
action436.line_or_change_bus = [28]
actions.append(action436)
# ---- END OF ACTION ---
action437 = env.action_space()
action437.gen_change_bus = [11]
action437.gen_change_bus = [12]
action437.line_ex_change_bus = [31]
action437.line_or_change_bus = [32]
action437.line_or_change_bus = [34]
action437.line_or_change_bus = [37]
action437.line_or_change_bus = [38]
actions.append(action437)
# ---- END OF ACTION ---
action438 = env.action_space()
action438.load_change_bus = [27]
action438.line_or_change_bus = [40]
action438.line_or_change_bus = [41]
action438.line_ex_change_bus = [56]
actions.append(action438)
# ---- END OF ACTION ---
action439 = env.action_space()
action439.line_ex_change_bus = [38]
action439.line_ex_change_bus = [39]
actions.append(action439)
# ---- END OF ACTION ---
action440 = env.action_space()
action440.load_change_bus = [22]
actions.append(action440)
# ---- END OF ACTION ---
action441 = env.action_space()
action441.load_change_bus = [17]
action441.line_ex_change_bus = [18]
action441.line_ex_change_bus = [19]
action441.line_ex_change_bus = [20]
action441.line_or_change_bus = [22]
action441.line_or_change_bus = [54]
actions.append(action441)
# ---- END OF ACTION ---
action442 = env.action_space()
action442.line_ex_change_bus = [27]
action442.line_ex_change_bus = [28]
action442.line_or_change_bus = [36]
actions.append(action442)
# ---- END OF ACTION ---
action443 = env.action_space()
action443.gen_change_bus = [8]
action443.load_change_bus = [17]
action443.line_or_change_bus = [22]
action443.line_or_change_bus = [23]
action443.line_or_change_bus = [27]
action443.line_or_change_bus = [48]
action443.line_or_change_bus = [49]
actions.append(action443)
# ---- END OF ACTION ---
action444 = env.action_space()
action444.line_ex_change_bus = [31]
action444.line_or_change_bus = [32]
actions.append(action444)
# ---- END OF ACTION ---
action445 = env.action_space()
action445.gen_change_bus = [13]
action445.load_change_bus = [24]
action445.line_ex_change_bus = [31]
action445.line_or_change_bus = [32]
action445.line_or_change_bus = [37]
action445.line_or_change_bus = [38]
actions.append(action445)
# ---- END OF ACTION ---
action446 = env.action_space()
action446.load_change_bus = [10]
action446.line_or_change_bus = [18]
actions.append(action446)
# ---- END OF ACTION ---
action447 = env.action_space()
action447.gen_change_bus = [10]
action447.load_change_bus = [23]
action447.line_or_change_bus = [39]
actions.append(action447)
# ---- END OF ACTION ---
action448 = env.action_space()
action448.gen_change_bus = [11]
action448.gen_change_bus = [12]
action448.gen_change_bus = [13]
action448.load_change_bus = [24]
action448.line_or_change_bus = [32]
action448.line_or_change_bus = [37]
action448.line_or_change_bus = [38]
actions.append(action448)
# ---- END OF ACTION ---
action449 = env.action_space()
action449.gen_change_bus = [14]
action449.load_change_bus = [27]
action449.line_ex_change_bus = [38]
action449.line_ex_change_bus = [39]
action449.line_or_change_bus = [41]
actions.append(action449)
# ---- END OF ACTION ---
action450 = env.action_space()
action450.line_ex_change_bus = [31]
action450.line_or_change_bus = [34]
action450.line_or_change_bus = [37]
actions.append(action450)
# ---- END OF ACTION ---
action451 = env.action_space()
action451.gen_change_bus = [11]
action451.gen_change_bus = [12]
action451.load_change_bus = [24]
action451.line_or_change_bus = [37]
action451.line_or_change_bus = [38]
actions.append(action451)
# ---- END OF ACTION ---
action452 = env.action_space()
action452.gen_change_bus = [14]
action452.line_ex_change_bus = [39]
action452.line_or_change_bus = [40]
action452.line_or_change_bus = [41]
actions.append(action452)
# ---- END OF ACTION ---
action453 = env.action_space()
action453.line_or_change_bus = [47]
action453.line_or_change_bus = [57]
actions.append(action453)
# ---- END OF ACTION ---
action454 = env.action_space()
action454.gen_change_bus = [11]
action454.gen_change_bus = [12]
action454.line_or_change_bus = [32]
action454.line_or_change_bus = [37]
action454.line_or_change_bus = [38]
actions.append(action454)
# ---- END OF ACTION ---
action455 = env.action_space()
action455.gen_change_bus = [9]
action455.load_change_bus = [22]
action455.line_ex_change_bus = [27]
action455.line_or_change_bus = [30]
actions.append(action455)
# ---- END OF ACTION ---
action456 = env.action_space()
action456.gen_change_bus = [14]
action456.line_ex_change_bus = [37]
action456.line_or_change_bus = [40]
action456.line_or_change_bus = [41]
actions.append(action456)
# ---- END OF ACTION ---
action457 = env.action_space()
action457.line_ex_change_bus = [2]
action457.line_ex_change_bus = [4]
action457.line_or_change_bus = [5]
actions.append(action457)
# ---- END OF ACTION ---
action458 = env.action_space()
action458.line_ex_change_bus = [28]
actions.append(action458)
# ---- END OF ACTION ---
action459 = env.action_space()
action459.gen_change_bus = [8]
action459.line_ex_change_bus = [18]
action459.line_ex_change_bus = [19]
action459.line_or_change_bus = [27]
action459.line_or_change_bus = [28]
actions.append(action459)
# ---- END OF ACTION ---
action460 = env.action_space()
action460.gen_change_bus = [12]
action460.gen_change_bus = [13]
action460.load_change_bus = [24]
action460.line_or_change_bus = [37]
action460.line_or_change_bus = [38]
actions.append(action460)
# ---- END OF ACTION ---
action461 = env.action_space()
action461.gen_change_bus = [4]
action461.load_change_bus = [14]
action461.line_or_change_bus = [16]
actions.append(action461)
# ---- END OF ACTION ---
action462 = env.action_space()
action462.gen_change_bus = [5]
actions.append(action462)
# ---- END OF ACTION ---
action463 = env.action_space()
action463.line_ex_change_bus = [10]
actions.append(action463)
# ---- END OF ACTION ---
action464 = env.action_space()
action464.gen_change_bus = [5]
action464.gen_change_bus = [6]
action464.gen_change_bus = [7]
action464.gen_change_bus = [8]
action464.line_or_change_bus = [22]
action464.line_or_change_bus = [23]
action464.line_or_change_bus = [27]
action464.line_or_change_bus = [48]
action464.line_or_change_bus = [49]
actions.append(action464)
# ---- END OF ACTION ---
action465 = env.action_space()
action465.load_change_bus = [17]
action465.line_ex_change_bus = [19]
action465.line_ex_change_bus = [20]
action465.line_or_change_bus = [22]
action465.line_or_change_bus = [23]
action465.line_or_change_bus = [48]
action465.line_or_change_bus = [49]
actions.append(action465)
# ---- END OF ACTION ---
action466 = env.action_space()
action466.load_change_bus = [24]
action466.line_or_change_bus = [34]
actions.append(action466)
# ---- END OF ACTION ---
action467 = env.action_space()
action467.load_change_bus = [22]
action467.line_ex_change_bus = [27]
action467.line_ex_change_bus = [28]
action467.line_or_change_bus = [29]
action467.line_or_change_bus = [30]
actions.append(action467)
# ---- END OF ACTION ---
action468 = env.action_space()
action468.gen_change_bus = [9]
action468.load_change_bus = [22]
action468.line_ex_change_bus = [27]
action468.line_ex_change_bus = [28]
action468.line_or_change_bus = [29]
actions.append(action468)
# ---- END OF ACTION ---
action469 = env.action_space()
action469.gen_change_bus = [1]
action469.line_ex_change_bus = [7]
action469.line_or_change_bus = [8]
action469.line_or_change_bus = [9]
actions.append(action469)
# ---- END OF ACTION ---
action470 = env.action_space()
action470.gen_change_bus = [5]
action470.gen_change_bus = [6]
action470.gen_change_bus = [7]
action470.gen_change_bus = [8]
action470.line_ex_change_bus = [19]
action470.line_ex_change_bus = [21]
action470.line_or_change_bus = [22]
action470.line_or_change_bus = [23]
action470.line_or_change_bus = [27]
action470.line_or_change_bus = [48]
action470.line_or_change_bus = [49]
action470.line_or_change_bus = [54]
actions.append(action470)
# ---- END OF ACTION ---
action471 = env.action_space()
action471.gen_change_bus = [2]
action471.gen_change_bus = [3]
action471.load_change_bus = [10]
actions.append(action471)
# ---- END OF ACTION ---
action472 = env.action_space()
action472.line_ex_change_bus = [7]
action472.load_change_bus = [8]
actions.append(action472)
# ---- END OF ACTION ---
action473 = env.action_space()
action473.load_change_bus = [8]
actions.append(action473)
# ---- END OF ACTION ---
action474 = env.action_space()
action474.gen_change_bus = [21]
action474.load_change_bus = [34]
action474.load_change_bus = [36]
actions.append(action474)
# ---- END OF ACTION ---
action475 = env.action_space()
action475.line_ex_change_bus = [19]
actions.append(action475)
# ---- END OF ACTION ---
action476 = env.action_space()
action476.gen_change_bus = [7]
action476.gen_change_bus = [8]
action476.line_ex_change_bus = [18]
action476.line_ex_change_bus = [19]
action476.line_or_change_bus = [27]
action476.line_or_change_bus = [28]
actions.append(action476)
# ---- END OF ACTION ---
action477 = env.action_space()
action477.line_ex_change_bus = [37]
action477.line_ex_change_bus = [38]
action477.line_ex_change_bus = [39]
action477.line_or_change_bus = [40]
actions.append(action477)
# ---- END OF ACTION ---
action478 = env.action_space()
action478.gen_change_bus = [14]
action478.line_ex_change_bus = [37]
action478.line_ex_change_bus = [39]
action478.line_or_change_bus = [40]
actions.append(action478)
# ---- END OF ACTION ---
action479 = env.action_space()
action479.gen_change_bus = [13]
action479.line_or_change_bus = [38]
actions.append(action479)
# ---- END OF ACTION ---
action480 = env.action_space()
action480.load_change_bus = [31]
action480.line_ex_change_bus = [58]
actions.append(action480)
# ---- END OF ACTION ---
action481 = env.action_space()
action481.gen_change_bus = [13]
action481.load_change_bus = [24]
action481.line_or_change_bus = [38]
actions.append(action481)
# ---- END OF ACTION ---
action482 = env.action_space()
action482.gen_change_bus = [8]
action482.load_change_bus = [17]
action482.line_or_change_bus = [22]
action482.line_or_change_bus = [23]
action482.line_or_change_bus = [48]
action482.line_or_change_bus = [49]
actions.append(action482)
# ---- END OF ACTION ---
action483 = env.action_space()
action483.line_ex_change_bus = [27]
action483.line_ex_change_bus = [28]
actions.append(action483)
# ---- END OF ACTION ---
action484 = env.action_space()
action484.load_change_bus = [17]
action484.line_ex_change_bus = [19]
action484.line_ex_change_bus = [20]
action484.line_or_change_bus = [22]
action484.line_or_change_bus = [54]
actions.append(action484)
# ---- END OF ACTION ---
action485 = env.action_space()
action485.gen_change_bus = [2]
action485.line_ex_change_bus = [10]
action485.line_or_change_bus = [18]
actions.append(action485)
# ---- END OF ACTION ---
action486 = env.action_space()
action486.load_change_bus = [17]
action486.line_ex_change_bus = [20]
action486.line_ex_change_bus = [21]
action486.line_or_change_bus = [49]
actions.append(action486)
# ---- END OF ACTION ---
action487 = env.action_space()
action487.gen_change_bus = [21]
action487.load_change_bus = [34]
action487.load_change_bus = [35]
action487.load_change_bus = [36]
actions.append(action487)
# ---- END OF ACTION ---
action488 = env.action_space()
action488.line_or_change_bus = [17]
action488.line_or_change_bus = [53]
actions.append(action488)
# ---- END OF ACTION ---
action489 = env.action_space()
action489.load_change_bus = [27]
action489.line_ex_change_bus = [37]
action489.line_ex_change_bus = [39]
action489.line_or_change_bus = [41]
action489.line_ex_change_bus = [56]
actions.append(action489)
# ---- END OF ACTION ---
action490 = env.action_space()
action490.gen_change_bus = [11]
action490.gen_change_bus = [12]
action490.line_ex_change_bus = [31]
action490.line_or_change_bus = [32]
action490.line_or_change_bus = [34]
actions.append(action490)
# ---- END OF ACTION ---
action491 = env.action_space()
action491.gen_change_bus = [14]
action491.load_change_bus = [27]
action491.line_ex_change_bus = [38]
action491.line_ex_change_bus = [39]
action491.line_or_change_bus = [40]
action491.line_ex_change_bus = [56]
actions.append(action491)
# ---- END OF ACTION ---
action492 = env.action_space()
action492.gen_change_bus = [11]
action492.gen_change_bus = [12]
action492.gen_change_bus = [13]
action492.load_change_bus = [24]
action492.line_or_change_bus = [32]
action492.line_or_change_bus = [34]
action492.line_or_change_bus = [38]
actions.append(action492)
# ---- END OF ACTION ---
action493 = env.action_space()
action493.gen_change_bus = [14]
action493.line_ex_change_bus = [39]
action493.line_or_change_bus = [40]
actions.append(action493)
# ---- END OF ACTION ---
action494 = env.action_space()
action494.load_change_bus = [17]
action494.line_ex_change_bus = [18]
action494.line_ex_change_bus = [19]
action494.line_or_change_bus = [22]
action494.line_or_change_bus = [23]
action494.line_or_change_bus = [48]
action494.line_or_change_bus = [49]
action494.line_or_change_bus = [54]
actions.append(action494)
# ---- END OF ACTION ---
action495 = env.action_space()
action495.line_or_change_bus = [32]
action495.line_or_change_bus = [37]
actions.append(action495)
# ---- END OF ACTION ---
action496 = env.action_space()
action496.gen_change_bus = [9]
action496.load_change_bus = [22]
action496.line_ex_change_bus = [27]
action496.line_or_change_bus = [29]
actions.append(action496)
# ---- END OF ACTION ---
action497 = env.action_space()
action497.gen_change_bus = [14]
action497.line_or_change_bus = [40]
actions.append(action497)
# ---- END OF ACTION ---
action498 = env.action_space()
action498.gen_change_bus = [13]
action498.line_or_change_bus = [32]
actions.append(action498)
# ---- END OF ACTION ---
action499 = env.action_space()
action499.gen_change_bus = [14]
action499.load_change_bus = [27]
action499.line_ex_change_bus = [37]
action499.line_ex_change_bus = [38]
action499.line_ex_change_bus = [39]
action499.line_or_change_bus = [40]
action499.line_or_change_bus = [41]
actions.append(action499)
# ---- END OF ACTION ---
action500 = env.action_space()
action500.load_change_bus = [18]
action500.line_or_change_bus = [33]
actions.append(action500)
# ---- END OF ACTION ---
action501 = env.action_space()
action501.gen_change_bus = [5]
action501.gen_change_bus = [6]
action501.gen_change_bus = [7]
action501.gen_change_bus = [8]
action501.line_ex_change_bus = [19]
action501.line_or_change_bus = [27]
action501.line_or_change_bus = [28]
actions.append(action501)
# ---- END OF ACTION ---
action502 = env.action_space()
action502.load_change_bus = [17]
action502.line_ex_change_bus = [19]
action502.line_ex_change_bus = [20]
action502.line_or_change_bus = [22]
action502.line_or_change_bus = [28]
action502.line_or_change_bus = [54]
actions.append(action502)
# ---- END OF ACTION ---
action503 = env.action_space()
action503.load_change_bus = [17]
action503.line_ex_change_bus = [18]
action503.line_ex_change_bus = [19]
action503.line_ex_change_bus = [20]
action503.line_ex_change_bus = [21]
action503.line_or_change_bus = [54]
actions.append(action503)
# ---- END OF ACTION ---
action504 = env.action_space()
action504.gen_change_bus = [9]
action504.load_change_bus = [22]
action504.line_ex_change_bus = [27]
action504.line_ex_change_bus = [28]
action504.line_or_change_bus = [29]
action504.line_or_change_bus = [36]
actions.append(action504)
# ---- END OF ACTION ---
action505 = env.action_space()
action505.gen_change_bus = [0]
action505.load_change_bus = [2]
action505.load_change_bus = [3]
action505.line_or_change_bus = [12]
actions.append(action505)
# ---- END OF ACTION ---
action506 = env.action_space()
action506.gen_change_bus = [9]
action506.line_ex_change_bus = [27]
action506.line_ex_change_bus = [28]
actions.append(action506)
# ---- END OF ACTION ---
action507 = env.action_space()
action507.line_or_change_bus = [18]
action507.line_or_change_bus = [19]
actions.append(action507)
# ---- END OF ACTION ---
action508 = env.action_space()
action508.gen_change_bus = [14]
action508.line_ex_change_bus = [37]
action508.line_ex_change_bus = [38]
actions.append(action508)
# ---- END OF ACTION ---
action509 = env.action_space()
action509.line_or_change_bus = [16]
actions.append(action509)
# ---- END OF ACTION ---
action510 = env.action_space()
action510.gen_change_bus = [11]
action510.gen_change_bus = [12]
action510.load_change_bus = [24]
action510.line_or_change_bus = [32]
actions.append(action510)
# ---- END OF ACTION ---
action511 = env.action_space()
action511.gen_change_bus = [5]
action511.load_change_bus = [17]
actions.append(action511)
# ---- END OF ACTION ---
action512 = env.action_space()
action512.gen_change_bus = [14]
action512.load_change_bus = [27]
action512.line_ex_change_bus = [37]
action512.line_or_change_bus = [40]
action512.line_or_change_bus = [41]
actions.append(action512)
# ---- END OF ACTION ---
action513 = env.action_space()
action513.load_change_bus = [31]
action513.line_ex_change_bus = [49]
action513.line_or_change_bus = [52]
action513.line_ex_change_bus = [58]
actions.append(action513)
# ---- END OF ACTION ---
action514 = env.action_space()
action514.line_or_change_bus = [29]
action514.line_or_change_bus = [30]
actions.append(action514)
# ---- END OF ACTION ---
action515 = env.action_space()
action515.load_change_bus = [34]
action515.line_ex_change_bus = [54]
actions.append(action515)
# ---- END OF ACTION ---
action516 = env.action_space()
action516.load_change_bus = [27]
action516.line_ex_change_bus = [39]
action516.line_or_change_bus = [40]
action516.line_or_change_bus = [41]
actions.append(action516)
# ---- END OF ACTION ---
action517 = env.action_space()
action517.gen_change_bus = [11]
action517.gen_change_bus = [12]
action517.gen_change_bus = [13]
action517.load_change_bus = [24]
action517.line_or_change_bus = [32]
action517.line_or_change_bus = [34]
action517.line_or_change_bus = [37]
actions.append(action517)
# ---- END OF ACTION ---
action518 = env.action_space()
action518.gen_change_bus = [14]
action518.load_change_bus = [27]
action518.line_ex_change_bus = [38]
action518.line_or_change_bus = [40]
action518.line_or_change_bus = [41]
action518.line_ex_change_bus = [56]
actions.append(action518)
# ---- END OF ACTION ---
action519 = env.action_space()
action519.load_change_bus = [17]
action519.line_ex_change_bus = [19]
action519.line_or_change_bus = [22]
action519.line_or_change_bus = [23]
action519.line_or_change_bus = [48]
action519.line_or_change_bus = [49]
actions.append(action519)
# ---- END OF ACTION ---
action520 = env.action_space()
action520.gen_change_bus = [12]
action520.gen_change_bus = [13]
action520.load_change_bus = [24]
action520.line_or_change_bus = [34]
actions.append(action520)
# ---- END OF ACTION ---
action521 = env.action_space()
action521.line_or_change_bus = [14]
actions.append(action521)
# ---- END OF ACTION ---
action522 = env.action_space()
action522.gen_change_bus = [1]
action522.line_ex_change_bus = [7]
action522.line_or_change_bus = [8]
actions.append(action522)
# ---- END OF ACTION ---
action523 = env.action_space()
action523.gen_change_bus = [2]
action523.gen_change_bus = [3]
actions.append(action523)
# ---- END OF ACTION ---
action524 = env.action_space()
action524.gen_change_bus = [14]
action524.load_change_bus = [27]
action524.line_ex_change_bus = [38]
action524.line_ex_change_bus = [39]
action524.line_or_change_bus = [40]
action524.line_or_change_bus = [41]
action524.line_ex_change_bus = [56]
actions.append(action524)
# ---- END OF ACTION ---
action525 = env.action_space()
action525.line_ex_change_bus = [7]
action525.load_change_bus = [8]
action525.line_or_change_bus = [9]
actions.append(action525)
# ---- END OF ACTION ---
action526 = env.action_space()
action526.gen_change_bus = [21]
action526.load_change_bus = [33]
action526.load_change_bus = [34]
action526.load_change_bus = [35]
action526.line_ex_change_bus = [54]
actions.append(action526)
# ---- END OF ACTION ---
action527 = env.action_space()
action527.load_change_bus = [17]
action527.line_ex_change_bus = [19]
action527.line_or_change_bus = [22]
action527.line_or_change_bus = [23]
action527.line_or_change_bus = [27]
action527.line_or_change_bus = [28]
action527.line_or_change_bus = [48]
action527.line_or_change_bus = [49]
actions.append(action527)
# ---- END OF ACTION ---
action528 = env.action_space()
action528.gen_change_bus = [5]
action528.gen_change_bus = [8]
action528.load_change_bus = [17]
action528.line_ex_change_bus = [18]
action528.line_ex_change_bus = [19]
action528.line_or_change_bus = [22]
action528.line_or_change_bus = [23]
action528.line_or_change_bus = [28]
action528.line_or_change_bus = [48]
action528.line_or_change_bus = [49]
actions.append(action528)
# ---- END OF ACTION ---
action529 = env.action_space()
action529.gen_change_bus = [13]
action529.load_change_bus = [24]
action529.line_or_change_bus = [32]
action529.line_or_change_bus = [34]
action529.line_or_change_bus = [38]
actions.append(action529)
# ---- END OF ACTION ---
action530 = env.action_space()
action530.gen_change_bus = [7]
action530.load_change_bus = [17]
action530.line_ex_change_bus = [19]
action530.line_or_change_bus = [22]
action530.line_or_change_bus = [23]
action530.line_or_change_bus = [48]
action530.line_or_change_bus = [49]
action530.line_or_change_bus = [54]
actions.append(action530)
# ---- END OF ACTION ---
action531 = env.action_space()
action531.gen_change_bus = [18]
action531.load_change_bus = [29]
action531.line_ex_change_bus = [44]
action531.line_or_change_bus = [50]
actions.append(action531)
# ---- END OF ACTION ---
action532 = env.action_space()
action532.load_change_bus = [17]
action532.line_or_change_bus = [22]
action532.line_or_change_bus = [23]
action532.line_or_change_bus = [48]
action532.line_or_change_bus = [49]
actions.append(action532)
# ---- END OF ACTION ---
action533 = env.action_space()
action533.gen_change_bus = [9]
action533.load_change_bus = [22]
action533.line_or_change_bus = [36]
actions.append(action533)
# ---- END OF ACTION ---
action534 = env.action_space()
action534.line_ex_change_bus = [10]
action534.line_or_change_bus = [19]
actions.append(action534)
# ---- END OF ACTION ---
action535 = env.action_space()
action535.gen_change_bus = [6]
action535.gen_change_bus = [7]
action535.line_or_change_bus = [28]
actions.append(action535)
# ---- END OF ACTION ---
action536 = env.action_space()
action536.gen_change_bus = [7]
action536.load_change_bus = [17]
action536.line_ex_change_bus = [21]
action536.line_or_change_bus = [22]
action536.line_or_change_bus = [23]
action536.line_or_change_bus = [48]
action536.line_or_change_bus = [49]
actions.append(action536)
# ---- END OF ACTION ---
action537 = env.action_space()
action537.gen_change_bus = [7]
action537.load_change_bus = [17]
actions.append(action537)
# ---- END OF ACTION ---
action538 = env.action_space()
action538.gen_change_bus = [14]
action538.line_ex_change_bus = [56]
actions.append(action538)
# ---- END OF ACTION ---
action539 = env.action_space()
action539.gen_change_bus = [17]
action539.gen_change_bus = [18]
action539.load_change_bus = [29]
action539.line_or_change_bus = [50]
action539.line_or_change_bus = [51]
actions.append(action539)
# ---- END OF ACTION ---
action540 = env.action_space()
action540.gen_change_bus = [1]
action540.load_change_bus = [8]
actions.append(action540)
# ---- END OF ACTION ---
action541 = env.action_space()
action541.load_change_bus = [27]
action541.line_or_change_bus = [40]
actions.append(action541)
# ---- END OF ACTION ---
action542 = env.action_space()
action542.gen_change_bus = [11]
action542.gen_change_bus = [12]
action542.load_change_bus = [24]
action542.line_or_change_bus = [34]
actions.append(action542)
# ---- END OF ACTION ---
action543 = env.action_space()
action543.gen_change_bus = [14]
action543.load_change_bus = [27]
action543.line_ex_change_bus = [39]
action543.line_or_change_bus = [41]
action543.line_ex_change_bus = [56]
actions.append(action543)
# ---- END OF ACTION ---
action544 = env.action_space()
action544.gen_change_bus = [5]
action544.gen_change_bus = [7]
action544.gen_change_bus = [8]
action544.load_change_bus = [17]
action544.line_ex_change_bus = [18]
action544.line_ex_change_bus = [19]
action544.line_ex_change_bus = [20]
action544.line_or_change_bus = [22]
action544.line_or_change_bus = [23]
action544.line_or_change_bus = [27]
action544.line_or_change_bus = [28]
action544.line_or_change_bus = [48]
action544.line_or_change_bus = [49]
action544.line_or_change_bus = [54]
actions.append(action544)
# ---- END OF ACTION ---
action545 = env.action_space()
action545.gen_change_bus = [13]
action545.load_change_bus = [24]
action545.line_ex_change_bus = [31]
actions.append(action545)
# ---- END OF ACTION ---
action546 = env.action_space()
action546.gen_change_bus = [2]
action546.line_ex_change_bus = [10]
actions.append(action546)
# ---- END OF ACTION ---
action547 = env.action_space()
action547.gen_change_bus = [5]
action547.gen_change_bus = [8]
action547.line_ex_change_bus = [18]
action547.line_ex_change_bus = [19]
action547.line_or_change_bus = [22]
action547.line_or_change_bus = [23]
action547.line_or_change_bus = [48]
action547.line_or_change_bus = [49]
action547.line_or_change_bus = [54]
actions.append(action547)
# ---- END OF ACTION ---
action548 = env.action_space()
action548.load_change_bus = [17]
action548.line_ex_change_bus = [19]
action548.line_ex_change_bus = [20]
action548.line_or_change_bus = [27]
action548.line_or_change_bus = [28]
action548.line_or_change_bus = [54]
actions.append(action548)
# ---- END OF ACTION ---
action549 = env.action_space()
action549.load_change_bus = [27]
action549.line_ex_change_bus = [56]
actions.append(action549)
# ---- END OF ACTION ---
action550 = env.action_space()
action550.line_ex_change_bus = [50]
actions.append(action550)
# ---- END OF ACTION ---
action551 = env.action_space()
action551.load_change_bus = [14]
actions.append(action551)
# ---- END OF ACTION ---
action552 = env.action_space()
action552.load_change_bus = [33]
action552.load_change_bus = [35]
action552.line_ex_change_bus = [54]
actions.append(action552)
# ---- END OF ACTION ---
action553 = env.action_space()
action553.gen_change_bus = [13]
action553.line_or_change_bus = [34]
action553.line_or_change_bus = [37]
actions.append(action553)
# ---- END OF ACTION ---
action554 = env.action_space()
action554.gen_change_bus = [13]
action554.load_change_bus = [24]
action554.line_ex_change_bus = [31]
action554.line_or_change_bus = [32]
action554.line_or_change_bus = [34]
action554.line_or_change_bus = [37]
action554.line_or_change_bus = [38]
actions.append(action554)
# ---- END OF ACTION ---
action555 = env.action_space()
action555.gen_change_bus = [9]
action555.load_change_bus = [22]
action555.line_ex_change_bus = [27]
action555.line_or_change_bus = [29]
action555.line_or_change_bus = [36]
actions.append(action555)
# ---- END OF ACTION ---
action556 = env.action_space()
action556.gen_change_bus = [14]
action556.line_ex_change_bus = [37]
action556.line_ex_change_bus = [38]
action556.line_or_change_bus = [40]
action556.line_or_change_bus = [41]
actions.append(action556)
# ---- END OF ACTION ---
action557 = env.action_space()
action557.gen_change_bus = [14]
action557.load_change_bus = [27]
action557.line_or_change_bus = [40]
action557.line_or_change_bus = [41]
action557.line_ex_change_bus = [56]
actions.append(action557)
# ---- END OF ACTION ---
action558 = env.action_space()
action558.gen_change_bus = [17]
action558.gen_change_bus = [18]
action558.line_or_change_bus = [50]
action558.line_or_change_bus = [51]
actions.append(action558)
# ---- END OF ACTION ---
action559 = env.action_space()
action559.gen_change_bus = [20]
action559.line_ex_change_bus = [49]
action559.line_ex_change_bus = [50]
action559.line_or_change_bus = [52]
action559.line_ex_change_bus = [58]
actions.append(action559)
# ---- END OF ACTION ---
action560 = env.action_space()
action560.load_change_bus = [22]
action560.line_ex_change_bus = [27]
action560.line_or_change_bus = [30]
actions.append(action560)
# ---- END OF ACTION ---
action561 = env.action_space()
action561.gen_change_bus = [14]
action561.line_ex_change_bus = [37]
action561.line_ex_change_bus = [38]
action561.line_ex_change_bus = [39]
action561.line_or_change_bus = [40]
action561.line_or_change_bus = [41]
actions.append(action561)
# ---- END OF ACTION ---
action562 = env.action_space()
action562.gen_change_bus = [14]
action562.load_change_bus = [27]
action562.line_ex_change_bus = [39]
action562.line_or_change_bus = [41]
actions.append(action562)
# ---- END OF ACTION ---
action563 = env.action_space()
action563.gen_change_bus = [5]
action563.gen_change_bus = [6]
action563.gen_change_bus = [7]
action563.load_change_bus = [17]
action563.line_ex_change_bus = [18]
action563.line_ex_change_bus = [19]
action563.line_ex_change_bus = [20]
action563.line_or_change_bus = [22]
action563.line_or_change_bus = [23]
action563.line_or_change_bus = [27]
action563.line_or_change_bus = [28]
action563.line_or_change_bus = [48]
action563.line_or_change_bus = [49]
action563.line_or_change_bus = [54]
actions.append(action563)
# ---- END OF ACTION ---
action564 = env.action_space()
action564.gen_change_bus = [17]
action564.line_ex_change_bus = [44]
actions.append(action564)
# ---- END OF ACTION ---
action565 = env.action_space()
action565.load_change_bus = [24]
action565.line_ex_change_bus = [31]
action565.line_or_change_bus = [34]
actions.append(action565)
# ---- END OF ACTION ---
action566 = env.action_space()
action566.load_change_bus = [27]
action566.line_ex_change_bus = [39]
action566.line_or_change_bus = [40]
action566.line_or_change_bus = [41]
action566.line_ex_change_bus = [56]
actions.append(action566)
# ---- END OF ACTION ---
action567 = env.action_space()
action567.line_or_change_bus = [22]
action567.line_or_change_bus = [23]
action567.line_or_change_bus = [27]
action567.line_or_change_bus = [28]
action567.line_or_change_bus = [48]
action567.line_or_change_bus = [49]
actions.append(action567)
# ---- END OF ACTION ---
action568 = env.action_space()
action568.gen_change_bus = [14]
action568.load_change_bus = [27]
action568.line_ex_change_bus = [37]
action568.line_or_change_bus = [41]
action568.line_ex_change_bus = [56]
actions.append(action568)
# ---- END OF ACTION ---
action569 = env.action_space()
action569.line_ex_change_bus = [54]
actions.append(action569)
# ---- END OF ACTION ---
action570 = env.action_space()
action570.gen_change_bus = [5]
action570.gen_change_bus = [6]
action570.gen_change_bus = [7]
action570.gen_change_bus = [8]
action570.load_change_bus = [17]
action570.line_ex_change_bus = [18]
action570.line_ex_change_bus = [19]
action570.line_or_change_bus = [22]
action570.line_or_change_bus = [23]
action570.line_or_change_bus = [27]
action570.line_or_change_bus = [28]
action570.line_or_change_bus = [48]
action570.line_or_change_bus = [49]
action570.line_or_change_bus = [54]
actions.append(action570)
# ---- END OF ACTION ---
action571 = env.action_space()
action571.load_change_bus = [15]
action571.line_or_change_bus = [17]
actions.append(action571)
# ---- END OF ACTION ---
action572 = env.action_space()
action572.gen_change_bus = [5]
action572.gen_change_bus = [8]
action572.load_change_bus = [17]
action572.line_ex_change_bus = [20]
action572.line_ex_change_bus = [21]
action572.line_or_change_bus = [27]
action572.line_or_change_bus = [28]
actions.append(action572)
# ---- END OF ACTION ---
action573 = env.action_space()
action573.gen_change_bus = [5]
action573.gen_change_bus = [7]
action573.gen_change_bus = [8]
action573.line_ex_change_bus = [19]
action573.line_or_change_bus = [28]
action573.line_or_change_bus = [54]
actions.append(action573)
# ---- END OF ACTION ---
action574 = env.action_space()
action574.gen_change_bus = [9]
action574.line_ex_change_bus = [28]
action574.line_or_change_bus = [30]
action574.line_or_change_bus = [36]
actions.append(action574)
# ---- END OF ACTION ---
action575 = env.action_space()
action575.load_change_bus = [23]
action575.line_or_change_bus = [31]
actions.append(action575)
# ---- END OF ACTION ---
action576 = env.action_space()
action576.gen_change_bus = [16]
action576.line_ex_change_bus = [42]
action576.line_or_change_bus = [44]
action576.line_ex_change_bus = [57]
actions.append(action576)
# ---- END OF ACTION ---
action577 = env.action_space()
action577.line_ex_change_bus = [37]
action577.line_or_change_bus = [41]
actions.append(action577)
# ---- END OF ACTION ---
action578 = env.action_space()
action578.load_change_bus = [17]
action578.line_ex_change_bus = [18]
action578.line_ex_change_bus = [19]
action578.line_or_change_bus = [22]
action578.line_or_change_bus = [23]
action578.line_or_change_bus = [27]
action578.line_or_change_bus = [28]
action578.line_or_change_bus = [48]
action578.line_or_change_bus = [49]
action578.line_or_change_bus = [54]
actions.append(action578)
# ---- END OF ACTION ---
action579 = env.action_space()
action579.gen_change_bus = [13]
action579.load_change_bus = [24]
action579.line_or_change_bus = [34]
action579.line_or_change_bus = [37]
actions.append(action579)
# ---- END OF ACTION ---
action580 = env.action_space()
action580.load_change_bus = [33]
action580.load_change_bus = [35]
actions.append(action580)
# ---- END OF ACTION ---
action581 = env.action_space()
action581.gen_change_bus = [17]
action581.gen_change_bus = [18]
action581.load_change_bus = [29]
action581.line_ex_change_bus = [44]
action581.line_or_change_bus = [50]
actions.append(action581)
# ---- END OF ACTION ---
action582 = env.action_space()
action582.gen_change_bus = [21]
action582.load_change_bus = [33]
action582.load_change_bus = [35]
action582.line_ex_change_bus = [54]
actions.append(action582)
# ---- END OF ACTION ---
action583 = env.action_space()
action583.gen_change_bus = [12]
action583.gen_change_bus = [13]
action583.line_or_change_bus = [32]
action583.line_or_change_bus = [34]
action583.line_or_change_bus = [37]
action583.line_or_change_bus = [38]
actions.append(action583)
# ---- END OF ACTION ---
action584 = env.action_space()
action584.gen_change_bus = [5]
action584.gen_change_bus = [7]
action584.gen_change_bus = [8]
action584.load_change_bus = [17]
action584.line_ex_change_bus = [19]
action584.line_or_change_bus = [22]
action584.line_or_change_bus = [23]
action584.line_or_change_bus = [48]
action584.line_or_change_bus = [49]
action584.line_or_change_bus = [54]
actions.append(action584)
# ---- END OF ACTION ---
action585 = env.action_space()
action585.gen_change_bus = [11]
action585.gen_change_bus = [12]
action585.load_change_bus = [24]
action585.line_or_change_bus = [32]
action585.line_or_change_bus = [34]
action585.line_or_change_bus = [38]
actions.append(action585)
# ---- END OF ACTION ---
action586 = env.action_space()
action586.gen_change_bus = [7]
action586.load_change_bus = [17]
action586.line_ex_change_bus = [19]
action586.line_or_change_bus = [22]
action586.line_or_change_bus = [23]
action586.line_or_change_bus = [28]
action586.line_or_change_bus = [48]
action586.line_or_change_bus = [49]
action586.line_or_change_bus = [54]
actions.append(action586)
# ---- END OF ACTION ---
action587 = env.action_space()
action587.load_change_bus = [24]
action587.line_or_change_bus = [38]
actions.append(action587)
# ---- END OF ACTION ---
action588 = env.action_space()
action588.gen_change_bus = [9]
action588.line_ex_change_bus = [28]
action588.line_or_change_bus = [29]
action588.line_or_change_bus = [30]
action588.line_or_change_bus = [36]
actions.append(action588)
# ---- END OF ACTION ---
action589 = env.action_space()
action589.gen_change_bus = [12]
action589.gen_change_bus = [13]
action589.load_change_bus = [24]
action589.line_or_change_bus = [32]
action589.line_or_change_bus = [34]
actions.append(action589)
# ---- END OF ACTION ---
action590 = env.action_space()
action590.gen_change_bus = [5]
action590.gen_change_bus = [6]
action590.gen_change_bus = [8]
action590.line_ex_change_bus = [18]
action590.line_ex_change_bus = [19]
action590.line_or_change_bus = [27]
action590.line_or_change_bus = [28]
action590.line_or_change_bus = [54]
actions.append(action590)
# ---- END OF ACTION ---
action591 = env.action_space()
action591.gen_change_bus = [5]
action591.gen_change_bus = [6]
action591.gen_change_bus = [7]
action591.gen_change_bus = [8]
action591.line_ex_change_bus = [18]
action591.line_ex_change_bus = [19]
action591.line_or_change_bus = [22]
action591.line_or_change_bus = [23]
action591.line_or_change_bus = [27]
action591.line_or_change_bus = [28]
action591.line_or_change_bus = [49]
actions.append(action591)
# ---- END OF ACTION ---
action592 = env.action_space()
action592.gen_change_bus = [12]
action592.gen_change_bus = [13]
action592.load_change_bus = [24]
actions.append(action592)
# ---- END OF ACTION ---
action593 = env.action_space()
action593.gen_change_bus = [7]
action593.gen_change_bus = [8]
action593.load_change_bus = [17]
actions.append(action593)
# ---- END OF ACTION ---
action594 = env.action_space()
action594.load_change_bus = [17]
action594.line_ex_change_bus = [19]
action594.line_ex_change_bus = [20]
action594.line_or_change_bus = [28]
actions.append(action594)
# ---- END OF ACTION ---
action595 = env.action_space()
action595.gen_change_bus = [14]
action595.load_change_bus = [27]
action595.line_ex_change_bus = [39]
action595.line_or_change_bus = [40]
action595.line_or_change_bus = [41]
actions.append(action595)
# ---- END OF ACTION ---
action596 = env.action_space()
action596.gen_change_bus = [8]
action596.load_change_bus = [17]
action596.line_ex_change_bus = [18]
action596.line_ex_change_bus = [19]
action596.line_ex_change_bus = [20]
action596.line_or_change_bus = [22]
action596.line_or_change_bus = [23]
action596.line_or_change_bus = [27]
action596.line_or_change_bus = [28]
action596.line_or_change_bus = [48]
action596.line_or_change_bus = [49]
actions.append(action596)
# ---- END OF ACTION ---
action597 = env.action_space()
action597.gen_change_bus = [9]
action597.line_ex_change_bus = [28]
action597.line_or_change_bus = [29]
action597.line_or_change_bus = [30]
actions.append(action597)
# ---- END OF ACTION ---
action598 = env.action_space()
action598.load_change_bus = [27]
action598.line_ex_change_bus = [37]
action598.line_ex_change_bus = [39]
action598.line_ex_change_bus = [56]
actions.append(action598)
# ---- END OF ACTION ---
action599 = env.action_space()
action599.load_change_bus = [27]
action599.line_ex_change_bus = [39]
actions.append(action599)
# ---- END OF ACTION ---
action600 = env.action_space()
action600.gen_change_bus = [8]
action600.load_change_bus = [17]
action600.line_ex_change_bus = [19]
action600.line_or_change_bus = [22]
action600.line_or_change_bus = [23]
action600.line_or_change_bus = [48]
action600.line_or_change_bus = [49]
action600.line_or_change_bus = [54]
actions.append(action600)
# ---- END OF ACTION ---
action601 = env.action_space()
action601.line_ex_change_bus = [31]
action601.line_or_change_bus = [32]
action601.line_or_change_bus = [38]
actions.append(action601)
# ---- END OF ACTION ---
action602 = env.action_space()
action602.gen_change_bus = [12]
action602.load_change_bus = [24]
actions.append(action602)
# ---- END OF ACTION ---
action603 = env.action_space()
action603.gen_change_bus = [13]
action603.line_or_change_bus = [32]
action603.line_or_change_bus = [34]
action603.line_or_change_bus = [38]
actions.append(action603)
# ---- END OF ACTION ---
action604 = env.action_space()
action604.gen_change_bus = [7]
action604.load_change_bus = [17]
action604.line_ex_change_bus = [18]
action604.line_ex_change_bus = [19]
action604.line_or_change_bus = [22]
action604.line_or_change_bus = [23]
actions.append(action604)
# ---- END OF ACTION ---
action605 = env.action_space()
action605.gen_change_bus = [11]
action605.gen_change_bus = [12]
action605.line_or_change_bus = [32]
action605.line_or_change_bus = [34]
actions.append(action605)
# ---- END OF ACTION ---
action606 = env.action_space()
action606.gen_change_bus = [5]
action606.gen_change_bus = [8]
action606.load_change_bus = [17]
action606.line_ex_change_bus = [18]
action606.line_ex_change_bus = [19]
action606.line_or_change_bus = [27]
action606.line_or_change_bus = [28]
actions.append(action606)
# ---- END OF ACTION ---
action607 = env.action_space()
action607.gen_change_bus = [8]
action607.load_change_bus = [17]
action607.line_ex_change_bus = [19]
action607.line_or_change_bus = [22]
action607.line_or_change_bus = [23]
action607.line_or_change_bus = [49]
action607.line_or_change_bus = [54]
actions.append(action607)
# ---- END OF ACTION ---
action608 = env.action_space()
action608.gen_change_bus = [5]
action608.gen_change_bus = [6]
action608.gen_change_bus = [7]
action608.gen_change_bus = [8]
action608.line_ex_change_bus = [19]
action608.line_or_change_bus = [27]
action608.line_or_change_bus = [28]
action608.line_or_change_bus = [54]
actions.append(action608)
# ---- END OF ACTION ---
action609 = env.action_space()
action609.gen_change_bus = [5]
action609.gen_change_bus = [6]
action609.gen_change_bus = [7]
action609.gen_change_bus = [8]
action609.line_ex_change_bus = [18]
action609.line_ex_change_bus = [19]
action609.line_or_change_bus = [22]
action609.line_or_change_bus = [23]
action609.line_or_change_bus = [27]
actions.append(action609)
# ---- END OF ACTION ---
action610 = env.action_space()
action610.gen_change_bus = [11]
action610.gen_change_bus = [12]
action610.gen_change_bus = [13]
action610.load_change_bus = [24]
action610.line_or_change_bus = [34]
actions.append(action610)
# ---- END OF ACTION ---
action611 = env.action_space()
action611.gen_change_bus = [5]
action611.gen_change_bus = [8]
action611.load_change_bus = [17]
action611.line_ex_change_bus = [19]
action611.line_or_change_bus = [22]
action611.line_or_change_bus = [23]
action611.line_or_change_bus = [49]
action611.line_or_change_bus = [54]
actions.append(action611)
# ---- END OF ACTION ---
action612 = env.action_space()
action612.gen_change_bus = [5]
action612.gen_change_bus = [8]
action612.load_change_bus = [17]
action612.line_ex_change_bus = [18]
action612.line_ex_change_bus = [19]
action612.line_ex_change_bus = [20]
action612.line_ex_change_bus = [21]
action612.line_or_change_bus = [22]
action612.line_or_change_bus = [23]
action612.line_or_change_bus = [27]
action612.line_or_change_bus = [28]
action612.line_or_change_bus = [48]
action612.line_or_change_bus = [49]
action612.line_or_change_bus = [54]
actions.append(action612)
# ---- END OF ACTION ---
action613 = env.action_space()
action613.gen_change_bus = [13]
action613.line_or_change_bus = [34]
action613.line_or_change_bus = [37]
action613.line_or_change_bus = [38]
actions.append(action613)
# ---- END OF ACTION ---
action614 = env.action_space()
action614.gen_change_bus = [9]
action614.load_change_bus = [22]
action614.line_ex_change_bus = [27]
action614.line_ex_change_bus = [28]
action614.line_or_change_bus = [30]
action614.line_or_change_bus = [36]
actions.append(action614)
# ---- END OF ACTION ---
action615 = env.action_space()
action615.gen_change_bus = [5]
action615.gen_change_bus = [8]
action615.load_change_bus = [17]
action615.line_ex_change_bus = [18]
action615.line_ex_change_bus = [19]
action615.line_ex_change_bus = [20]
action615.line_ex_change_bus = [21]
action615.line_or_change_bus = [22]
action615.line_or_change_bus = [23]
action615.line_or_change_bus = [27]
action615.line_or_change_bus = [28]
action615.line_or_change_bus = [48]
action615.line_or_change_bus = [49]
actions.append(action615)
# ---- END OF ACTION ---
action616 = env.action_space()
action616.line_ex_change_bus = [31]
action616.line_or_change_bus = [32]
action616.line_or_change_bus = [34]
action616.line_or_change_bus = [38]
actions.append(action616)
# ---- END OF ACTION ---
action617 = env.action_space()
action617.line_ex_change_bus = [20]
actions.append(action617)
# ---- END OF ACTION ---
action618 = env.action_space()
action618.gen_change_bus = [5]
action618.load_change_bus = [17]
action618.line_ex_change_bus = [19]
action618.line_or_change_bus = [22]
action618.line_or_change_bus = [23]
action618.line_or_change_bus = [28]
action618.line_or_change_bus = [48]
action618.line_or_change_bus = [49]
action618.line_or_change_bus = [54]
actions.append(action618)
# ---- END OF ACTION ---
action619 = env.action_space()
action619.gen_change_bus = [5]
action619.gen_change_bus = [7]
action619.gen_change_bus = [8]
action619.load_change_bus = [17]
action619.line_ex_change_bus = [19]
action619.line_or_change_bus = [22]
action619.line_or_change_bus = [23]
action619.line_or_change_bus = [48]
action619.line_or_change_bus = [49]
actions.append(action619)
# ---- END OF ACTION ---
action620 = env.action_space()
action620.gen_change_bus = [7]
actions.append(action620)
# ---- END OF ACTION ---
action621 = env.action_space()
action621.line_ex_change_bus = [44]
action621.line_or_change_bus = [50]
actions.append(action621)
# ---- END OF ACTION ---
action622 = env.action_space()
action622.gen_change_bus = [17]
action622.load_change_bus = [29]
action622.line_or_change_bus = [51]
actions.append(action622)
# ---- END OF ACTION ---
action623 = env.action_space()
action623.line_ex_change_bus = [31]
action623.line_or_change_bus = [37]
action623.line_or_change_bus = [38]
actions.append(action623)
# ---- END OF ACTION ---
action624 = env.action_space()
action624.line_ex_change_bus = [27]
action624.line_or_change_bus = [29]
action624.line_or_change_bus = [30]
actions.append(action624)
# ---- END OF ACTION ---
action625 = env.action_space()
action625.load_change_bus = [17]
action625.line_ex_change_bus = [18]
action625.line_ex_change_bus = [19]
action625.line_ex_change_bus = [20]
action625.line_ex_change_bus = [21]
action625.line_or_change_bus = [22]
actions.append(action625)
# ---- END OF ACTION ---
action626 = env.action_space()
action626.load_change_bus = [17]
action626.line_ex_change_bus = [19]
action626.line_ex_change_bus = [20]
action626.line_or_change_bus = [22]
action626.line_or_change_bus = [27]
action626.line_or_change_bus = [28]
actions.append(action626)
# ---- END OF ACTION ---
action627 = env.action_space()
action627.line_ex_change_bus = [37]
action627.line_or_change_bus = [40]
action627.line_or_change_bus = [41]
actions.append(action627)
# ---- END OF ACTION ---
action628 = env.action_space()
action628.gen_change_bus = [12]
action628.line_or_change_bus = [32]
action628.line_or_change_bus = [37]
actions.append(action628)
# ---- END OF ACTION ---
action629 = env.action_space()
action629.load_change_bus = [17]
action629.line_ex_change_bus = [20]
action629.line_ex_change_bus = [21]
action629.line_or_change_bus = [22]
action629.line_or_change_bus = [49]
actions.append(action629)
# ---- END OF ACTION ---
action630 = env.action_space()
action630.gen_change_bus = [9]
action630.load_change_bus = [22]
action630.line_ex_change_bus = [28]
action630.line_or_change_bus = [30]
action630.line_or_change_bus = [36]
actions.append(action630)
# ---- END OF ACTION ---
action631 = env.action_space()
action631.gen_change_bus = [14]
action631.line_ex_change_bus = [37]
action631.line_ex_change_bus = [38]
action631.line_or_change_bus = [40]
action631.line_ex_change_bus = [56]
actions.append(action631)
# ---- END OF ACTION ---
action632 = env.action_space()
action632.line_ex_change_bus = [37]
action632.line_ex_change_bus = [38]
action632.line_ex_change_bus = [39]
actions.append(action632)
# ---- END OF ACTION ---
action633 = env.action_space()
action633.gen_change_bus = [5]
action633.gen_change_bus = [6]
action633.gen_change_bus = [7]
action633.gen_change_bus = [8]
action633.line_or_change_bus = [22]
action633.line_or_change_bus = [23]
action633.line_or_change_bus = [54]
actions.append(action633)
# ---- END OF ACTION ---
action634 = env.action_space()
action634.line_ex_change_bus = [28]
action634.line_or_change_bus = [29]
action634.line_or_change_bus = [30]
actions.append(action634)
# ---- END OF ACTION ---
action635 = env.action_space()
action635.gen_change_bus = [14]
action635.load_change_bus = [27]
action635.line_ex_change_bus = [39]
actions.append(action635)
# ---- END OF ACTION ---
action636 = env.action_space()
action636.gen_change_bus = [11]
action636.line_ex_change_bus = [31]
action636.line_or_change_bus = [34]
action636.line_or_change_bus = [37]
action636.line_or_change_bus = [38]
actions.append(action636)
# ---- END OF ACTION ---
action637 = env.action_space()
action637.load_change_bus = [17]
action637.line_ex_change_bus = [20]
action637.line_ex_change_bus = [21]
action637.line_or_change_bus = [27]
action637.line_or_change_bus = [28]
action637.line_or_change_bus = [54]
actions.append(action637)
# ---- END OF ACTION ---
action638 = env.action_space()
action638.load_change_bus = [33]
actions.append(action638)
# ---- END OF ACTION ---
action639 = env.action_space()
action639.line_or_change_bus = [22]
action639.line_or_change_bus = [23]
actions.append(action639)
# ---- END OF ACTION ---
action640 = env.action_space()
action640.gen_change_bus = [11]
action640.gen_change_bus = [12]
action640.line_or_change_bus = [34]
action640.line_or_change_bus = [37]
action640.line_or_change_bus = [38]
actions.append(action640)
# ---- END OF ACTION ---
action641 = env.action_space()
action641.load_change_bus = [17]
action641.line_or_change_bus = [54]
actions.append(action641)
# ---- END OF ACTION ---
action642 = env.action_space()
action642.gen_change_bus = [7]
action642.load_change_bus = [17]
action642.line_or_change_bus = [22]
action642.line_or_change_bus = [23]
action642.line_or_change_bus = [48]
action642.line_or_change_bus = [49]
action642.line_or_change_bus = [54]
actions.append(action642)
# ---- END OF ACTION ---
action643 = env.action_space()
action643.load_change_bus = [22]
action643.line_or_change_bus = [36]
actions.append(action643)
# ---- END OF ACTION ---
action644 = env.action_space()
action644.gen_change_bus = [8]
action644.load_change_bus = [17]
action644.line_ex_change_bus = [18]
action644.line_ex_change_bus = [19]
action644.line_or_change_bus = [22]
action644.line_or_change_bus = [23]
action644.line_or_change_bus = [48]
action644.line_or_change_bus = [49]
action644.line_or_change_bus = [54]
actions.append(action644)
# ---- END OF ACTION ---
action645 = env.action_space()
action645.gen_change_bus = [13]
action645.line_or_change_bus = [32]
action645.line_or_change_bus = [37]
action645.line_or_change_bus = [38]
actions.append(action645)
# ---- END OF ACTION ---
action646 = env.action_space()
action646.gen_change_bus = [13]
action646.line_or_change_bus = [34]
actions.append(action646)
# ---- END OF ACTION ---
action647 = env.action_space()
action647.gen_change_bus = [5]
action647.gen_change_bus = [6]
action647.gen_change_bus = [7]
action647.gen_change_bus = [8]
action647.line_ex_change_bus = [18]
action647.line_ex_change_bus = [19]
action647.line_or_change_bus = [22]
action647.line_or_change_bus = [23]
action647.line_or_change_bus = [54]
actions.append(action647)
# ---- END OF ACTION ---
action648 = env.action_space()
action648.gen_change_bus = [12]
action648.gen_change_bus = [13]
action648.line_or_change_bus = [37]
action648.line_or_change_bus = [38]
actions.append(action648)
# ---- END OF ACTION ---
action649 = env.action_space()
action649.line_ex_change_bus = [7]
action649.line_or_change_bus = [8]
action649.line_or_change_bus = [9]
actions.append(action649)
# ---- END OF ACTION ---
action650 = env.action_space()
action650.gen_change_bus = [14]
action650.load_change_bus = [27]
action650.line_ex_change_bus = [37]
action650.line_ex_change_bus = [38]
action650.line_or_change_bus = [40]
action650.line_or_change_bus = [41]
action650.line_ex_change_bus = [56]
actions.append(action650)
# ---- END OF ACTION ---
action651 = env.action_space()
action651.gen_change_bus = [21]
action651.load_change_bus = [33]
action651.load_change_bus = [34]
action651.load_change_bus = [35]
action651.load_change_bus = [36]
action651.line_ex_change_bus = [54]
actions.append(action651)
# ---- END OF ACTION ---
action652 = env.action_space()
action652.gen_change_bus = [6]
actions.append(action652)
# ---- END OF ACTION ---
action653 = env.action_space()
action653.gen_change_bus = [5]
action653.gen_change_bus = [7]
action653.gen_change_bus = [8]
action653.line_or_change_bus = [54]
actions.append(action653)
# ---- END OF ACTION ---
action654 = env.action_space()
action654.load_change_bus = [19]
action654.line_or_change_bus = [24]
actions.append(action654)
# ---- END OF ACTION ---
action655 = env.action_space()
action655.gen_change_bus = [10]
action655.line_or_change_bus = [39]
actions.append(action655)
# ---- END OF ACTION ---
action656 = env.action_space()
action656.gen_change_bus = [7]
action656.line_ex_change_bus = [19]
action656.line_or_change_bus = [22]
action656.line_or_change_bus = [23]
action656.line_or_change_bus = [48]
action656.line_or_change_bus = [49]
action656.line_or_change_bus = [54]
actions.append(action656)
# ---- END OF ACTION ---
action657 = env.action_space()
action657.line_ex_change_bus = [27]
action657.line_ex_change_bus = [28]
action657.line_or_change_bus = [30]
action657.line_or_change_bus = [36]
actions.append(action657)
# ---- END OF ACTION ---
action658 = env.action_space()
action658.load_change_bus = [34]
actions.append(action658)
# ---- END OF ACTION ---
action659 = env.action_space()
action659.gen_change_bus = [14]
action659.load_change_bus = [27]
action659.line_ex_change_bus = [37]
action659.line_ex_change_bus = [39]
action659.line_or_change_bus = [40]
action659.line_ex_change_bus = [56]
actions.append(action659)
# ---- END OF ACTION ---
action660 = env.action_space()
action660.gen_change_bus = [17]
action660.gen_change_bus = [18]
action660.line_ex_change_bus = [44]
action660.line_or_change_bus = [50]
action660.line_or_change_bus = [51]
actions.append(action660)
# ---- END OF ACTION ---
action661 = env.action_space()
action661.gen_change_bus = [9]
action661.line_ex_change_bus = [28]
action661.line_or_change_bus = [29]
action661.line_or_change_bus = [36]
actions.append(action661)
# ---- END OF ACTION ---
action662 = env.action_space()
action662.line_or_change_bus = [50]
action662.line_or_change_bus = [51]
actions.append(action662)
# ---- END OF ACTION ---
action663 = env.action_space()
action663.gen_change_bus = [11]
action663.load_change_bus = [24]
actions.append(action663)
# ---- END OF ACTION ---
action664 = env.action_space()
action664.load_change_bus = [17]
action664.line_ex_change_bus = [19]
action664.line_ex_change_bus = [20]
action664.line_or_change_bus = [49]
actions.append(action664)
# ---- END OF ACTION ---
action665 = env.action_space()
action665.load_change_bus = [17]
action665.line_or_change_bus = [48]
action665.line_or_change_bus = [49]
actions.append(action665)
# ---- END OF ACTION ---
action666 = env.action_space()
action666.gen_change_bus = [11]
action666.gen_change_bus = [12]
action666.gen_change_bus = [13]
action666.line_ex_change_bus = [31]
action666.line_or_change_bus = [34]
action666.line_or_change_bus = [37]
action666.line_or_change_bus = [38]
actions.append(action666)
# ---- END OF ACTION ---
action667 = env.action_space()
action667.gen_change_bus = [13]
action667.line_or_change_bus = [32]
action667.line_or_change_bus = [34]
actions.append(action667)
# ---- END OF ACTION ---
action668 = env.action_space()
action668.gen_change_bus = [14]
action668.load_change_bus = [27]
action668.line_ex_change_bus = [37]
action668.line_ex_change_bus = [38]
action668.line_or_change_bus = [41]
action668.line_ex_change_bus = [56]
actions.append(action668)
# ---- END OF ACTION ---
action669 = env.action_space()
action669.gen_change_bus = [20]
action669.line_ex_change_bus = [49]
action669.line_ex_change_bus = [50]
actions.append(action669)
# ---- END OF ACTION ---
action670 = env.action_space()
action670.gen_change_bus = [11]
action670.gen_change_bus = [12]
action670.line_or_change_bus = [38]
actions.append(action670)
# ---- END OF ACTION ---
action671 = env.action_space()
action671.line_ex_change_bus = [37]
action671.line_ex_change_bus = [38]
action671.line_ex_change_bus = [56]
actions.append(action671)
# ---- END OF ACTION ---
action672 = env.action_space()
action672.gen_change_bus = [14]
action672.line_ex_change_bus = [37]
action672.line_ex_change_bus = [39]
action672.line_or_change_bus = [40]
action672.line_or_change_bus = [41]
actions.append(action672)
# ---- END OF ACTION ---
action673 = env.action_space()
action673.line_ex_change_bus = [10]
action673.line_or_change_bus = [18]
action673.line_or_change_bus = [19]
actions.append(action673)
# ---- END OF ACTION ---
action674 = env.action_space()
action674.load_change_bus = [17]
action674.line_ex_change_bus = [18]
action674.line_ex_change_bus = [19]
action674.line_or_change_bus = [22]
action674.line_or_change_bus = [23]
action674.line_or_change_bus = [48]
action674.line_or_change_bus = [49]
actions.append(action674)
# ---- END OF ACTION ---
action675 = env.action_space()
action675.gen_change_bus = [21]
action675.load_change_bus = [36]
action675.line_ex_change_bus = [54]
actions.append(action675)
# ---- END OF ACTION ---
action676 = env.action_space()
action676.line_or_change_bus = [52]
actions.append(action676)
# ---- END OF ACTION ---
action677 = env.action_space()
action677.gen_change_bus = [9]
action677.line_or_change_bus = [30]
actions.append(action677)
# ---- END OF ACTION ---
action678 = env.action_space()
action678.line_or_change_bus = [43]
actions.append(action678)
# ---- END OF ACTION ---
action679 = env.action_space()
action679.gen_change_bus = [20]
action679.load_change_bus = [31]
action679.line_ex_change_bus = [49]
action679.line_ex_change_bus = [58]
actions.append(action679)
# ---- END OF ACTION ---
action680 = env.action_space()
action680.line_ex_change_bus = [37]
action680.line_ex_change_bus = [38]
action680.line_ex_change_bus = [39]
action680.line_or_change_bus = [40]
action680.line_or_change_bus = [41]
action680.line_ex_change_bus = [56]
actions.append(action680)
# ---- END OF ACTION ---
action681 = env.action_space()
action681.gen_change_bus = [5]
action681.line_ex_change_bus = [20]
actions.append(action681)
# ---- END OF ACTION ---
action682 = env.action_space()
action682.load_change_bus = [17]
action682.line_ex_change_bus = [18]
action682.line_ex_change_bus = [19]
action682.line_ex_change_bus = [20]
action682.line_or_change_bus = [27]
action682.line_or_change_bus = [54]
actions.append(action682)
# ---- END OF ACTION ---
action683 = env.action_space()
action683.gen_change_bus = [0]
action683.load_change_bus = [3]
action683.line_or_change_bus = [12]
actions.append(action683)
# ---- END OF ACTION ---
action684 = env.action_space()
action684.gen_change_bus = [18]
action684.load_change_bus = [29]
action684.line_or_change_bus = [51]
actions.append(action684)
# ---- END OF ACTION ---
action685 = env.action_space()
action685.gen_change_bus = [21]
action685.line_ex_change_bus = [54]
actions.append(action685)
# ---- END OF ACTION ---
action686 = env.action_space()
action686.load_change_bus = [17]
action686.line_ex_change_bus = [19]
action686.line_ex_change_bus = [20]
action686.line_or_change_bus = [27]
actions.append(action686)
# ---- END OF ACTION ---
action687 = env.action_space()
action687.line_ex_change_bus = [7]
actions.append(action687)
# ---- END OF ACTION ---
action688 = env.action_space()
action688.gen_change_bus = [13]
action688.load_change_bus = [24]
action688.line_or_change_bus = [32]
action688.line_or_change_bus = [37]
actions.append(action688)
# ---- END OF ACTION ---
action689 = env.action_space()
action689.load_change_bus = [24]
action689.line_ex_change_bus = [31]
actions.append(action689)
# ---- END OF ACTION ---
action690 = env.action_space()
action690.gen_change_bus = [13]
action690.line_ex_change_bus = [31]
actions.append(action690)
# ---- END OF ACTION ---
action691 = env.action_space()
action691.gen_change_bus = [21]
action691.load_change_bus = [33]
action691.load_change_bus = [34]
action691.load_change_bus = [36]
actions.append(action691)
# ---- END OF ACTION ---
action692 = env.action_space()
action692.gen_change_bus = [2]
action692.line_ex_change_bus = [10]
action692.line_or_change_bus = [18]
action692.line_or_change_bus = [19]
actions.append(action692)
# ---- END OF ACTION ---
action693 = env.action_space()
action693.line_ex_change_bus = [28]
action693.line_or_change_bus = [29]
action693.line_or_change_bus = [36]
actions.append(action693)
# ---- END OF ACTION ---
action694 = env.action_space()
action694.gen_change_bus = [9]
action694.load_change_bus = [22]
action694.line_or_change_bus = [30]
action694.line_or_change_bus = [36]
actions.append(action694)
# ---- END OF ACTION ---
action695 = env.action_space()
action695.gen_change_bus = [11]
action695.gen_change_bus = [13]
action695.line_or_change_bus = [32]
action695.line_or_change_bus = [34]
action695.line_or_change_bus = [37]
action695.line_or_change_bus = [38]
actions.append(action695)
# ---- END OF ACTION ---
action696 = env.action_space()
action696.gen_change_bus = [5]
action696.line_ex_change_bus = [19]
action696.line_or_change_bus = [28]
action696.line_or_change_bus = [54]
actions.append(action696)
# ---- END OF ACTION ---
action697 = env.action_space()
action697.load_change_bus = [22]
action697.line_or_change_bus = [29]
action697.line_or_change_bus = [36]
actions.append(action697)
# ---- END OF ACTION ---
action698 = env.action_space()
action698.gen_change_bus = [8]
action698.line_ex_change_bus = [20]
actions.append(action698)
# ---- END OF ACTION ---
action699 = env.action_space()
action699.gen_change_bus = [0]
action699.load_change_bus = [3]
actions.append(action699)
# ---- END OF ACTION ---
action700 = env.action_space()
action700.gen_change_bus = [5]
action700.gen_change_bus = [6]
action700.gen_change_bus = [7]
action700.load_change_bus = [17]
action700.line_or_change_bus = [22]
action700.line_or_change_bus = [23]
action700.line_or_change_bus = [27]
action700.line_or_change_bus = [28]
action700.line_or_change_bus = [48]
action700.line_or_change_bus = [49]
actions.append(action700)
# ---- END OF ACTION ---
action701 = env.action_space()
action701.gen_change_bus = [5]
action701.line_ex_change_bus = [18]
action701.line_ex_change_bus = [19]
action701.line_or_change_bus = [27]
action701.line_or_change_bus = [28]
actions.append(action701)
# ---- END OF ACTION ---
action702 = env.action_space()
action702.line_ex_change_bus = [20]
action702.line_ex_change_bus = [21]
actions.append(action702)
# ---- END OF ACTION ---
action703 = env.action_space()
action703.gen_change_bus = [8]
action703.load_change_bus = [17]
action703.line_ex_change_bus = [19]
action703.line_ex_change_bus = [20]
action703.line_or_change_bus = [22]
action703.line_or_change_bus = [23]
action703.line_or_change_bus = [28]
action703.line_or_change_bus = [48]
action703.line_or_change_bus = [49]
action703.line_or_change_bus = [54]
actions.append(action703)
# ---- END OF ACTION ---
action704 = env.action_space()
action704.gen_change_bus = [13]
action704.load_change_bus = [24]
action704.line_ex_change_bus = [31]
action704.line_or_change_bus = [32]
action704.line_or_change_bus = [38]
actions.append(action704)
# ---- END OF ACTION ---
action705 = env.action_space()
action705.gen_change_bus = [7]
action705.gen_change_bus = [8]
action705.line_or_change_bus = [28]
actions.append(action705)
# ---- END OF ACTION ---
action706 = env.action_space()
action706.gen_change_bus = [9]
action706.line_or_change_bus = [30]
action706.line_or_change_bus = [36]
actions.append(action706)
# ---- END OF ACTION ---
action707 = env.action_space()
action707.gen_change_bus = [5]
action707.gen_change_bus = [8]
action707.line_or_change_bus = [22]
action707.line_or_change_bus = [23]
action707.line_or_change_bus = [49]
actions.append(action707)
# ---- END OF ACTION ---
action708 = env.action_space()
action708.gen_change_bus = [11]
action708.load_change_bus = [24]
action708.line_or_change_bus = [32]
action708.line_or_change_bus = [34]
action708.line_or_change_bus = [37]
actions.append(action708)
# ---- END OF ACTION ---
action709 = env.action_space()
action709.gen_change_bus = [14]
action709.line_ex_change_bus = [38]
action709.line_or_change_bus = [41]
actions.append(action709)
# ---- END OF ACTION ---
action710 = env.action_space()
action710.line_or_change_bus = [22]
action710.line_or_change_bus = [27]
actions.append(action710)
# ---- END OF ACTION ---
action711 = env.action_space()
action711.gen_change_bus = [11]
action711.gen_change_bus = [12]
action711.load_change_bus = [24]
action711.line_or_change_bus = [32]
action711.line_or_change_bus = [37]
action711.line_or_change_bus = [38]
actions.append(action711)
# ---- END OF ACTION ---
action712 = env.action_space()
action712.line_ex_change_bus = [18]
actions.append(action712)
# ---- END OF ACTION ---
action713 = env.action_space()
action713.load_change_bus = [29]
actions.append(action713)
# ---- END OF ACTION ---
action714 = env.action_space()
action714.gen_change_bus = [5]
action714.gen_change_bus = [8]
action714.load_change_bus = [17]
action714.line_or_change_bus = [54]
actions.append(action714)
# ---- END OF ACTION ---
action715 = env.action_space()
action715.load_change_bus = [21]
action715.line_or_change_bus = [26]
actions.append(action715)
# ---- END OF ACTION ---
action716 = env.action_space()
action716.gen_change_bus = [5]
action716.gen_change_bus = [6]
action716.gen_change_bus = [7]
action716.gen_change_bus = [8]
action716.line_ex_change_bus = [18]
action716.line_ex_change_bus = [19]
action716.line_ex_change_bus = [21]
action716.line_or_change_bus = [22]
action716.line_or_change_bus = [23]
action716.line_or_change_bus = [27]
action716.line_or_change_bus = [28]
action716.line_or_change_bus = [49]
action716.line_or_change_bus = [54]
actions.append(action716)
# ---- END OF ACTION ---
action717 = env.action_space()
action717.gen_change_bus = [11]
action717.gen_change_bus = [13]
action717.line_or_change_bus = [37]
actions.append(action717)
# ---- END OF ACTION ---
action718 = env.action_space()
action718.load_change_bus = [17]
action718.line_ex_change_bus = [20]
action718.line_or_change_bus = [22]
action718.line_or_change_bus = [48]
action718.line_or_change_bus = [49]
actions.append(action718)
# ---- END OF ACTION ---
action719 = env.action_space()
action719.gen_change_bus = [14]
action719.line_ex_change_bus = [37]
action719.line_ex_change_bus = [38]
action719.line_ex_change_bus = [39]
action719.line_or_change_bus = [40]
actions.append(action719)
# ---- END OF ACTION ---
action720 = env.action_space()
action720.gen_change_bus = [11]
action720.line_or_change_bus = [32]
action720.line_or_change_bus = [34]
action720.line_or_change_bus = [37]
action720.line_or_change_bus = [38]
actions.append(action720)
# ---- END OF ACTION ---
action721 = env.action_space()
action721.line_ex_change_bus = [12]
actions.append(action721)
# ---- END OF ACTION ---
action722 = env.action_space()
action722.load_change_bus = [27]
action722.line_ex_change_bus = [37]
action722.line_ex_change_bus = [38]
action722.line_ex_change_bus = [39]
action722.line_or_change_bus = [41]
action722.line_ex_change_bus = [56]
actions.append(action722)
# ---- END OF ACTION ---
action723 = env.action_space()
action723.load_change_bus = [27]
action723.line_ex_change_bus = [37]
action723.line_or_change_bus = [40]
actions.append(action723)
# ---- END OF ACTION ---
action724 = env.action_space()
action724.line_ex_change_bus = [18]
action724.line_ex_change_bus = [19]
actions.append(action724)
# ---- END OF ACTION ---
action725 = env.action_space()
action725.line_ex_change_bus = [37]
action725.line_ex_change_bus = [39]
action725.line_or_change_bus = [40]
action725.line_or_change_bus = [41]
action725.line_ex_change_bus = [56]
actions.append(action725)
# ---- END OF ACTION ---
action726 = env.action_space()
action726.gen_change_bus = [5]
action726.load_change_bus = [17]
action726.line_or_change_bus = [22]
action726.line_or_change_bus = [23]
action726.line_or_change_bus = [28]
action726.line_or_change_bus = [48]
action726.line_or_change_bus = [49]
actions.append(action726)
# ---- END OF ACTION ---
action727 = env.action_space()
action727.gen_change_bus = [14]
action727.line_ex_change_bus = [38]
action727.line_ex_change_bus = [39]
actions.append(action727)
# ---- END OF ACTION ---
action728 = env.action_space()
action728.gen_change_bus = [6]
action728.gen_change_bus = [7]
action728.gen_change_bus = [8]
action728.line_ex_change_bus = [18]
action728.line_ex_change_bus = [19]
action728.line_or_change_bus = [27]
actions.append(action728)
# ---- END OF ACTION ---
action729 = env.action_space()
action729.gen_change_bus = [5]
action729.load_change_bus = [17]
action729.line_ex_change_bus = [18]
action729.line_ex_change_bus = [19]
action729.line_or_change_bus = [22]
action729.line_or_change_bus = [23]
action729.line_or_change_bus = [27]
action729.line_or_change_bus = [28]
action729.line_or_change_bus = [48]
action729.line_or_change_bus = [49]
action729.line_or_change_bus = [54]
actions.append(action729)
# ---- END OF ACTION ---
action730 = env.action_space()
action730.gen_change_bus = [5]
action730.gen_change_bus = [6]
action730.gen_change_bus = [7]
action730.gen_change_bus = [8]
action730.load_change_bus = [17]
action730.line_ex_change_bus = [19]
action730.line_or_change_bus = [22]
action730.line_or_change_bus = [23]
action730.line_or_change_bus = [27]
action730.line_or_change_bus = [28]
action730.line_or_change_bus = [48]
action730.line_or_change_bus = [49]
actions.append(action730)
# ---- END OF ACTION ---
action731 = env.action_space()
action731.gen_change_bus = [9]
action731.line_ex_change_bus = [27]
actions.append(action731)
# ---- END OF ACTION ---
action732 = env.action_space()
action732.gen_change_bus = [14]
action732.load_change_bus = [27]
action732.line_ex_change_bus = [37]
action732.line_ex_change_bus = [56]
actions.append(action732)
# ---- END OF ACTION ---
action733 = env.action_space()
action733.gen_change_bus = [14]
action733.load_change_bus = [27]
action733.line_ex_change_bus = [38]
action733.line_or_change_bus = [40]
actions.append(action733)
# ---- END OF ACTION ---
action734 = env.action_space()
action734.gen_change_bus = [11]
action734.gen_change_bus = [12]
action734.gen_change_bus = [13]
action734.load_change_bus = [24]
action734.line_ex_change_bus = [31]
action734.line_or_change_bus = [32]
action734.line_or_change_bus = [34]
action734.line_or_change_bus = [38]
actions.append(action734)
# ---- END OF ACTION ---
action735 = env.action_space()
action735.gen_change_bus = [7]
action735.gen_change_bus = [8]
action735.line_ex_change_bus = [20]
action735.line_or_change_bus = [28]
actions.append(action735)
# ---- END OF ACTION ---
action736 = env.action_space()
action736.load_change_bus = [17]
action736.line_or_change_bus = [22]
action736.line_or_change_bus = [23]
action736.line_or_change_bus = [27]
action736.line_or_change_bus = [28]
action736.line_or_change_bus = [48]
action736.line_or_change_bus = [49]
action736.line_or_change_bus = [54]
actions.append(action736)
# ---- END OF ACTION ---
action737 = env.action_space()
action737.gen_change_bus = [20]
action737.load_change_bus = [31]
action737.line_ex_change_bus = [49]
actions.append(action737)
# ---- END OF ACTION ---
action738 = env.action_space()
action738.gen_change_bus = [5]
action738.gen_change_bus = [8]
action738.load_change_bus = [17]
action738.line_ex_change_bus = [18]
action738.line_ex_change_bus = [19]
action738.line_ex_change_bus = [20]
action738.line_or_change_bus = [22]
action738.line_or_change_bus = [23]
action738.line_or_change_bus = [27]
action738.line_or_change_bus = [28]
action738.line_or_change_bus = [48]
action738.line_or_change_bus = [49]
action738.line_or_change_bus = [54]
actions.append(action738)
# ---- END OF ACTION ---
action739 = env.action_space()
action739.gen_change_bus = [14]
action739.load_change_bus = [27]
action739.line_ex_change_bus = [39]
action739.line_or_change_bus = [40]
action739.line_or_change_bus = [41]
action739.line_ex_change_bus = [56]
actions.append(action739)
# ---- END OF ACTION ---
action740 = env.action_space()
action740.load_change_bus = [24]
action740.line_ex_change_bus = [31]
action740.line_or_change_bus = [37]
action740.line_or_change_bus = [38]
actions.append(action740)
# ---- END OF ACTION ---
action741 = env.action_space()
action741.line_ex_change_bus = [19]
action741.line_or_change_bus = [27]
action741.line_or_change_bus = [28]
actions.append(action741)
# ---- END OF ACTION ---
action742 = env.action_space()
action742.gen_change_bus = [9]
action742.line_ex_change_bus = [27]
action742.line_or_change_bus = [30]
actions.append(action742)
# ---- END OF ACTION ---
action743 = env.action_space()
action743.gen_change_bus = [8]
action743.load_change_bus = [17]
action743.line_or_change_bus = [22]
action743.line_or_change_bus = [23]
action743.line_or_change_bus = [27]
action743.line_or_change_bus = [28]
action743.line_or_change_bus = [48]
action743.line_or_change_bus = [49]
actions.append(action743)
# ---- END OF ACTION ---
action744 = env.action_space()
action744.load_change_bus = [3]
actions.append(action744)
# ---- END OF ACTION ---
action745 = env.action_space()
action745.load_change_bus = [27]
action745.line_ex_change_bus = [37]
action745.line_ex_change_bus = [38]
actions.append(action745)
# ---- END OF ACTION ---
action746 = env.action_space()
action746.gen_change_bus = [5]
action746.gen_change_bus = [6]
action746.gen_change_bus = [7]
action746.gen_change_bus = [8]
action746.line_ex_change_bus = [21]
action746.line_or_change_bus = [22]
action746.line_or_change_bus = [23]
action746.line_or_change_bus = [28]
action746.line_or_change_bus = [48]
action746.line_or_change_bus = [49]
action746.line_or_change_bus = [54]
actions.append(action746)
# ---- END OF ACTION ---
action747 = env.action_space()
action747.gen_change_bus = [7]
action747.line_ex_change_bus = [19]
actions.append(action747)
# ---- END OF ACTION ---
action748 = env.action_space()
action748.gen_change_bus = [5]
action748.gen_change_bus = [7]
action748.load_change_bus = [17]
action748.line_ex_change_bus = [19]
action748.line_or_change_bus = [22]
action748.line_or_change_bus = [23]
action748.line_or_change_bus = [48]
action748.line_or_change_bus = [49]
action748.line_or_change_bus = [54]
actions.append(action748)
# ---- END OF ACTION ---
action749 = env.action_space()
action749.gen_change_bus = [11]
action749.gen_change_bus = [12]
action749.gen_change_bus = [13]
action749.line_or_change_bus = [32]
actions.append(action749)
# ---- END OF ACTION ---
action750 = env.action_space()
action750.load_change_bus = [17]
action750.line_ex_change_bus = [19]
action750.line_or_change_bus = [22]
action750.line_or_change_bus = [23]
action750.line_or_change_bus = [27]
action750.line_or_change_bus = [28]
action750.line_or_change_bus = [49]
actions.append(action750)
# ---- END OF ACTION ---
action751 = env.action_space()
action751.gen_change_bus = [6]
action751.gen_change_bus = [7]
action751.gen_change_bus = [8]
action751.load_change_bus = [17]
action751.line_ex_change_bus = [19]
action751.line_or_change_bus = [22]
action751.line_or_change_bus = [23]
action751.line_or_change_bus = [49]
action751.line_or_change_bus = [54]
actions.append(action751)
# ---- END OF ACTION ---
action752 = env.action_space()
action752.gen_change_bus = [8]
action752.line_ex_change_bus = [19]
action752.line_or_change_bus = [22]
action752.line_or_change_bus = [23]
action752.line_or_change_bus = [48]
action752.line_or_change_bus = [49]
actions.append(action752)
# ---- END OF ACTION ---
action753 = env.action_space()
action753.gen_change_bus = [5]
action753.gen_change_bus = [7]
action753.gen_change_bus = [8]
action753.line_ex_change_bus = [19]
action753.line_ex_change_bus = [20]
actions.append(action753)
# ---- END OF ACTION ---
action754 = env.action_space()
action754.gen_change_bus = [12]
action754.gen_change_bus = [13]
action754.line_or_change_bus = [37]
actions.append(action754)
# ---- END OF ACTION ---
action755 = env.action_space()
action755.gen_change_bus = [20]
action755.line_ex_change_bus = [49]
actions.append(action755)
# ---- END OF ACTION ---
action756 = env.action_space()
action756.gen_change_bus = [5]
action756.gen_change_bus = [8]
action756.load_change_bus = [17]
action756.line_ex_change_bus = [19]
action756.line_or_change_bus = [22]
action756.line_or_change_bus = [23]
action756.line_or_change_bus = [28]
action756.line_or_change_bus = [49]
action756.line_or_change_bus = [54]
actions.append(action756)
# ---- END OF ACTION ---
action757 = env.action_space()
action757.gen_change_bus = [5]
action757.line_or_change_bus = [28]
actions.append(action757)
# ---- END OF ACTION ---
action758 = env.action_space()
action758.line_ex_change_bus = [35]
actions.append(action758)
# ---- END OF ACTION ---
action759 = env.action_space()
action759.load_change_bus = [17]
action759.line_ex_change_bus = [18]
action759.line_ex_change_bus = [19]
action759.line_or_change_bus = [22]
action759.line_or_change_bus = [23]
action759.line_or_change_bus = [27]
action759.line_or_change_bus = [28]
action759.line_or_change_bus = [48]
action759.line_or_change_bus = [49]
actions.append(action759)
# ---- END OF ACTION ---
action760 = env.action_space()
action760.gen_change_bus = [5]
action760.gen_change_bus = [7]
action760.gen_change_bus = [8]
action760.load_change_bus = [17]
action760.line_or_change_bus = [22]
action760.line_or_change_bus = [23]
action760.line_or_change_bus = [28]
action760.line_or_change_bus = [48]
action760.line_or_change_bus = [49]
actions.append(action760)
# ---- END OF ACTION ---
action761 = env.action_space()
action761.gen_change_bus = [17]
action761.load_change_bus = [29]
action761.line_or_change_bus = [50]
actions.append(action761)
# ---- END OF ACTION ---
action762 = env.action_space()
action762.gen_change_bus = [8]
action762.line_ex_change_bus = [18]
action762.line_ex_change_bus = [19]
action762.line_or_change_bus = [22]
action762.line_or_change_bus = [23]
action762.line_or_change_bus = [27]
action762.line_or_change_bus = [28]
action762.line_or_change_bus = [48]
action762.line_or_change_bus = [49]
actions.append(action762)
# ---- END OF ACTION ---
action763 = env.action_space()
action763.line_ex_change_bus = [27]
action763.line_ex_change_bus = [28]
action763.line_or_change_bus = [29]
action763.line_or_change_bus = [30]
action763.line_or_change_bus = [36]
actions.append(action763)
# ---- END OF ACTION ---
action764 = env.action_space()
action764.load_change_bus = [27]
action764.line_ex_change_bus = [37]
action764.line_ex_change_bus = [38]
action764.line_or_change_bus = [41]
action764.line_ex_change_bus = [56]
actions.append(action764)
# ---- END OF ACTION ---
action765 = env.action_space()
action765.gen_change_bus = [8]
action765.line_ex_change_bus = [18]
action765.line_ex_change_bus = [19]
action765.line_ex_change_bus = [20]
action765.line_or_change_bus = [48]
action765.line_or_change_bus = [49]
actions.append(action765)
# ---- END OF ACTION ---
action766 = env.action_space()
action766.gen_change_bus = [7]
action766.load_change_bus = [17]
action766.line_ex_change_bus = [19]
action766.line_ex_change_bus = [20]
action766.line_or_change_bus = [22]
action766.line_or_change_bus = [23]
action766.line_or_change_bus = [27]
action766.line_or_change_bus = [28]
action766.line_or_change_bus = [48]
action766.line_or_change_bus = [49]
actions.append(action766)
# ---- END OF ACTION ---
action767 = env.action_space()
action767.load_change_bus = [24]
action767.line_or_change_bus = [32]
action767.line_or_change_bus = [34]
action767.line_or_change_bus = [38]
actions.append(action767)
# ---- END OF ACTION ---
action768 = env.action_space()
action768.gen_change_bus = [11]
action768.gen_change_bus = [13]
action768.load_change_bus = [24]
action768.line_or_change_bus = [38]
actions.append(action768)
# ---- END OF ACTION ---
action769 = env.action_space()
action769.gen_change_bus = [21]
action769.load_change_bus = [33]
action769.load_change_bus = [34]
action769.load_change_bus = [35]
action769.load_change_bus = [36]
actions.append(action769)
# ---- END OF ACTION ---
action770 = env.action_space()
action770.gen_change_bus = [7]
action770.line_ex_change_bus = [18]
action770.line_ex_change_bus = [19]
action770.line_or_change_bus = [22]
action770.line_or_change_bus = [23]
action770.line_or_change_bus = [49]
action770.line_or_change_bus = [54]
actions.append(action770)
# ---- END OF ACTION ---
action771 = env.action_space()
action771.gen_change_bus = [5]
action771.gen_change_bus = [7]
action771.gen_change_bus = [8]
action771.load_change_bus = [17]
action771.line_ex_change_bus = [19]
action771.line_or_change_bus = [22]
action771.line_or_change_bus = [23]
action771.line_or_change_bus = [49]
action771.line_or_change_bus = [54]
actions.append(action771)
# ---- END OF ACTION ---
action772 = env.action_space()
action772.load_change_bus = [31]
action772.line_ex_change_bus = [50]
actions.append(action772)
# ---- END OF ACTION ---
action773 = env.action_space()
action773.line_ex_change_bus = [21]
action773.line_or_change_bus = [27]
actions.append(action773)
# ---- END OF ACTION ---
action774 = env.action_space()
action774.gen_change_bus = [6]
action774.gen_change_bus = [7]
actions.append(action774)
# ---- END OF ACTION ---
action775 = env.action_space()
action775.gen_change_bus = [7]
action775.load_change_bus = [17]
action775.line_ex_change_bus = [18]
action775.line_ex_change_bus = [19]
action775.line_or_change_bus = [22]
action775.line_or_change_bus = [23]
action775.line_or_change_bus = [27]
action775.line_or_change_bus = [28]
action775.line_or_change_bus = [48]
action775.line_or_change_bus = [49]
actions.append(action775)
# ---- END OF ACTION ---
action776 = env.action_space()
action776.gen_change_bus = [17]
action776.gen_change_bus = [18]
action776.load_change_bus = [29]
action776.line_or_change_bus = [50]
actions.append(action776)
# ---- END OF ACTION ---
action777 = env.action_space()
action777.gen_change_bus = [11]
action777.line_or_change_bus = [32]
action777.line_or_change_bus = [38]
actions.append(action777)
# ---- END OF ACTION ---
action778 = env.action_space()
action778.gen_change_bus = [8]
action778.line_or_change_bus = [22]
action778.line_or_change_bus = [23]
actions.append(action778)
# ---- END OF ACTION ---
action779 = env.action_space()
action779.load_change_bus = [17]
action779.line_or_change_bus = [28]
actions.append(action779)
# ---- END OF ACTION ---
action780 = env.action_space()
action780.gen_change_bus = [14]
action780.load_change_bus = [27]
action780.line_ex_change_bus = [37]
action780.line_ex_change_bus = [39]
action780.line_or_change_bus = [41]
action780.line_ex_change_bus = [56]
actions.append(action780)
# ---- END OF ACTION ---
action781 = env.action_space()
action781.gen_change_bus = [11]
action781.gen_change_bus = [12]
action781.line_or_change_bus = [32]
actions.append(action781)
# ---- END OF ACTION ---
action782 = env.action_space()
action782.gen_change_bus = [5]
action782.gen_change_bus = [7]
action782.gen_change_bus = [8]
action782.load_change_bus = [17]
action782.line_ex_change_bus = [18]
action782.line_ex_change_bus = [19]
action782.line_or_change_bus = [22]
action782.line_or_change_bus = [23]
action782.line_or_change_bus = [27]
action782.line_or_change_bus = [28]
action782.line_or_change_bus = [48]
action782.line_or_change_bus = [49]
actions.append(action782)
# ---- END OF ACTION ---
action783 = env.action_space()
action783.gen_change_bus = [5]
action783.gen_change_bus = [6]
action783.gen_change_bus = [7]
action783.gen_change_bus = [8]
action783.line_ex_change_bus = [19]
action783.line_ex_change_bus = [21]
actions.append(action783)
# ---- END OF ACTION ---
action784 = env.action_space()
action784.gen_change_bus = [7]
action784.line_or_change_bus = [22]
action784.line_or_change_bus = [23]
action784.line_or_change_bus = [27]
action784.line_or_change_bus = [28]
action784.line_or_change_bus = [48]
action784.line_or_change_bus = [49]
action784.line_or_change_bus = [54]
actions.append(action784)
# ---- END OF ACTION ---
action785 = env.action_space()
action785.gen_change_bus = [5]
action785.gen_change_bus = [6]
action785.gen_change_bus = [7]
action785.gen_change_bus = [8]
action785.load_change_bus = [17]
action785.line_ex_change_bus = [19]
action785.line_ex_change_bus = [21]
action785.line_or_change_bus = [22]
action785.line_or_change_bus = [23]
action785.line_or_change_bus = [49]
actions.append(action785)
# ---- END OF ACTION ---
action786 = env.action_space()
action786.gen_change_bus = [7]
action786.load_change_bus = [17]
action786.line_ex_change_bus = [19]
action786.line_ex_change_bus = [21]
action786.line_or_change_bus = [22]
action786.line_or_change_bus = [23]
action786.line_or_change_bus = [27]
action786.line_or_change_bus = [28]
action786.line_or_change_bus = [48]
action786.line_or_change_bus = [49]
actions.append(action786)
# ---- END OF ACTION ---
action787 = env.action_space()
action787.load_change_bus = [17]
action787.line_or_change_bus = [22]
action787.line_or_change_bus = [23]
action787.line_or_change_bus = [27]
action787.line_or_change_bus = [28]
actions.append(action787)
# ---- END OF ACTION ---
action788 = env.action_space()
action788.gen_change_bus = [5]
action788.load_change_bus = [17]
action788.line_or_change_bus = [22]
action788.line_or_change_bus = [23]
action788.line_or_change_bus = [48]
action788.line_or_change_bus = [49]
actions.append(action788)
# ---- END OF ACTION ---
action789 = env.action_space()
action789.gen_change_bus = [7]
action789.line_or_change_bus = [22]
action789.line_or_change_bus = [23]
actions.append(action789)
# ---- END OF ACTION ---
action790 = env.action_space()
action790.gen_change_bus = [7]
action790.gen_change_bus = [8]
action790.line_or_change_bus = [27]
action790.line_or_change_bus = [54]
actions.append(action790)
# ---- END OF ACTION ---
action791 = env.action_space()
action791.gen_change_bus = [14]
action791.load_change_bus = [27]
action791.line_ex_change_bus = [37]
action791.line_ex_change_bus = [38]
action791.line_ex_change_bus = [39]
action791.line_or_change_bus = [41]
action791.line_ex_change_bus = [56]
actions.append(action791)
# ---- END OF ACTION ---
action792 = env.action_space()
action792.gen_change_bus = [21]
action792.load_change_bus = [33]
action792.load_change_bus = [35]
action792.load_change_bus = [36]
actions.append(action792)
# ---- END OF ACTION ---
action793 = env.action_space()
action793.gen_change_bus = [8]
action793.load_change_bus = [17]
action793.line_or_change_bus = [27]
action793.line_or_change_bus = [49]
actions.append(action793)
# ---- END OF ACTION ---
action794 = env.action_space()
action794.gen_change_bus = [6]
action794.load_change_bus = [17]
action794.line_or_change_bus = [22]
action794.line_or_change_bus = [23]
action794.line_or_change_bus = [28]
action794.line_or_change_bus = [48]
action794.line_or_change_bus = [49]
actions.append(action794)
# ---- END OF ACTION ---
action795 = env.action_space()
action795.gen_change_bus = [5]
action795.gen_change_bus = [8]
action795.line_ex_change_bus = [18]
action795.line_ex_change_bus = [19]
action795.line_or_change_bus = [28]
action795.line_or_change_bus = [54]
actions.append(action795)
# ---- END OF ACTION ---
action796 = env.action_space()
action796.load_change_bus = [17]
action796.line_ex_change_bus = [18]
action796.line_ex_change_bus = [19]
action796.line_ex_change_bus = [20]
action796.line_or_change_bus = [22]
actions.append(action796)
# ---- END OF ACTION ---
action797 = env.action_space()
action797.gen_change_bus = [5]
action797.gen_change_bus = [8]
action797.line_ex_change_bus = [18]
action797.line_ex_change_bus = [19]
action797.line_ex_change_bus = [20]
action797.line_or_change_bus = [27]
action797.line_or_change_bus = [28]
action797.line_or_change_bus = [54]
actions.append(action797)
# ---- END OF ACTION ---
action798 = env.action_space()
action798.gen_change_bus = [5]
action798.gen_change_bus = [6]
action798.gen_change_bus = [7]
action798.gen_change_bus = [8]
action798.load_change_bus = [17]
action798.line_ex_change_bus = [20]
actions.append(action798)
# ---- END OF ACTION ---
action799 = env.action_space()
action799.load_change_bus = [27]
action799.line_ex_change_bus = [37]
action799.line_or_change_bus = [40]
action799.line_ex_change_bus = [56]
actions.append(action799)
# ---- END OF ACTION ---
action800 = env.action_space()
action800.gen_change_bus = [5]
action800.gen_change_bus = [8]
action800.load_change_bus = [17]
action800.line_or_change_bus = [22]
action800.line_or_change_bus = [23]
action800.line_or_change_bus = [27]
action800.line_or_change_bus = [48]
action800.line_or_change_bus = [49]
actions.append(action800)
# ---- END OF ACTION ---
action801 = env.action_space()
action801.gen_change_bus = [8]
action801.load_change_bus = [17]
action801.line_ex_change_bus = [18]
action801.line_ex_change_bus = [19]
action801.line_ex_change_bus = [21]
action801.line_or_change_bus = [22]
action801.line_or_change_bus = [23]
action801.line_or_change_bus = [28]
action801.line_or_change_bus = [48]
action801.line_or_change_bus = [49]
action801.line_or_change_bus = [54]
actions.append(action801)
# ---- END OF ACTION ---
action802 = env.action_space()
action802.gen_change_bus = [6]
action802.gen_change_bus = [7]
action802.line_ex_change_bus = [19]
action802.line_or_change_bus = [22]
action802.line_or_change_bus = [49]
actions.append(action802)
# ---- END OF ACTION ---
action803 = env.action_space()
action803.gen_change_bus = [12]
action803.gen_change_bus = [13]
action803.load_change_bus = [24]
action803.line_or_change_bus = [32]
action803.line_or_change_bus = [34]
action803.line_or_change_bus = [37]
action803.line_or_change_bus = [38]
actions.append(action803)
# ---- END OF ACTION ---
action804 = env.action_space()
action804.load_change_bus = [31]
action804.line_ex_change_bus = [50]
action804.line_ex_change_bus = [58]
actions.append(action804)
# ---- END OF ACTION ---
action805 = env.action_space()
action805.line_ex_change_bus = [18]
action805.line_ex_change_bus = [19]
action805.line_ex_change_bus = [21]
action805.line_or_change_bus = [28]
action805.line_or_change_bus = [54]
actions.append(action805)
# ---- END OF ACTION ---
action806 = env.action_space()
action806.line_ex_change_bus = [27]
action806.line_ex_change_bus = [28]
action806.line_or_change_bus = [29]
action806.line_or_change_bus = [30]
actions.append(action806)
# ---- END OF ACTION ---
action807 = env.action_space()
action807.gen_change_bus = [12]
action807.line_ex_change_bus = [31]
action807.line_or_change_bus = [37]
action807.line_or_change_bus = [38]
actions.append(action807)
# ---- END OF ACTION ---
action808 = env.action_space()
action808.gen_change_bus = [5]
action808.gen_change_bus = [6]
action808.gen_change_bus = [7]
action808.gen_change_bus = [8]
action808.line_ex_change_bus = [18]
action808.line_ex_change_bus = [19]
action808.line_or_change_bus = [27]
action808.line_or_change_bus = [28]
action808.line_or_change_bus = [49]
actions.append(action808)
# ---- END OF ACTION ---
action809 = env.action_space()
action809.load_change_bus = [2]
action809.load_change_bus = [3]
actions.append(action809)
# ---- END OF ACTION ---
action810 = env.action_space()
action810.gen_change_bus = [5]
action810.gen_change_bus = [6]
action810.gen_change_bus = [8]
action810.load_change_bus = [17]
action810.line_ex_change_bus = [18]
action810.line_ex_change_bus = [19]
action810.line_ex_change_bus = [20]
action810.line_ex_change_bus = [21]
action810.line_or_change_bus = [22]
action810.line_or_change_bus = [23]
action810.line_or_change_bus = [27]
action810.line_or_change_bus = [28]
actions.append(action810)
# ---- END OF ACTION ---
action811 = env.action_space()
action811.gen_change_bus = [7]
action811.load_change_bus = [17]
action811.line_ex_change_bus = [19]
action811.line_ex_change_bus = [21]
action811.line_or_change_bus = [22]
action811.line_or_change_bus = [23]
action811.line_or_change_bus = [48]
action811.line_or_change_bus = [49]
actions.append(action811)
# ---- END OF ACTION ---
action812 = env.action_space()
action812.load_change_bus = [27]
action812.line_ex_change_bus = [38]
action812.line_ex_change_bus = [39]
action812.line_or_change_bus = [40]
action812.line_or_change_bus = [41]
action812.line_ex_change_bus = [56]
actions.append(action812)
# ---- END OF ACTION ---
action813 = env.action_space()
action813.gen_change_bus = [5]
action813.gen_change_bus = [6]
action813.gen_change_bus = [7]
action813.gen_change_bus = [8]
action813.load_change_bus = [17]
actions.append(action813)
# ---- END OF ACTION ---
action814 = env.action_space()
action814.gen_change_bus = [14]
action814.load_change_bus = [27]
action814.line_ex_change_bus = [38]
actions.append(action814)
# ---- END OF ACTION ---
action815 = env.action_space()
action815.load_change_bus = [11]
action815.line_ex_change_bus = [12]
actions.append(action815)
# ---- END OF ACTION ---
action816 = env.action_space()
action816.line_or_change_bus = [15]
actions.append(action816)
# ---- END OF ACTION ---
action817 = env.action_space()
action817.gen_change_bus = [17]
action817.gen_change_bus = [18]
action817.line_or_change_bus = [51]
actions.append(action817)
# ---- END OF ACTION ---
action818 = env.action_space()
action818.gen_change_bus = [11]
action818.gen_change_bus = [12]
action818.load_change_bus = [24]
action818.line_or_change_bus = [38]
actions.append(action818)
# ---- END OF ACTION ---
action819 = env.action_space()
action819.gen_change_bus = [12]
action819.load_change_bus = [24]
action819.line_ex_change_bus = [31]
action819.line_or_change_bus = [32]
action819.line_or_change_bus = [37]
actions.append(action819)
# ---- END OF ACTION ---
action820 = env.action_space()
action820.gen_change_bus = [9]
action820.line_or_change_bus = [29]
action820.line_or_change_bus = [30]
actions.append(action820)
# ---- END OF ACTION ---
action821 = env.action_space()
action821.gen_change_bus = [5]
action821.gen_change_bus = [6]
action821.gen_change_bus = [7]
action821.gen_change_bus = [8]
action821.load_change_bus = [17]
action821.line_ex_change_bus = [19]
action821.line_or_change_bus = [22]
action821.line_or_change_bus = [23]
actions.append(action821)
# ---- END OF ACTION ---
action822 = env.action_space()
action822.load_change_bus = [17]
action822.line_ex_change_bus = [20]
action822.line_or_change_bus = [22]
action822.line_or_change_bus = [23]
action822.line_or_change_bus = [48]
action822.line_or_change_bus = [49]
actions.append(action822)
# ---- END OF ACTION ---
action823 = env.action_space()
action823.gen_change_bus = [7]
action823.gen_change_bus = [8]
action823.load_change_bus = [17]
action823.line_ex_change_bus = [19]
action823.line_or_change_bus = [22]
action823.line_or_change_bus = [23]
action823.line_or_change_bus = [28]
action823.line_or_change_bus = [48]
action823.line_or_change_bus = [49]
action823.line_or_change_bus = [54]
actions.append(action823)
# ---- END OF ACTION ---
action824 = env.action_space()
action824.load_change_bus = [27]
action824.line_ex_change_bus = [38]
action824.line_ex_change_bus = [39]
action824.line_or_change_bus = [40]
action824.line_or_change_bus = [41]
actions.append(action824)
# ---- END OF ACTION ---
action825 = env.action_space()
action825.line_or_change_bus = [14]
action825.line_or_change_bus = [20]
actions.append(action825)
# ---- END OF ACTION ---
action826 = env.action_space()
action826.gen_change_bus = [12]
action826.line_or_change_bus = [32]
actions.append(action826)
# ---- END OF ACTION ---
action827 = env.action_space()
action827.load_change_bus = [24]
action827.line_or_change_bus = [34]
action827.line_or_change_bus = [37]
action827.line_or_change_bus = [38]
actions.append(action827)
# ---- END OF ACTION ---
action828 = env.action_space()
action828.load_change_bus = [35]
actions.append(action828)
# ---- END OF ACTION ---
action829 = env.action_space()
action829.gen_change_bus = [11]
action829.line_or_change_bus = [37]
actions.append(action829)
# ---- END OF ACTION ---
action830 = env.action_space()
action830.gen_change_bus = [7]
action830.line_ex_change_bus = [18]
action830.line_ex_change_bus = [19]
action830.line_or_change_bus = [27]
action830.line_or_change_bus = [28]
actions.append(action830)
# ---- END OF ACTION ---
action831 = env.action_space()
action831.gen_change_bus = [14]
action831.load_change_bus = [27]
action831.line_ex_change_bus = [39]
action831.line_or_change_bus = [40]
actions.append(action831)
# ---- END OF ACTION ---
action832 = env.action_space()
action832.load_change_bus = [27]
action832.line_ex_change_bus = [37]
action832.line_or_change_bus = [41]
action832.line_ex_change_bus = [56]
actions.append(action832)
# ---- END OF ACTION ---
action833 = env.action_space()
action833.gen_change_bus = [11]
action833.gen_change_bus = [12]
action833.gen_change_bus = [13]
action833.line_ex_change_bus = [31]
action833.line_or_change_bus = [34]
action833.line_or_change_bus = [38]
actions.append(action833)
# ---- END OF ACTION ---
action834 = env.action_space()
action834.gen_change_bus = [6]
action834.gen_change_bus = [7]
action834.gen_change_bus = [8]
action834.line_ex_change_bus = [18]
action834.line_ex_change_bus = [19]
action834.line_or_change_bus = [22]
action834.line_or_change_bus = [23]
action834.line_or_change_bus = [27]
action834.line_or_change_bus = [28]
actions.append(action834)
# ---- END OF ACTION ---
action835 = env.action_space()
action835.load_change_bus = [27]
action835.line_ex_change_bus = [39]
action835.line_or_change_bus = [40]
action835.line_ex_change_bus = [56]
actions.append(action835)
# ---- END OF ACTION ---
action836 = env.action_space()
action836.line_ex_change_bus = [28]
action836.line_or_change_bus = [29]
actions.append(action836)
# ---- END OF ACTION ---
action837 = env.action_space()
action837.gen_change_bus = [11]
action837.load_change_bus = [24]
action837.line_ex_change_bus = [31]
actions.append(action837)
# ---- END OF ACTION ---
action838 = env.action_space()
action838.gen_change_bus = [2]
action838.gen_change_bus = [3]
action838.line_ex_change_bus = [10]
actions.append(action838)
# ---- END OF ACTION ---
action839 = env.action_space()
action839.line_ex_change_bus = [49]
action839.line_ex_change_bus = [58]
actions.append(action839)
# ---- END OF ACTION ---
action840 = env.action_space()
action840.gen_change_bus = [11]
action840.gen_change_bus = [13]
action840.load_change_bus = [24]
action840.line_or_change_bus = [34]
actions.append(action840)
# ---- END OF ACTION ---
action841 = env.action_space()
action841.gen_change_bus = [5]
action841.gen_change_bus = [8]
action841.load_change_bus = [17]
action841.line_ex_change_bus = [18]
action841.line_ex_change_bus = [19]
action841.line_or_change_bus = [22]
action841.line_or_change_bus = [23]
action841.line_or_change_bus = [27]
action841.line_or_change_bus = [48]
action841.line_or_change_bus = [49]
action841.line_or_change_bus = [54]
actions.append(action841)
# ---- END OF ACTION ---
action842 = env.action_space()
action842.line_ex_change_bus = [18]
action842.line_ex_change_bus = [19]
action842.line_or_change_bus = [22]
action842.line_or_change_bus = [23]
action842.line_or_change_bus = [28]
action842.line_or_change_bus = [48]
action842.line_or_change_bus = [49]
actions.append(action842)
# ---- END OF ACTION ---
action843 = env.action_space()
action843.gen_change_bus = [5]
action843.gen_change_bus = [6]
action843.gen_change_bus = [7]
action843.gen_change_bus = [8]
action843.load_change_bus = [17]
action843.line_ex_change_bus = [18]
action843.line_ex_change_bus = [19]
action843.line_ex_change_bus = [20]
action843.line_or_change_bus = [22]
action843.line_or_change_bus = [23]
action843.line_or_change_bus = [27]
action843.line_or_change_bus = [28]
action843.line_or_change_bus = [48]
action843.line_or_change_bus = [49]
action843.line_or_change_bus = [54]
actions.append(action843)
# ---- END OF ACTION ---
action844 = env.action_space()
action844.gen_change_bus = [6]
action844.gen_change_bus = [7]
action844.gen_change_bus = [8]
action844.line_ex_change_bus = [18]
action844.line_ex_change_bus = [19]
action844.line_ex_change_bus = [20]
action844.line_or_change_bus = [27]
action844.line_or_change_bus = [28]
actions.append(action844)
# ---- END OF ACTION ---
action845 = env.action_space()
action845.gen_change_bus = [20]
action845.line_ex_change_bus = [49]
action845.line_or_change_bus = [52]
action845.line_ex_change_bus = [58]
actions.append(action845)
# ---- END OF ACTION ---
action846 = env.action_space()
action846.gen_change_bus = [11]
action846.gen_change_bus = [12]
action846.gen_change_bus = [13]
action846.load_change_bus = [24]
action846.line_or_change_bus = [32]
actions.append(action846)
# ---- END OF ACTION ---
action847 = env.action_space()
action847.gen_change_bus = [5]
action847.gen_change_bus = [7]
action847.gen_change_bus = [8]
action847.line_ex_change_bus = [18]
action847.line_ex_change_bus = [19]
action847.line_or_change_bus = [22]
action847.line_or_change_bus = [23]
action847.line_or_change_bus = [48]
action847.line_or_change_bus = [49]
action847.line_or_change_bus = [54]
actions.append(action847)
# ---- END OF ACTION ---
action848 = env.action_space()
action848.gen_change_bus = [6]
action848.gen_change_bus = [7]
action848.load_change_bus = [17]
action848.line_ex_change_bus = [18]
action848.line_ex_change_bus = [19]
action848.line_or_change_bus = [22]
action848.line_or_change_bus = [23]
action848.line_or_change_bus = [27]
action848.line_or_change_bus = [28]
action848.line_or_change_bus = [48]
action848.line_or_change_bus = [49]
actions.append(action848)
# ---- END OF ACTION ---
action849 = env.action_space()
action849.gen_change_bus = [9]
action849.load_change_bus = [22]
action849.line_or_change_bus = [30]
actions.append(action849)
# ---- END OF ACTION ---
action850 = env.action_space()
action850.gen_change_bus = [13]
action850.line_ex_change_bus = [31]
action850.line_or_change_bus = [32]
action850.line_or_change_bus = [34]
action850.line_or_change_bus = [38]
actions.append(action850)
# ---- END OF ACTION ---
action851 = env.action_space()
action851.gen_change_bus = [5]
action851.gen_change_bus = [6]
action851.gen_change_bus = [7]
action851.line_or_change_bus = [54]
actions.append(action851)
# ---- END OF ACTION ---
action852 = env.action_space()
action852.gen_change_bus = [5]
action852.gen_change_bus = [8]
action852.line_or_change_bus = [28]
actions.append(action852)
# ---- END OF ACTION ---
action853 = env.action_space()
action853.load_change_bus = [24]
action853.line_or_change_bus = [37]
action853.line_or_change_bus = [38]
actions.append(action853)
# ---- END OF ACTION ---
action854 = env.action_space()
action854.gen_change_bus = [7]
action854.load_change_bus = [17]
action854.line_or_change_bus = [22]
action854.line_or_change_bus = [23]
action854.line_or_change_bus = [54]
actions.append(action854)
# ---- END OF ACTION ---
action855 = env.action_space()
action855.load_change_bus = [17]
action855.line_ex_change_bus = [18]
action855.line_ex_change_bus = [19]
action855.line_ex_change_bus = [20]
action855.line_or_change_bus = [22]
action855.line_or_change_bus = [23]
action855.line_or_change_bus = [27]
action855.line_or_change_bus = [28]
action855.line_or_change_bus = [48]
action855.line_or_change_bus = [49]
action855.line_or_change_bus = [54]
actions.append(action855)
# ---- END OF ACTION ---
action856 = env.action_space()
action856.gen_change_bus = [3]
action856.line_ex_change_bus = [10]
action856.line_or_change_bus = [18]
actions.append(action856)
# ---- END OF ACTION ---
action857 = env.action_space()
action857.gen_change_bus = [14]
action857.load_change_bus = [27]
action857.line_ex_change_bus = [37]
action857.line_ex_change_bus = [39]
action857.line_or_change_bus = [41]
actions.append(action857)
# ---- END OF ACTION ---
action858 = env.action_space()
action858.gen_change_bus = [10]
action858.load_change_bus = [23]
action858.line_or_change_bus = [31]
action858.line_or_change_bus = [39]
actions.append(action858)
# ---- END OF ACTION ---
action859 = env.action_space()
action859.gen_change_bus = [8]
action859.line_ex_change_bus = [18]
action859.line_ex_change_bus = [19]
action859.line_or_change_bus = [22]
action859.line_or_change_bus = [23]
action859.line_or_change_bus = [28]
action859.line_or_change_bus = [49]
action859.line_or_change_bus = [54]
actions.append(action859)
# ---- END OF ACTION ---
action860 = env.action_space()
action860.gen_change_bus = [5]
action860.gen_change_bus = [8]
action860.load_change_bus = [17]
action860.line_ex_change_bus = [19]
action860.line_ex_change_bus = [20]
action860.line_or_change_bus = [22]
action860.line_or_change_bus = [23]
action860.line_or_change_bus = [27]
action860.line_or_change_bus = [28]
action860.line_or_change_bus = [48]
action860.line_or_change_bus = [49]
action860.line_or_change_bus = [54]
actions.append(action860)
# ---- END OF ACTION ---
action861 = env.action_space()
action861.line_ex_change_bus = [10]
action861.line_or_change_bus = [18]
actions.append(action861)
# ---- END OF ACTION ---
action862 = env.action_space()
action862.gen_change_bus = [6]
action862.gen_change_bus = [7]
action862.gen_change_bus = [8]
action862.line_ex_change_bus = [18]
action862.line_ex_change_bus = [19]
action862.line_or_change_bus = [22]
action862.line_or_change_bus = [23]
action862.line_or_change_bus = [48]
action862.line_or_change_bus = [49]
actions.append(action862)
# ---- END OF ACTION ---
action863 = env.action_space()
action863.gen_change_bus = [5]
action863.gen_change_bus = [6]
action863.gen_change_bus = [7]
action863.gen_change_bus = [8]
action863.load_change_bus = [17]
action863.line_ex_change_bus = [18]
action863.line_ex_change_bus = [19]
action863.line_or_change_bus = [22]
action863.line_or_change_bus = [23]
action863.line_or_change_bus = [27]
action863.line_or_change_bus = [28]
action863.line_or_change_bus = [48]
action863.line_or_change_bus = [49]
actions.append(action863)
# ---- END OF ACTION ---
action864 = env.action_space()
action864.load_change_bus = [31]
action864.line_or_change_bus = [52]
action864.line_ex_change_bus = [58]
actions.append(action864)
# ---- END OF ACTION ---
action865 = env.action_space()
action865.line_ex_change_bus = [20]
action865.line_or_change_bus = [27]
action865.line_or_change_bus = [28]
action865.line_or_change_bus = [54]
actions.append(action865)
# ---- END OF ACTION ---
action866 = env.action_space()
action866.gen_change_bus = [8]
action866.line_ex_change_bus = [19]
action866.line_ex_change_bus = [20]
action866.line_ex_change_bus = [21]
action866.line_or_change_bus = [27]
action866.line_or_change_bus = [28]
action866.line_or_change_bus = [54]
actions.append(action866)
# ---- END OF ACTION ---
action867 = env.action_space()
action867.gen_change_bus = [14]
action867.load_change_bus = [27]
action867.line_ex_change_bus = [38]
action867.line_or_change_bus = [40]
action867.line_or_change_bus = [41]
actions.append(action867)
# ---- END OF ACTION ---
action868 = env.action_space()
action868.gen_change_bus = [5]
action868.gen_change_bus = [6]
action868.gen_change_bus = [7]
action868.gen_change_bus = [8]
action868.load_change_bus = [17]
action868.line_ex_change_bus = [19]
action868.line_or_change_bus = [22]
action868.line_or_change_bus = [23]
action868.line_or_change_bus = [49]
actions.append(action868)
# ---- END OF ACTION ---
action869 = env.action_space()
action869.gen_change_bus = [5]
action869.gen_change_bus = [7]
action869.gen_change_bus = [8]
action869.line_ex_change_bus = [19]
action869.line_or_change_bus = [28]
actions.append(action869)
# ---- END OF ACTION ---
action870 = env.action_space()
action870.gen_change_bus = [8]
action870.line_ex_change_bus = [19]
actions.append(action870)
# ---- END OF ACTION ---
action871 = env.action_space()
action871.load_change_bus = [34]
action871.load_change_bus = [35]
action871.line_ex_change_bus = [54]
actions.append(action871)
# ---- END OF ACTION ---
action872 = env.action_space()
action872.gen_change_bus = [7]
action872.load_change_bus = [17]
action872.line_ex_change_bus = [20]
action872.line_or_change_bus = [22]
action872.line_or_change_bus = [23]
action872.line_or_change_bus = [48]
action872.line_or_change_bus = [49]
action872.line_or_change_bus = [54]
actions.append(action872)
# ---- END OF ACTION ---
action873 = env.action_space()
action873.gen_change_bus = [5]
action873.gen_change_bus = [8]
action873.load_change_bus = [17]
action873.line_ex_change_bus = [19]
action873.line_or_change_bus = [22]
action873.line_or_change_bus = [23]
actions.append(action873)
# ---- END OF ACTION ---
action874 = env.action_space()
action874.gen_change_bus = [11]
action874.gen_change_bus = [13]
action874.load_change_bus = [24]
actions.append(action874)
# ---- END OF ACTION ---
action875 = env.action_space()
action875.gen_change_bus = [6]
action875.gen_change_bus = [7]
action875.line_ex_change_bus = [19]
action875.line_or_change_bus = [22]
action875.line_or_change_bus = [23]
action875.line_or_change_bus = [48]
action875.line_or_change_bus = [49]
actions.append(action875)
# ---- END OF ACTION ---
action876 = env.action_space()
action876.line_or_change_bus = [29]
action876.line_or_change_bus = [36]
actions.append(action876)
# ---- END OF ACTION ---
action877 = env.action_space()
action877.gen_change_bus = [9]
action877.load_change_bus = [22]
action877.line_ex_change_bus = [27]
action877.line_or_change_bus = [30]
action877.line_or_change_bus = [36]
actions.append(action877)
# ---- END OF ACTION ---
action878 = env.action_space()
action878.gen_change_bus = [5]
action878.gen_change_bus = [6]
action878.gen_change_bus = [7]
action878.gen_change_bus = [8]
action878.line_or_change_bus = [54]
actions.append(action878)
# ---- END OF ACTION ---
action879 = env.action_space()
action879.gen_change_bus = [12]
action879.line_or_change_bus = [32]
action879.line_or_change_bus = [37]
action879.line_or_change_bus = [38]
actions.append(action879)
# ---- END OF ACTION ---
action880 = env.action_space()
action880.gen_change_bus = [14]
action880.line_or_change_bus = [41]
action880.line_ex_change_bus = [56]
actions.append(action880)
# ---- END OF ACTION ---
action881 = env.action_space()
action881.gen_change_bus = [5]
action881.gen_change_bus = [8]
action881.load_change_bus = [17]
action881.line_ex_change_bus = [18]
action881.line_ex_change_bus = [19]
action881.line_or_change_bus = [22]
action881.line_or_change_bus = [23]
action881.line_or_change_bus = [27]
action881.line_or_change_bus = [28]
action881.line_or_change_bus = [48]
action881.line_or_change_bus = [49]
actions.append(action881)
# ---- END OF ACTION ---
action882 = env.action_space()
action882.gen_change_bus = [5]
action882.gen_change_bus = [6]
action882.gen_change_bus = [7]
action882.gen_change_bus = [8]
action882.load_change_bus = [17]
action882.line_or_change_bus = [22]
action882.line_or_change_bus = [23]
action882.line_or_change_bus = [28]
action882.line_or_change_bus = [48]
action882.line_or_change_bus = [49]
actions.append(action882)
# ---- END OF ACTION ---
action883 = env.action_space()
action883.gen_change_bus = [9]
action883.load_change_bus = [22]
action883.line_ex_change_bus = [28]
action883.line_or_change_bus = [29]
action883.line_or_change_bus = [30]
action883.line_or_change_bus = [36]
actions.append(action883)
# ---- END OF ACTION ---
action884 = env.action_space()
action884.gen_change_bus = [2]
action884.load_change_bus = [10]
action884.line_or_change_bus = [18]
actions.append(action884)
# ---- END OF ACTION ---
action885 = env.action_space()
action885.gen_change_bus = [11]
action885.line_or_change_bus = [32]
action885.line_or_change_bus = [34]
action885.line_or_change_bus = [38]
actions.append(action885)
# ---- END OF ACTION ---
action886 = env.action_space()
action886.line_or_change_bus = [7]
actions.append(action886)
# ---- END OF ACTION ---
action887 = env.action_space()
action887.gen_change_bus = [7]
action887.gen_change_bus = [8]
action887.load_change_bus = [17]
action887.line_ex_change_bus = [18]
action887.line_ex_change_bus = [19]
action887.line_or_change_bus = [22]
action887.line_or_change_bus = [23]
action887.line_or_change_bus = [27]
action887.line_or_change_bus = [28]
action887.line_or_change_bus = [48]
action887.line_or_change_bus = [49]
action887.line_or_change_bus = [54]
actions.append(action887)
# ---- END OF ACTION ---
action888 = env.action_space()
action888.gen_change_bus = [9]
action888.line_ex_change_bus = [28]
actions.append(action888)
# ---- END OF ACTION ---
action889 = env.action_space()
action889.gen_change_bus = [11]
action889.gen_change_bus = [12]
action889.load_change_bus = [24]
action889.line_or_change_bus = [34]
action889.line_or_change_bus = [38]
actions.append(action889)
# ---- END OF ACTION ---
action890 = env.action_space()
action890.gen_change_bus = [17]
action890.gen_change_bus = [18]
action890.line_ex_change_bus = [44]
action890.line_or_change_bus = [50]
actions.append(action890)
# ---- END OF ACTION ---
action891 = env.action_space()
action891.gen_change_bus = [8]
action891.load_change_bus = [17]
action891.line_ex_change_bus = [18]
action891.line_ex_change_bus = [19]
action891.line_or_change_bus = [22]
action891.line_or_change_bus = [23]
action891.line_or_change_bus = [27]
action891.line_or_change_bus = [28]
action891.line_or_change_bus = [48]
action891.line_or_change_bus = [49]
actions.append(action891)
# ---- END OF ACTION ---
action892 = env.action_space()
action892.gen_change_bus = [7]
action892.line_ex_change_bus = [20]
action892.line_ex_change_bus = [21]
actions.append(action892)
# ---- END OF ACTION ---
action893 = env.action_space()
action893.gen_change_bus = [5]
action893.gen_change_bus = [8]
action893.load_change_bus = [17]
action893.line_ex_change_bus = [19]
action893.line_ex_change_bus = [20]
action893.line_or_change_bus = [22]
action893.line_or_change_bus = [23]
action893.line_or_change_bus = [28]
action893.line_or_change_bus = [48]
action893.line_or_change_bus = [49]
action893.line_or_change_bus = [54]
actions.append(action893)
# ---- END OF ACTION ---
action894 = env.action_space()
action894.line_or_change_bus = [22]
action894.line_or_change_bus = [23]
action894.line_or_change_bus = [54]
actions.append(action894)
# ---- END OF ACTION ---
action895 = env.action_space()
action895.load_change_bus = [17]
action895.line_ex_change_bus = [18]
action895.line_ex_change_bus = [19]
action895.line_ex_change_bus = [21]
action895.line_or_change_bus = [22]
action895.line_or_change_bus = [23]
action895.line_or_change_bus = [28]
action895.line_or_change_bus = [48]
action895.line_or_change_bus = [49]
actions.append(action895)
# ---- END OF ACTION ---
action896 = env.action_space()
action896.gen_change_bus = [5]
action896.gen_change_bus = [6]
action896.gen_change_bus = [7]
action896.gen_change_bus = [8]
action896.load_change_bus = [17]
action896.line_ex_change_bus = [19]
action896.line_or_change_bus = [22]
action896.line_or_change_bus = [23]
action896.line_or_change_bus = [49]
action896.line_or_change_bus = [54]
actions.append(action896)
# ---- END OF ACTION ---
action897 = env.action_space()
action897.gen_change_bus = [12]
action897.line_or_change_bus = [38]
actions.append(action897)
# ---- END OF ACTION ---
action898 = env.action_space()
action898.gen_change_bus = [19]
action898.load_change_bus = [30]
actions.append(action898)
# ---- END OF ACTION ---
action899 = env.action_space()
action899.gen_change_bus = [11]
action899.gen_change_bus = [12]
action899.line_ex_change_bus = [31]
action899.line_or_change_bus = [34]
actions.append(action899)
# ---- END OF ACTION ---
action900 = env.action_space()
action900.gen_change_bus = [13]
action900.line_ex_change_bus = [31]
action900.line_or_change_bus = [32]
action900.line_or_change_bus = [34]
action900.line_or_change_bus = [37]
action900.line_or_change_bus = [38]
actions.append(action900)
# ---- END OF ACTION ---
action901 = env.action_space()
action901.gen_change_bus = [14]
action901.line_ex_change_bus = [37]
action901.line_ex_change_bus = [56]
actions.append(action901)
# ---- END OF ACTION ---
action902 = env.action_space()
action902.gen_change_bus = [14]
action902.line_ex_change_bus = [37]
action902.line_ex_change_bus = [38]
action902.line_ex_change_bus = [39]
action902.line_or_change_bus = [41]
actions.append(action902)
# ---- END OF ACTION ---
action903 = env.action_space()
action903.gen_change_bus = [5]
action903.gen_change_bus = [8]
action903.load_change_bus = [17]
action903.line_or_change_bus = [27]
action903.line_or_change_bus = [28]
actions.append(action903)
# ---- END OF ACTION ---
action904 = env.action_space()
action904.gen_change_bus = [8]
action904.load_change_bus = [17]
action904.line_ex_change_bus = [19]
action904.line_or_change_bus = [22]
action904.line_or_change_bus = [23]
action904.line_or_change_bus = [48]
action904.line_or_change_bus = [49]
actions.append(action904)
# ---- END OF ACTION ---
action905 = env.action_space()
action905.gen_change_bus = [6]
action905.gen_change_bus = [7]
action905.line_ex_change_bus = [18]
action905.line_ex_change_bus = [19]
action905.line_or_change_bus = [27]
action905.line_or_change_bus = [28]
actions.append(action905)
# ---- END OF ACTION ---
action906 = env.action_space()
action906.gen_change_bus = [14]
action906.load_change_bus = [27]
action906.line_or_change_bus = [41]
action906.line_ex_change_bus = [56]
actions.append(action906)
# ---- END OF ACTION ---
action907 = env.action_space()
action907.gen_change_bus = [17]
action907.gen_change_bus = [18]
action907.line_ex_change_bus = [44]
action907.line_or_change_bus = [51]
actions.append(action907)
# ---- END OF ACTION ---
action908 = env.action_space()
action908.load_change_bus = [17]
action908.line_ex_change_bus = [18]
action908.line_ex_change_bus = [19]
action908.line_ex_change_bus = [20]
action908.line_ex_change_bus = [21]
action908.line_or_change_bus = [22]
action908.line_or_change_bus = [54]
actions.append(action908)
# ---- END OF ACTION ---
action909 = env.action_space()
action909.gen_change_bus = [12]
action909.load_change_bus = [24]
action909.line_or_change_bus = [34]
actions.append(action909)
# ---- END OF ACTION ---
action910 = env.action_space()
action910.load_change_bus = [17]
action910.line_ex_change_bus = [20]
action910.line_ex_change_bus = [21]
action910.line_or_change_bus = [48]
action910.line_or_change_bus = [49]
action910.line_or_change_bus = [54]
actions.append(action910)
# ---- END OF ACTION ---
action911 = env.action_space()
action911.load_change_bus = [24]
action911.line_or_change_bus = [32]
action911.line_or_change_bus = [37]
action911.line_or_change_bus = [38]
actions.append(action911)
# ---- END OF ACTION ---
action912 = env.action_space()
action912.gen_change_bus = [5]
action912.gen_change_bus = [6]
action912.gen_change_bus = [7]
action912.gen_change_bus = [8]
action912.load_change_bus = [17]
action912.line_ex_change_bus = [19]
action912.line_ex_change_bus = [21]
action912.line_or_change_bus = [22]
action912.line_or_change_bus = [23]
action912.line_or_change_bus = [48]
action912.line_or_change_bus = [49]
action912.line_or_change_bus = [54]
actions.append(action912)
# ---- END OF ACTION ---
action913 = env.action_space()
action913.gen_change_bus = [17]
action913.line_ex_change_bus = [44]
action913.line_or_change_bus = [50]
actions.append(action913)
# ---- END OF ACTION ---
action914 = env.action_space()
action914.load_change_bus = [17]
action914.line_ex_change_bus = [18]
action914.line_ex_change_bus = [19]
action914.line_ex_change_bus = [20]
action914.line_or_change_bus = [22]
action914.line_or_change_bus = [27]
actions.append(action914)
# ---- END OF ACTION ---
action915 = env.action_space()
action915.load_change_bus = [24]
action915.line_ex_change_bus = [31]
action915.line_or_change_bus = [32]
actions.append(action915)
# ---- END OF ACTION ---
action916 = env.action_space()
action916.gen_change_bus = [9]
action916.line_ex_change_bus = [27]
action916.line_ex_change_bus = [28]
action916.line_or_change_bus = [29]
action916.line_or_change_bus = [30]
action916.line_or_change_bus = [36]
actions.append(action916)
# ---- END OF ACTION ---
action917 = env.action_space()
action917.gen_change_bus = [7]
action917.line_ex_change_bus = [20]
actions.append(action917)
# ---- END OF ACTION ---
action918 = env.action_space()
action918.gen_change_bus = [11]
action918.gen_change_bus = [12]
action918.gen_change_bus = [13]
action918.load_change_bus = [24]
action918.line_ex_change_bus = [31]
action918.line_or_change_bus = [37]
action918.line_or_change_bus = [38]
actions.append(action918)
# ---- END OF ACTION ---
action919 = env.action_space()
action919.gen_change_bus = [7]
action919.load_change_bus = [17]
action919.line_ex_change_bus = [18]
action919.line_ex_change_bus = [19]
action919.line_or_change_bus = [22]
action919.line_or_change_bus = [23]
action919.line_or_change_bus = [48]
action919.line_or_change_bus = [49]
actions.append(action919)
# ---- END OF ACTION ---
action920 = env.action_space()
action920.gen_change_bus = [11]
action920.gen_change_bus = [12]
action920.gen_change_bus = [13]
action920.load_change_bus = [24]
action920.line_or_change_bus = [37]
actions.append(action920)
# ---- END OF ACTION ---
action921 = env.action_space()
action921.line_ex_change_bus = [31]
actions.append(action921)
# ---- END OF ACTION ---
action922 = env.action_space()
action922.line_ex_change_bus = [21]
action922.line_or_change_bus = [28]
actions.append(action922)
# ---- END OF ACTION ---
action923 = env.action_space()
action923.line_ex_change_bus = [2]
action923.line_ex_change_bus = [4]
action923.line_ex_change_bus = [55]
actions.append(action923)
# ---- END OF ACTION ---
action924 = env.action_space()
action924.gen_change_bus = [5]
action924.gen_change_bus = [6]
action924.gen_change_bus = [7]
action924.gen_change_bus = [8]
action924.line_ex_change_bus = [19]
action924.line_ex_change_bus = [21]
action924.line_or_change_bus = [22]
action924.line_or_change_bus = [23]
action924.line_or_change_bus = [27]
action924.line_or_change_bus = [48]
action924.line_or_change_bus = [49]
actions.append(action924)
# ---- END OF ACTION ---
action925 = env.action_space()
action925.load_change_bus = [30]
action925.line_or_change_bus = [58]
actions.append(action925)
# ---- END OF ACTION ---
action926 = env.action_space()
action926.line_ex_change_bus = [18]
action926.line_ex_change_bus = [19]
action926.line_or_change_bus = [22]
action926.line_or_change_bus = [23]
action926.line_or_change_bus = [27]
action926.line_or_change_bus = [49]
action926.line_or_change_bus = [54]
actions.append(action926)
# ---- END OF ACTION ---
action927 = env.action_space()
action927.gen_change_bus = [12]
action927.line_ex_change_bus = [31]
action927.line_or_change_bus = [38]
actions.append(action927)
# ---- END OF ACTION ---
action928 = env.action_space()
action928.line_or_change_bus = [27]
action928.line_or_change_bus = [28]
action928.line_or_change_bus = [48]
action928.line_or_change_bus = [54]
actions.append(action928)
# ---- END OF ACTION ---
action929 = env.action_space()
action929.gen_change_bus = [5]
action929.load_change_bus = [17]
action929.line_ex_change_bus = [18]
action929.line_ex_change_bus = [19]
action929.line_ex_change_bus = [20]
action929.line_or_change_bus = [27]
action929.line_or_change_bus = [28]
action929.line_or_change_bus = [48]
action929.line_or_change_bus = [49]
actions.append(action929)
# ---- END OF ACTION ---
action930 = env.action_space()
action930.gen_change_bus = [5]
action930.gen_change_bus = [6]
action930.gen_change_bus = [7]
action930.line_ex_change_bus = [18]
action930.line_ex_change_bus = [19]
action930.line_ex_change_bus = [20]
action930.line_or_change_bus = [22]
action930.line_or_change_bus = [23]
action930.line_or_change_bus = [27]
action930.line_or_change_bus = [28]
action930.line_or_change_bus = [48]
action930.line_or_change_bus = [49]
actions.append(action930)
# ---- END OF ACTION ---
action931 = env.action_space()
action931.line_ex_change_bus = [19]
action931.line_or_change_bus = [22]
action931.line_or_change_bus = [23]
actions.append(action931)
# ---- END OF ACTION ---
action932 = env.action_space()
action932.gen_change_bus = [6]
action932.load_change_bus = [17]
action932.line_ex_change_bus = [19]
action932.line_or_change_bus = [22]
action932.line_or_change_bus = [23]
action932.line_or_change_bus = [48]
action932.line_or_change_bus = [49]
action932.line_or_change_bus = [54]
actions.append(action932)
# ---- END OF ACTION ---
action933 = env.action_space()
action933.line_ex_change_bus = [19]
action933.line_ex_change_bus = [20]
action933.line_or_change_bus = [27]
action933.line_or_change_bus = [28]
action933.line_or_change_bus = [49]
actions.append(action933)
# ---- END OF ACTION ---
action934 = env.action_space()
action934.gen_change_bus = [7]
action934.load_change_bus = [17]
action934.line_or_change_bus = [48]
actions.append(action934)
# ---- END OF ACTION ---
action935 = env.action_space()
action935.gen_change_bus = [6]
action935.gen_change_bus = [7]
action935.gen_change_bus = [8]
action935.line_ex_change_bus = [18]
action935.line_ex_change_bus = [19]
action935.line_or_change_bus = [22]
action935.line_or_change_bus = [27]
action935.line_or_change_bus = [28]
action935.line_or_change_bus = [54]
actions.append(action935)
# ---- END OF ACTION ---
action936 = env.action_space()
action936.gen_change_bus = [5]
action936.gen_change_bus = [6]
action936.gen_change_bus = [7]
action936.load_change_bus = [17]
action936.line_or_change_bus = [49]
actions.append(action936)
# ---- END OF ACTION ---
action937 = env.action_space()
action937.gen_change_bus = [5]
action937.gen_change_bus = [6]
action937.gen_change_bus = [7]
action937.gen_change_bus = [8]
action937.load_change_bus = [17]
action937.line_ex_change_bus = [18]
action937.line_ex_change_bus = [19]
action937.line_or_change_bus = [22]
action937.line_or_change_bus = [23]
action937.line_or_change_bus = [27]
action937.line_or_change_bus = [48]
action937.line_or_change_bus = [49]
actions.append(action937)
# ---- END OF ACTION ---
action938 = env.action_space()
action938.load_change_bus = [17]
action938.line_ex_change_bus = [19]
action938.line_or_change_bus = [22]
action938.line_or_change_bus = [23]
action938.line_or_change_bus = [48]
action938.line_or_change_bus = [49]
action938.line_or_change_bus = [54]
actions.append(action938)
# ---- END OF ACTION ---
action939 = env.action_space()
action939.gen_change_bus = [7]
action939.gen_change_bus = [8]
action939.line_ex_change_bus = [19]
actions.append(action939)
# ---- END OF ACTION ---
action940 = env.action_space()
action940.load_change_bus = [7]
actions.append(action940)
# ---- END OF ACTION ---
action941 = env.action_space()
action941.gen_change_bus = [5]
action941.gen_change_bus = [6]
action941.gen_change_bus = [7]
action941.gen_change_bus = [8]
action941.load_change_bus = [17]
action941.line_ex_change_bus = [19]
action941.line_ex_change_bus = [20]
action941.line_or_change_bus = [27]
actions.append(action941)
# ---- END OF ACTION ---
action942 = env.action_space()
action942.load_change_bus = [17]
action942.line_ex_change_bus = [20]
action942.line_ex_change_bus = [21]
action942.line_or_change_bus = [22]
action942.line_or_change_bus = [23]
action942.line_or_change_bus = [28]
action942.line_or_change_bus = [48]
action942.line_or_change_bus = [49]
action942.line_or_change_bus = [54]
actions.append(action942)
# ---- END OF ACTION ---
action943 = env.action_space()
action943.gen_change_bus = [5]
action943.gen_change_bus = [7]
action943.gen_change_bus = [8]
action943.load_change_bus = [17]
action943.line_ex_change_bus = [19]
action943.line_or_change_bus = [28]
actions.append(action943)
# ---- END OF ACTION ---
action944 = env.action_space()
action944.gen_change_bus = [14]
action944.load_change_bus = [27]
action944.line_ex_change_bus = [37]
action944.line_ex_change_bus = [39]
action944.line_or_change_bus = [40]
action944.line_or_change_bus = [41]
action944.line_ex_change_bus = [56]
actions.append(action944)
# ---- END OF ACTION ---
action945 = env.action_space()
action945.gen_change_bus = [12]
action945.line_ex_change_bus = [31]
action945.line_or_change_bus = [34]
action945.line_or_change_bus = [38]
actions.append(action945)
# ---- END OF ACTION ---
action946 = env.action_space()
action946.gen_change_bus = [8]
action946.load_change_bus = [17]
action946.line_ex_change_bus = [19]
action946.line_or_change_bus = [22]
action946.line_or_change_bus = [23]
action946.line_or_change_bus = [28]
action946.line_or_change_bus = [48]
action946.line_or_change_bus = [49]
action946.line_or_change_bus = [54]
actions.append(action946)
# ---- END OF ACTION ---
action947 = env.action_space()
action947.gen_change_bus = [11]
action947.gen_change_bus = [12]
actions.append(action947)
# ---- END OF ACTION ---
action948 = env.action_space()
action948.line_or_change_bus = [33]
actions.append(action948)
# ---- END OF ACTION ---
action949 = env.action_space()
action949.gen_change_bus = [14]
action949.load_change_bus = [27]
action949.line_ex_change_bus = [38]
action949.line_ex_change_bus = [39]
action949.line_or_change_bus = [40]
action949.line_or_change_bus = [41]
actions.append(action949)
# ---- END OF ACTION ---
action950 = env.action_space()
action950.gen_change_bus = [5]
action950.gen_change_bus = [6]
action950.gen_change_bus = [8]
action950.line_ex_change_bus = [18]
action950.line_ex_change_bus = [19]
action950.line_ex_change_bus = [20]
action950.line_or_change_bus = [27]
action950.line_or_change_bus = [28]
actions.append(action950)
# ---- END OF ACTION ---
action951 = env.action_space()
action951.gen_change_bus = [5]
action951.gen_change_bus = [6]
action951.gen_change_bus = [8]
action951.load_change_bus = [17]
action951.line_ex_change_bus = [18]
action951.line_ex_change_bus = [19]
action951.line_or_change_bus = [22]
action951.line_or_change_bus = [23]
action951.line_or_change_bus = [28]
action951.line_or_change_bus = [48]
action951.line_or_change_bus = [49]
actions.append(action951)
# ---- END OF ACTION ---
action952 = env.action_space()
action952.gen_change_bus = [11]
action952.line_ex_change_bus = [31]
action952.line_or_change_bus = [32]
action952.line_or_change_bus = [34]
action952.line_or_change_bus = [38]
actions.append(action952)
# ---- END OF ACTION ---
action953 = env.action_space()
action953.line_ex_change_bus = [44]
action953.line_or_change_bus = [51]
actions.append(action953)
# ---- END OF ACTION ---
action954 = env.action_space()
action954.gen_change_bus = [5]
action954.gen_change_bus = [7]
action954.gen_change_bus = [8]
action954.line_ex_change_bus = [19]
action954.line_or_change_bus = [54]
actions.append(action954)
# ---- END OF ACTION ---
action955 = env.action_space()
action955.load_change_bus = [17]
action955.line_ex_change_bus = [20]
action955.line_ex_change_bus = [21]
action955.line_or_change_bus = [48]
action955.line_or_change_bus = [49]
actions.append(action955)
# ---- END OF ACTION ---
action956 = env.action_space()
action956.gen_change_bus = [20]
action956.load_change_bus = [31]
action956.line_ex_change_bus = [49]
action956.line_ex_change_bus = [50]
action956.line_or_change_bus = [52]
actions.append(action956)
# ---- END OF ACTION ---
action957 = env.action_space()
action957.gen_change_bus = [17]
action957.gen_change_bus = [18]
action957.load_change_bus = [29]
actions.append(action957)
# ---- END OF ACTION ---
action958 = env.action_space()
action958.gen_change_bus = [5]
action958.gen_change_bus = [6]
action958.gen_change_bus = [7]
action958.gen_change_bus = [8]
action958.line_ex_change_bus = [19]
action958.line_ex_change_bus = [21]
action958.line_or_change_bus = [23]
action958.line_or_change_bus = [27]
action958.line_or_change_bus = [48]
action958.line_or_change_bus = [49]
action958.line_or_change_bus = [54]
actions.append(action958)
# ---- END OF ACTION ---
action959 = env.action_space()
action959.gen_change_bus = [5]
action959.gen_change_bus = [6]
action959.gen_change_bus = [7]
action959.gen_change_bus = [8]
action959.line_ex_change_bus = [20]
action959.line_ex_change_bus = [21]
action959.line_or_change_bus = [22]
action959.line_or_change_bus = [23]
actions.append(action959)
# ---- END OF ACTION ---
action960 = env.action_space()
action960.gen_change_bus = [21]
action960.load_change_bus = [34]
action960.line_ex_change_bus = [54]
actions.append(action960)
# ---- END OF ACTION ---
action961 = env.action_space()
action961.gen_change_bus = [11]
action961.gen_change_bus = [12]
action961.gen_change_bus = [13]
action961.line_or_change_bus = [32]
action961.line_or_change_bus = [34]
actions.append(action961)
# ---- END OF ACTION ---
action962 = env.action_space()
action962.load_change_bus = [27]
action962.line_ex_change_bus = [37]
action962.line_ex_change_bus = [39]
action962.line_or_change_bus = [40]
action962.line_or_change_bus = [41]
actions.append(action962)
# ---- END OF ACTION ---
action963 = env.action_space()
action963.gen_change_bus = [5]
action963.gen_change_bus = [7]
action963.gen_change_bus = [8]
action963.line_ex_change_bus = [19]
actions.append(action963)
# ---- END OF ACTION ---
action964 = env.action_space()
action964.line_ex_change_bus = [20]
action964.line_or_change_bus = [22]
action964.line_or_change_bus = [23]
action964.line_or_change_bus = [49]
actions.append(action964)
# ---- END OF ACTION ---
action965 = env.action_space()
action965.gen_change_bus = [5]
action965.gen_change_bus = [6]
action965.gen_change_bus = [8]
action965.load_change_bus = [17]
action965.line_ex_change_bus = [18]
action965.line_ex_change_bus = [19]
action965.line_or_change_bus = [22]
action965.line_or_change_bus = [23]
action965.line_or_change_bus = [27]
action965.line_or_change_bus = [28]
action965.line_or_change_bus = [48]
action965.line_or_change_bus = [49]
actions.append(action965)
# ---- END OF ACTION ---
action966 = env.action_space()
action966.load_change_bus = [17]
action966.line_ex_change_bus = [18]
action966.line_ex_change_bus = [19]
action966.line_ex_change_bus = [20]
actions.append(action966)
# ---- END OF ACTION ---
action967 = env.action_space()
action967.gen_change_bus = [5]
action967.load_change_bus = [17]
action967.line_ex_change_bus = [19]
action967.line_or_change_bus = [22]
action967.line_or_change_bus = [23]
action967.line_or_change_bus = [48]
action967.line_or_change_bus = [49]
action967.line_or_change_bus = [54]
actions.append(action967)
# ---- END OF ACTION ---
action968 = env.action_space()
action968.gen_change_bus = [7]
action968.line_or_change_bus = [22]
action968.line_or_change_bus = [23]
action968.line_or_change_bus = [28]
actions.append(action968)
# ---- END OF ACTION ---
action969 = env.action_space()
action969.gen_change_bus = [5]
action969.line_or_change_bus = [22]
action969.line_or_change_bus = [23]
action969.line_or_change_bus = [27]
action969.line_or_change_bus = [28]
action969.line_or_change_bus = [48]
action969.line_or_change_bus = [49]
actions.append(action969)
# ---- END OF ACTION ---
action970 = env.action_space()
action970.gen_change_bus = [7]
action970.load_change_bus = [17]
action970.line_ex_change_bus = [18]
action970.line_ex_change_bus = [19]
action970.line_ex_change_bus = [20]
action970.line_or_change_bus = [22]
action970.line_or_change_bus = [23]
action970.line_or_change_bus = [27]
action970.line_or_change_bus = [28]
action970.line_or_change_bus = [48]
action970.line_or_change_bus = [49]
action970.line_or_change_bus = [54]
actions.append(action970)
# ---- END OF ACTION ---
action971 = env.action_space()
action971.gen_change_bus = [5]
action971.gen_change_bus = [6]
action971.gen_change_bus = [7]
action971.gen_change_bus = [8]
action971.load_change_bus = [17]
action971.line_ex_change_bus = [19]
action971.line_ex_change_bus = [20]
action971.line_or_change_bus = [22]
action971.line_or_change_bus = [23]
action971.line_or_change_bus = [27]
action971.line_or_change_bus = [28]
action971.line_or_change_bus = [49]
actions.append(action971)
# ---- END OF ACTION ---
action972 = env.action_space()
action972.line_or_change_bus = [55]
actions.append(action972)
# ---- END OF ACTION ---
action973 = env.action_space()
action973.gen_change_bus = [6]
action973.gen_change_bus = [7]
action973.load_change_bus = [17]
action973.line_ex_change_bus = [18]
action973.line_ex_change_bus = [19]
action973.line_or_change_bus = [22]
action973.line_or_change_bus = [23]
action973.line_or_change_bus = [28]
action973.line_or_change_bus = [48]
action973.line_or_change_bus = [49]
actions.append(action973)
# ---- END OF ACTION ---
action974 = env.action_space()
action974.gen_change_bus = [7]
action974.load_change_bus = [17]
action974.line_ex_change_bus = [18]
action974.line_ex_change_bus = [19]
action974.line_or_change_bus = [22]
action974.line_or_change_bus = [23]
action974.line_or_change_bus = [48]
action974.line_or_change_bus = [49]
action974.line_or_change_bus = [54]
actions.append(action974)
# ---- END OF ACTION ---
action975 = env.action_space()
action975.gen_change_bus = [6]
action975.gen_change_bus = [7]
action975.load_change_bus = [17]
action975.line_ex_change_bus = [18]
action975.line_ex_change_bus = [19]
action975.line_or_change_bus = [22]
action975.line_or_change_bus = [23]
action975.line_or_change_bus = [27]
action975.line_or_change_bus = [28]
action975.line_or_change_bus = [48]
action975.line_or_change_bus = [49]
action975.line_or_change_bus = [54]
actions.append(action975)
# ---- END OF ACTION ---
action976 = env.action_space()
action976.load_change_bus = [31]
action976.line_ex_change_bus = [49]
action976.line_or_change_bus = [52]
actions.append(action976)
# ---- END OF ACTION ---
action977 = env.action_space()
action977.gen_change_bus = [5]
action977.gen_change_bus = [8]
action977.load_change_bus = [17]
action977.line_ex_change_bus = [21]
action977.line_or_change_bus = [22]
action977.line_or_change_bus = [23]
action977.line_or_change_bus = [48]
action977.line_or_change_bus = [49]
action977.line_or_change_bus = [54]
actions.append(action977)
# ---- END OF ACTION ---
action978 = env.action_space()
action978.gen_change_bus = [5]
action978.load_change_bus = [17]
action978.line_ex_change_bus = [21]
action978.line_or_change_bus = [27]
actions.append(action978)
# ---- END OF ACTION ---
action979 = env.action_space()
action979.line_ex_change_bus = [20]
action979.line_or_change_bus = [22]
action979.line_or_change_bus = [23]
actions.append(action979)
# ---- END OF ACTION ---
action980 = env.action_space()
action980.gen_change_bus = [5]
action980.gen_change_bus = [6]
action980.gen_change_bus = [8]
action980.load_change_bus = [17]
action980.line_ex_change_bus = [18]
action980.line_ex_change_bus = [19]
action980.line_ex_change_bus = [21]
action980.line_or_change_bus = [22]
action980.line_or_change_bus = [23]
action980.line_or_change_bus = [28]
action980.line_or_change_bus = [48]
action980.line_or_change_bus = [49]
action980.line_or_change_bus = [54]
actions.append(action980)
# ---- END OF ACTION ---
action981 = env.action_space()
action981.load_change_bus = [2]
action981.load_change_bus = [3]
action981.line_or_change_bus = [4]
action981.line_or_change_bus = [12]
actions.append(action981)
# ---- END OF ACTION ---
action982 = env.action_space()
action982.gen_change_bus = [5]
action982.gen_change_bus = [7]
action982.gen_change_bus = [8]
action982.load_change_bus = [17]
action982.line_ex_change_bus = [18]
action982.line_ex_change_bus = [19]
action982.line_or_change_bus = [27]
action982.line_or_change_bus = [28]
action982.line_or_change_bus = [54]
actions.append(action982)
# ---- END OF ACTION ---
action983 = env.action_space()
action983.gen_change_bus = [6]
action983.load_change_bus = [17]
action983.line_or_change_bus = [22]
action983.line_or_change_bus = [23]
action983.line_or_change_bus = [48]
action983.line_or_change_bus = [49]
actions.append(action983)
# ---- END OF ACTION ---
action984 = env.action_space()
action984.line_ex_change_bus = [18]
action984.line_or_change_bus = [28]
action984.line_or_change_bus = [49]
actions.append(action984)
# ---- END OF ACTION ---
action985 = env.action_space()
action985.gen_change_bus = [7]
action985.line_ex_change_bus = [19]
action985.line_or_change_bus = [22]
action985.line_or_change_bus = [23]
action985.line_or_change_bus = [49]
actions.append(action985)
# ---- END OF ACTION ---
action986 = env.action_space()
action986.gen_change_bus = [13]
action986.load_change_bus = [24]
action986.line_or_change_bus = [37]
actions.append(action986)
# ---- END OF ACTION ---
action987 = env.action_space()
action987.gen_change_bus = [5]
action987.gen_change_bus = [7]
action987.gen_change_bus = [8]
action987.load_change_bus = [17]
action987.line_or_change_bus = [22]
action987.line_or_change_bus = [23]
action987.line_or_change_bus = [48]
action987.line_or_change_bus = [49]
actions.append(action987)
# ---- END OF ACTION ---
action988 = env.action_space()
action988.gen_change_bus = [5]
action988.gen_change_bus = [6]
action988.gen_change_bus = [7]
actions.append(action988)
# ---- END OF ACTION ---
action989 = env.action_space()
action989.load_change_bus = [25]
action989.line_ex_change_bus = [33]
actions.append(action989)
# ---- END OF ACTION ---
action990 = env.action_space()
action990.line_or_change_bus = [27]
action990.line_or_change_bus = [28]
action990.line_or_change_bus = [54]
actions.append(action990)
# ---- END OF ACTION ---
action991 = env.action_space()
action991.gen_change_bus = [5]
action991.gen_change_bus = [8]
action991.load_change_bus = [17]
action991.line_ex_change_bus = [19]
action991.line_ex_change_bus = [20]
action991.line_or_change_bus = [22]
action991.line_or_change_bus = [23]
action991.line_or_change_bus = [49]
action991.line_or_change_bus = [54]
actions.append(action991)
# ---- END OF ACTION ---
action992 = env.action_space()
action992.gen_change_bus = [7]
action992.line_ex_change_bus = [20]
action992.line_or_change_bus = [22]
action992.line_or_change_bus = [23]
action992.line_or_change_bus = [48]
action992.line_or_change_bus = [49]
actions.append(action992)
# ---- END OF ACTION ---
action993 = env.action_space()
action993.gen_change_bus = [9]
action993.load_change_bus = [22]
action993.line_ex_change_bus = [27]
action993.line_or_change_bus = [29]
action993.line_or_change_bus = [30]
actions.append(action993)
# ---- END OF ACTION ---
action994 = env.action_space()
action994.line_ex_change_bus = [19]
action994.line_ex_change_bus = [20]
actions.append(action994)
# ---- END OF ACTION ---
action995 = env.action_space()
action995.gen_change_bus = [5]
action995.gen_change_bus = [6]
action995.gen_change_bus = [7]
action995.gen_change_bus = [8]
action995.load_change_bus = [17]
action995.line_ex_change_bus = [18]
action995.line_ex_change_bus = [19]
action995.line_ex_change_bus = [20]
action995.line_or_change_bus = [22]
action995.line_or_change_bus = [23]
action995.line_or_change_bus = [28]
action995.line_or_change_bus = [48]
action995.line_or_change_bus = [49]
actions.append(action995)
# ---- END OF ACTION ---
action996 = env.action_space()
action996.gen_change_bus = [5]
action996.gen_change_bus = [8]
action996.load_change_bus = [17]
action996.line_ex_change_bus = [19]
action996.line_or_change_bus = [22]
action996.line_or_change_bus = [23]
action996.line_or_change_bus = [49]
actions.append(action996)
# ---- END OF ACTION ---
action997 = env.action_space()
action997.line_ex_change_bus = [20]
action997.line_or_change_bus = [49]
actions.append(action997)
# ---- END OF ACTION ---
action998 = env.action_space()
action998.gen_change_bus = [5]
action998.line_ex_change_bus = [18]
action998.line_ex_change_bus = [19]
action998.line_or_change_bus = [49]
actions.append(action998)
# ---- END OF ACTION ---
action999 = env.action_space()
action999.gen_change_bus = [13]
action999.load_change_bus = [24]
action999.line_ex_change_bus = [31]
action999.line_or_change_bus = [32]
actions.append(action999)
# ---- END OF ACTION ---
action1000 = env.action_space()
action1000.gen_change_bus = [17]
action1000.load_change_bus = [29]
action1000.line_ex_change_bus = [44]
action1000.line_or_change_bus = [50]
action1000.line_or_change_bus = [51]
actions.append(action1000)
# ---- END OF ACTION ---
action1001 = env.action_space()
action1001.gen_change_bus = [6]
action1001.gen_change_bus = [7]
action1001.gen_change_bus = [8]
action1001.load_change_bus = [17]
action1001.line_ex_change_bus = [19]
action1001.line_ex_change_bus = [20]
action1001.line_or_change_bus = [22]
action1001.line_or_change_bus = [23]
action1001.line_or_change_bus = [49]
actions.append(action1001)
# ---- END OF ACTION ---
action1002 = env.action_space()
action1002.load_change_bus = [17]
action1002.line_ex_change_bus = [18]
action1002.line_ex_change_bus = [19]
action1002.line_ex_change_bus = [20]
action1002.line_or_change_bus = [23]
action1002.line_or_change_bus = [28]
action1002.line_or_change_bus = [48]
action1002.line_or_change_bus = [49]
actions.append(action1002)
# ---- END OF ACTION ---
action1003 = env.action_space()
action1003.gen_change_bus = [5]
action1003.gen_change_bus = [7]
action1003.gen_change_bus = [8]
action1003.line_ex_change_bus = [19]
action1003.line_or_change_bus = [22]
action1003.line_or_change_bus = [23]
action1003.line_or_change_bus = [48]
action1003.line_or_change_bus = [49]
action1003.line_or_change_bus = [54]
actions.append(action1003)
# ---- END OF ACTION ---
action1004 = env.action_space()
action1004.gen_change_bus = [5]
action1004.gen_change_bus = [8]
action1004.load_change_bus = [17]
action1004.line_ex_change_bus = [18]
action1004.line_ex_change_bus = [19]
action1004.line_ex_change_bus = [20]
action1004.line_or_change_bus = [22]
action1004.line_or_change_bus = [28]
actions.append(action1004)
# ---- END OF ACTION ---
action1005 = env.action_space()
action1005.gen_change_bus = [7]
action1005.line_ex_change_bus = [18]
action1005.line_ex_change_bus = [19]
action1005.line_ex_change_bus = [20]
action1005.line_or_change_bus = [22]
action1005.line_or_change_bus = [23]
action1005.line_or_change_bus = [27]
action1005.line_or_change_bus = [28]
action1005.line_or_change_bus = [48]
action1005.line_or_change_bus = [49]
actions.append(action1005)
# ---- END OF ACTION ---
action1006 = env.action_space()
action1006.gen_change_bus = [8]
action1006.load_change_bus = [17]
action1006.line_ex_change_bus = [20]
action1006.line_or_change_bus = [27]
action1006.line_or_change_bus = [28]
action1006.line_or_change_bus = [49]
action1006.line_or_change_bus = [54]
actions.append(action1006)
# ---- END OF ACTION ---
action1007 = env.action_space()
action1007.gen_change_bus = [14]
action1007.load_change_bus = [27]
action1007.line_ex_change_bus = [38]
action1007.line_or_change_bus = [41]
action1007.line_ex_change_bus = [56]
actions.append(action1007)
# ---- END OF ACTION ---
action1008 = env.action_space()
action1008.gen_change_bus = [6]
action1008.load_change_bus = [17]
action1008.line_ex_change_bus = [20]
actions.append(action1008)
# ---- END OF ACTION ---
action1009 = env.action_space()
action1009.gen_change_bus = [5]
action1009.gen_change_bus = [8]
action1009.load_change_bus = [17]
action1009.line_ex_change_bus = [18]
action1009.line_ex_change_bus = [19]
action1009.line_or_change_bus = [22]
action1009.line_or_change_bus = [23]
action1009.line_or_change_bus = [28]
action1009.line_or_change_bus = [49]
actions.append(action1009)
# ---- END OF ACTION ---
action1010 = env.action_space()
action1010.gen_change_bus = [5]
action1010.load_change_bus = [17]
action1010.line_ex_change_bus = [20]
action1010.line_or_change_bus = [54]
actions.append(action1010)
# ---- END OF ACTION ---
action1011 = env.action_space()
action1011.gen_change_bus = [17]
action1011.load_change_bus = [29]
action1011.line_ex_change_bus = [44]
actions.append(action1011)
# ---- END OF ACTION ---
action1012 = env.action_space()
action1012.line_ex_change_bus = [52]
actions.append(action1012)
# ---- END OF ACTION ---
action1013 = env.action_space()
action1013.gen_change_bus = [21]
action1013.load_change_bus = [33]
action1013.load_change_bus = [34]
action1013.line_ex_change_bus = [54]
actions.append(action1013)
# ---- END OF ACTION ---
action1014 = env.action_space()
action1014.gen_change_bus = [2]
action1014.gen_change_bus = [3]
action1014.line_ex_change_bus = [10]
action1014.line_or_change_bus = [18]
actions.append(action1014)
# ---- END OF ACTION ---
action1015 = env.action_space()
action1015.line_ex_change_bus = [19]
action1015.line_or_change_bus = [22]
action1015.line_or_change_bus = [23]
action1015.line_or_change_bus = [27]
action1015.line_or_change_bus = [28]
action1015.line_or_change_bus = [54]
actions.append(action1015)
# ---- END OF ACTION ---
action1016 = env.action_space()
action1016.load_change_bus = [17]
action1016.line_ex_change_bus = [19]
action1016.line_or_change_bus = [23]
action1016.line_or_change_bus = [28]
actions.append(action1016)
# ---- END OF ACTION ---
action1017 = env.action_space()
action1017.load_change_bus = [15]
action1017.line_or_change_bus = [17]
action1017.line_or_change_bus = [53]
actions.append(action1017)
# ---- END OF ACTION ---
action1018 = env.action_space()
action1018.gen_change_bus = [6]
action1018.gen_change_bus = [7]
action1018.line_or_change_bus = [49]
actions.append(action1018)
# ---- END OF ACTION ---
action1019 = env.action_space()
action1019.gen_change_bus = [6]
action1019.gen_change_bus = [8]
action1019.line_ex_change_bus = [19]
action1019.line_or_change_bus = [22]
action1019.line_or_change_bus = [23]
action1019.line_or_change_bus = [54]
actions.append(action1019)
# ---- END OF ACTION ---
action1020 = env.action_space()
action1020.load_change_bus = [24]
action1020.line_ex_change_bus = [31]
action1020.line_or_change_bus = [34]
action1020.line_or_change_bus = [37]
action1020.line_or_change_bus = [38]
actions.append(action1020)
# ---- END OF ACTION ---
action1021 = env.action_space()
action1021.load_change_bus = [17]
action1021.line_ex_change_bus = [19]
action1021.line_ex_change_bus = [20]
action1021.line_or_change_bus = [27]
action1021.line_or_change_bus = [48]
action1021.line_or_change_bus = [49]
action1021.line_or_change_bus = [54]
actions.append(action1021)
# ---- END OF ACTION ---
action1022 = env.action_space()
action1022.gen_change_bus = [11]
action1022.gen_change_bus = [13]
action1022.line_or_change_bus = [32]
action1022.line_or_change_bus = [34]
action1022.line_or_change_bus = [38]
actions.append(action1022)
# ---- END OF ACTION ---
action1023 = env.action_space()
action1023.line_ex_change_bus = [20]
action1023.line_or_change_bus = [22]
action1023.line_or_change_bus = [54]
actions.append(action1023)
# ---- END OF ACTION ---
action1024 = env.action_space()
action1024.line_or_change_bus = [28]
action1024.line_or_change_bus = [48]
actions.append(action1024)
# ---- END OF ACTION ---
action1025 = env.action_space()
action1025.gen_change_bus = [9]
action1025.load_change_bus = [22]
action1025.line_or_change_bus = [29]
action1025.line_or_change_bus = [36]
actions.append(action1025)
# ---- END OF ACTION ---
action1026 = env.action_space()
action1026.load_change_bus = [17]
action1026.line_ex_change_bus = [20]
action1026.line_or_change_bus = [28]
action1026.line_or_change_bus = [49]
actions.append(action1026)
# ---- END OF ACTION ---
action1027 = env.action_space()
action1027.gen_change_bus = [5]
action1027.load_change_bus = [17]
action1027.line_or_change_bus = [22]
action1027.line_or_change_bus = [23]
action1027.line_or_change_bus = [48]
action1027.line_or_change_bus = [49]
action1027.line_or_change_bus = [54]
actions.append(action1027)
# ---- END OF ACTION ---
action1028 = env.action_space()
action1028.gen_change_bus = [5]
action1028.gen_change_bus = [8]
action1028.line_ex_change_bus = [18]
action1028.line_ex_change_bus = [19]
action1028.line_ex_change_bus = [20]
action1028.line_or_change_bus = [22]
action1028.line_or_change_bus = [23]
action1028.line_or_change_bus = [28]
action1028.line_or_change_bus = [48]
action1028.line_or_change_bus = [49]
action1028.line_or_change_bus = [54]
actions.append(action1028)
# ---- END OF ACTION ---
action1029 = env.action_space()
action1029.gen_change_bus = [5]
action1029.gen_change_bus = [6]
action1029.gen_change_bus = [8]
action1029.load_change_bus = [17]
action1029.line_ex_change_bus = [18]
action1029.line_ex_change_bus = [19]
action1029.line_ex_change_bus = [20]
action1029.line_or_change_bus = [22]
action1029.line_or_change_bus = [23]
action1029.line_or_change_bus = [27]
action1029.line_or_change_bus = [28]
action1029.line_or_change_bus = [48]
action1029.line_or_change_bus = [49]
actions.append(action1029)
# ---- END OF ACTION ---
action1030 = env.action_space()
action1030.gen_change_bus = [5]
action1030.gen_change_bus = [8]
action1030.load_change_bus = [17]
action1030.line_ex_change_bus = [19]
action1030.line_ex_change_bus = [20]
action1030.line_or_change_bus = [48]
action1030.line_or_change_bus = [49]
actions.append(action1030)
# ---- END OF ACTION ---
action1031 = env.action_space()
action1031.gen_change_bus = [7]
action1031.line_ex_change_bus = [18]
actions.append(action1031)
# ---- END OF ACTION ---
action1032 = env.action_space()
action1032.load_change_bus = [27]
action1032.line_ex_change_bus = [37]
action1032.line_ex_change_bus = [38]
action1032.line_ex_change_bus = [39]
action1032.line_ex_change_bus = [56]
actions.append(action1032)
# ---- END OF ACTION ---
action1033 = env.action_space()
action1033.gen_change_bus = [20]
action1033.line_ex_change_bus = [58]
actions.append(action1033)
# ---- END OF ACTION ---
action1034 = env.action_space()
action1034.load_change_bus = [27]
action1034.line_ex_change_bus = [37]
action1034.line_or_change_bus = [40]
action1034.line_or_change_bus = [41]
action1034.line_ex_change_bus = [56]
actions.append(action1034)
# ---- END OF ACTION ---
action1035 = env.action_space()
action1035.gen_change_bus = [6]
action1035.gen_change_bus = [7]
action1035.line_ex_change_bus = [20]
action1035.line_or_change_bus = [27]
action1035.line_or_change_bus = [28]
action1035.line_or_change_bus = [54]
actions.append(action1035)
# ---- END OF ACTION ---
action1036 = env.action_space()
action1036.gen_change_bus = [1]
action1036.line_ex_change_bus = [7]
action1036.line_or_change_bus = [9]
actions.append(action1036)
# ---- END OF ACTION ---
action1037 = env.action_space()
action1037.gen_change_bus = [0]
actions.append(action1037)
# ---- END OF ACTION ---
action1038 = env.action_space()
action1038.gen_change_bus = [5]
action1038.gen_change_bus = [6]
action1038.gen_change_bus = [7]
action1038.gen_change_bus = [8]
action1038.line_ex_change_bus = [18]
action1038.line_ex_change_bus = [19]
action1038.line_ex_change_bus = [20]
action1038.line_or_change_bus = [54]
actions.append(action1038)
# ---- END OF ACTION ---
action1039 = env.action_space()
action1039.line_ex_change_bus = [31]
action1039.line_or_change_bus = [32]
action1039.line_or_change_bus = [37]
actions.append(action1039)
# ---- END OF ACTION ---
action1040 = env.action_space()
action1040.gen_change_bus = [12]
action1040.gen_change_bus = [13]
action1040.line_or_change_bus = [34]
actions.append(action1040)
# ---- END OF ACTION ---
action1041 = env.action_space()
action1041.line_ex_change_bus = [18]
action1041.line_ex_change_bus = [19]
action1041.line_or_change_bus = [22]
action1041.line_or_change_bus = [23]
action1041.line_or_change_bus = [28]
action1041.line_or_change_bus = [48]
action1041.line_or_change_bus = [49]
action1041.line_or_change_bus = [54]
actions.append(action1041)
# ---- END OF ACTION ---
action1042 = env.action_space()
action1042.gen_change_bus = [18]
action1042.load_change_bus = [29]
action1042.line_ex_change_bus = [44]
action1042.line_or_change_bus = [50]
action1042.line_or_change_bus = [51]
actions.append(action1042)
# ---- END OF ACTION ---
action1043 = env.action_space()
action1043.gen_change_bus = [5]
action1043.gen_change_bus = [6]
action1043.gen_change_bus = [7]
action1043.gen_change_bus = [8]
action1043.line_ex_change_bus = [18]
action1043.line_ex_change_bus = [19]
action1043.line_ex_change_bus = [20]
action1043.line_ex_change_bus = [21]
action1043.line_or_change_bus = [22]
action1043.line_or_change_bus = [23]
actions.append(action1043)
# ---- END OF ACTION ---
action1044 = env.action_space()
action1044.load_change_bus = [22]
action1044.line_ex_change_bus = [27]
action1044.line_or_change_bus = [30]
action1044.line_or_change_bus = [36]
actions.append(action1044)
# ---- END OF ACTION ---
action1045 = env.action_space()
action1045.gen_change_bus = [6]
action1045.gen_change_bus = [7]
action1045.gen_change_bus = [8]
action1045.load_change_bus = [17]
action1045.line_ex_change_bus = [18]
action1045.line_ex_change_bus = [19]
action1045.line_ex_change_bus = [20]
action1045.line_or_change_bus = [22]
action1045.line_or_change_bus = [23]
action1045.line_or_change_bus = [28]
action1045.line_or_change_bus = [48]
action1045.line_or_change_bus = [49]
action1045.line_or_change_bus = [54]
actions.append(action1045)
# ---- END OF ACTION ---
action1046 = env.action_space()
action1046.gen_change_bus = [5]
action1046.gen_change_bus = [6]
action1046.gen_change_bus = [7]
action1046.load_change_bus = [17]
action1046.line_ex_change_bus = [18]
action1046.line_ex_change_bus = [19]
action1046.line_or_change_bus = [22]
action1046.line_or_change_bus = [23]
action1046.line_or_change_bus = [27]
action1046.line_or_change_bus = [28]
action1046.line_or_change_bus = [48]
action1046.line_or_change_bus = [49]
action1046.line_or_change_bus = [54]
actions.append(action1046)
# ---- END OF ACTION ---
action1047 = env.action_space()
action1047.gen_change_bus = [5]
action1047.gen_change_bus = [8]
action1047.load_change_bus = [17]
action1047.line_ex_change_bus = [18]
action1047.line_ex_change_bus = [19]
action1047.line_ex_change_bus = [20]
action1047.line_ex_change_bus = [21]
action1047.line_or_change_bus = [22]
action1047.line_or_change_bus = [23]
action1047.line_or_change_bus = [27]
action1047.line_or_change_bus = [28]
action1047.line_or_change_bus = [49]
actions.append(action1047)
# ---- END OF ACTION ---
action1048 = env.action_space()
action1048.gen_change_bus = [8]
action1048.line_ex_change_bus = [21]
action1048.line_or_change_bus = [54]
actions.append(action1048)
# ---- END OF ACTION ---
action1049 = env.action_space()
action1049.line_or_change_bus = [17]
actions.append(action1049)
# ---- END OF ACTION ---
action1050 = env.action_space()
action1050.load_change_bus = [10]
action1050.line_or_change_bus = [18]
action1050.line_or_change_bus = [19]
actions.append(action1050)
# ---- END OF ACTION ---
action1051 = env.action_space()
action1051.gen_change_bus = [6]
action1051.gen_change_bus = [7]
action1051.load_change_bus = [17]
action1051.line_or_change_bus = [54]
actions.append(action1051)
# ---- END OF ACTION ---
action1052 = env.action_space()
action1052.gen_change_bus = [5]
action1052.gen_change_bus = [8]
action1052.line_or_change_bus = [22]
action1052.line_or_change_bus = [28]
actions.append(action1052)
# ---- END OF ACTION ---
action1053 = env.action_space()
action1053.line_ex_change_bus = [27]
action1053.line_or_change_bus = [30]
actions.append(action1053)
# ---- END OF ACTION ---
action1054 = env.action_space()
action1054.gen_change_bus = [5]
action1054.load_change_bus = [17]
action1054.line_ex_change_bus = [20]
action1054.line_or_change_bus = [22]
action1054.line_or_change_bus = [23]
action1054.line_or_change_bus = [48]
action1054.line_or_change_bus = [49]
actions.append(action1054)
# ---- END OF ACTION ---
action1055 = env.action_space()
action1055.gen_change_bus = [13]
action1055.load_change_bus = [24]
action1055.line_ex_change_bus = [31]
action1055.line_or_change_bus = [34]
action1055.line_or_change_bus = [38]
actions.append(action1055)
# ---- END OF ACTION ---
action1056 = env.action_space()
action1056.gen_change_bus = [5]
action1056.gen_change_bus = [8]
action1056.load_change_bus = [17]
action1056.line_ex_change_bus = [18]
action1056.line_ex_change_bus = [19]
action1056.line_or_change_bus = [22]
action1056.line_or_change_bus = [23]
action1056.line_or_change_bus = [48]
action1056.line_or_change_bus = [49]
action1056.line_or_change_bus = [54]
actions.append(action1056)
# ---- END OF ACTION ---
action1057 = env.action_space()
action1057.gen_change_bus = [8]
action1057.line_or_change_bus = [22]
action1057.line_or_change_bus = [23]
action1057.line_or_change_bus = [54]
actions.append(action1057)
# ---- END OF ACTION ---
action1058 = env.action_space()
action1058.gen_change_bus = [12]
action1058.line_or_change_bus = [32]
action1058.line_or_change_bus = [34]
action1058.line_or_change_bus = [38]
actions.append(action1058)
# ---- END OF ACTION ---
action1059 = env.action_space()
action1059.gen_change_bus = [8]
action1059.load_change_bus = [17]
action1059.line_ex_change_bus = [19]
action1059.line_or_change_bus = [22]
action1059.line_or_change_bus = [23]
action1059.line_or_change_bus = [49]
actions.append(action1059)
# ---- END OF ACTION ---
action1060 = env.action_space()
action1060.gen_change_bus = [5]
action1060.gen_change_bus = [8]
action1060.load_change_bus = [17]
action1060.line_ex_change_bus = [18]
action1060.line_ex_change_bus = [19]
action1060.line_or_change_bus = [22]
action1060.line_or_change_bus = [23]
action1060.line_or_change_bus = [27]
action1060.line_or_change_bus = [28]
action1060.line_or_change_bus = [54]
actions.append(action1060)
# ---- END OF ACTION ---
action1061 = env.action_space()
action1061.gen_change_bus = [5]
action1061.gen_change_bus = [8]
action1061.line_ex_change_bus = [18]
action1061.line_ex_change_bus = [19]
action1061.line_or_change_bus = [22]
action1061.line_or_change_bus = [23]
action1061.line_or_change_bus = [27]
action1061.line_or_change_bus = [28]
action1061.line_or_change_bus = [48]
action1061.line_or_change_bus = [49]
action1061.line_or_change_bus = [54]
actions.append(action1061)
# ---- END OF ACTION ---
action1062 = env.action_space()
action1062.gen_change_bus = [7]
action1062.load_change_bus = [17]
action1062.line_ex_change_bus = [18]
action1062.line_ex_change_bus = [19]
action1062.line_or_change_bus = [22]
action1062.line_or_change_bus = [23]
action1062.line_or_change_bus = [49]
actions.append(action1062)
# ---- END OF ACTION ---
action1063 = env.action_space()
action1063.gen_change_bus = [5]
action1063.gen_change_bus = [6]
action1063.gen_change_bus = [7]
action1063.gen_change_bus = [8]
action1063.load_change_bus = [17]
action1063.line_ex_change_bus = [18]
action1063.line_ex_change_bus = [19]
action1063.line_or_change_bus = [27]
action1063.line_or_change_bus = [28]
actions.append(action1063)
# ---- END OF ACTION ---
action1064 = env.action_space()
action1064.gen_change_bus = [8]
action1064.line_ex_change_bus = [20]
action1064.line_ex_change_bus = [21]
action1064.line_or_change_bus = [22]
action1064.line_or_change_bus = [23]
action1064.line_or_change_bus = [28]
action1064.line_or_change_bus = [54]
actions.append(action1064)
# ---- END OF ACTION ---
action1065 = env.action_space()
action1065.line_or_change_bus = [29]
actions.append(action1065)
# ---- END OF ACTION ---
action1066 = env.action_space()
action1066.gen_change_bus = [20]
action1066.load_change_bus = [31]
action1066.line_ex_change_bus = [58]
actions.append(action1066)
# ---- END OF ACTION ---
action1067 = env.action_space()
action1067.line_ex_change_bus = [18]
action1067.line_ex_change_bus = [19]
action1067.line_or_change_bus = [22]
action1067.line_or_change_bus = [23]
action1067.line_or_change_bus = [48]
action1067.line_or_change_bus = [49]
action1067.line_or_change_bus = [54]
actions.append(action1067)
# ---- END OF ACTION ---
action1068 = env.action_space()
action1068.gen_change_bus = [11]
action1068.gen_change_bus = [13]
action1068.load_change_bus = [24]
action1068.line_or_change_bus = [34]
action1068.line_or_change_bus = [37]
action1068.line_or_change_bus = [38]
actions.append(action1068)
# ---- END OF ACTION ---
action1069 = env.action_space()
action1069.gen_change_bus = [5]
action1069.gen_change_bus = [7]
action1069.gen_change_bus = [8]
action1069.load_change_bus = [17]
actions.append(action1069)
# ---- END OF ACTION ---
action1070 = env.action_space()
action1070.gen_change_bus = [18]
action1070.load_change_bus = [29]
action1070.line_ex_change_bus = [44]
action1070.line_or_change_bus = [51]
actions.append(action1070)
# ---- END OF ACTION ---
action1071 = env.action_space()
action1071.load_change_bus = [17]
action1071.line_ex_change_bus = [18]
action1071.line_ex_change_bus = [19]
action1071.line_or_change_bus = [48]
action1071.line_or_change_bus = [49]
action1071.line_or_change_bus = [54]
actions.append(action1071)
# ---- END OF ACTION ---
action1072 = env.action_space()
action1072.gen_change_bus = [7]
action1072.load_change_bus = [17]
action1072.line_ex_change_bus = [18]
action1072.line_ex_change_bus = [19]
action1072.line_ex_change_bus = [21]
action1072.line_or_change_bus = [22]
action1072.line_or_change_bus = [23]
action1072.line_or_change_bus = [27]
action1072.line_or_change_bus = [28]
action1072.line_or_change_bus = [48]
action1072.line_or_change_bus = [49]
action1072.line_or_change_bus = [54]
actions.append(action1072)
# ---- END OF ACTION ---
action1073 = env.action_space()
action1073.gen_change_bus = [6]
action1073.gen_change_bus = [7]
action1073.line_ex_change_bus = [18]
action1073.line_ex_change_bus = [19]
action1073.line_or_change_bus = [22]
action1073.line_or_change_bus = [23]
action1073.line_or_change_bus = [28]
action1073.line_or_change_bus = [48]
action1073.line_or_change_bus = [49]
action1073.line_or_change_bus = [54]
actions.append(action1073)
# ---- END OF ACTION ---
action1074 = env.action_space()
action1074.gen_change_bus = [12]
action1074.gen_change_bus = [13]
action1074.line_ex_change_bus = [31]
action1074.line_or_change_bus = [32]
actions.append(action1074)
# ---- END OF ACTION ---
action1075 = env.action_space()
action1075.gen_change_bus = [5]
action1075.gen_change_bus = [6]
action1075.gen_change_bus = [7]
action1075.gen_change_bus = [8]
action1075.line_ex_change_bus = [20]
action1075.line_ex_change_bus = [21]
actions.append(action1075)
# ---- END OF ACTION ---
action1076 = env.action_space()
action1076.gen_change_bus = [5]
action1076.gen_change_bus = [6]
action1076.gen_change_bus = [7]
action1076.gen_change_bus = [8]
action1076.load_change_bus = [17]
action1076.line_ex_change_bus = [18]
action1076.line_ex_change_bus = [19]
action1076.line_ex_change_bus = [20]
action1076.line_or_change_bus = [22]
action1076.line_or_change_bus = [23]
action1076.line_or_change_bus = [27]
action1076.line_or_change_bus = [28]
action1076.line_or_change_bus = [48]
action1076.line_or_change_bus = [49]
actions.append(action1076)
# ---- END OF ACTION ---
action1077 = env.action_space()
action1077.line_or_change_bus = [27]
action1077.line_or_change_bus = [28]
action1077.line_or_change_bus = [48]
actions.append(action1077)
# ---- END OF ACTION ---
action1078 = env.action_space()
action1078.gen_change_bus = [11]
action1078.gen_change_bus = [13]
action1078.line_or_change_bus = [32]
action1078.line_or_change_bus = [37]
action1078.line_or_change_bus = [38]
actions.append(action1078)
# ---- END OF ACTION ---
action1079 = env.action_space()
action1079.gen_change_bus = [5]
action1079.line_ex_change_bus = [20]
action1079.line_ex_change_bus = [21]
action1079.line_or_change_bus = [27]
action1079.line_or_change_bus = [28]
actions.append(action1079)
# ---- END OF ACTION ---
action1080 = env.action_space()
action1080.gen_change_bus = [5]
action1080.gen_change_bus = [6]
action1080.gen_change_bus = [7]
action1080.gen_change_bus = [8]
action1080.load_change_bus = [17]
action1080.line_or_change_bus = [22]
action1080.line_or_change_bus = [23]
action1080.line_or_change_bus = [27]
action1080.line_or_change_bus = [28]
action1080.line_or_change_bus = [48]
action1080.line_or_change_bus = [49]
actions.append(action1080)
# ---- END OF ACTION ---
action1081 = env.action_space()
action1081.gen_change_bus = [12]
action1081.gen_change_bus = [13]
action1081.line_or_change_bus = [32]
actions.append(action1081)
# ---- END OF ACTION ---
action1082 = env.action_space()
action1082.line_or_change_bus = [22]
action1082.line_or_change_bus = [28]
actions.append(action1082)
# ---- END OF ACTION ---
action1083 = env.action_space()
action1083.gen_change_bus = [8]
action1083.line_ex_change_bus = [18]
action1083.line_or_change_bus = [54]
actions.append(action1083)
# ---- END OF ACTION ---
action1084 = env.action_space()
action1084.gen_change_bus = [8]
action1084.load_change_bus = [17]
action1084.line_or_change_bus = [28]
actions.append(action1084)
# ---- END OF ACTION ---
action1085 = env.action_space()
action1085.gen_change_bus = [5]
action1085.gen_change_bus = [8]
action1085.line_ex_change_bus = [20]
action1085.line_or_change_bus = [23]
action1085.line_or_change_bus = [48]
action1085.line_or_change_bus = [49]
actions.append(action1085)
# ---- END OF ACTION ---
action1086 = env.action_space()
action1086.gen_change_bus = [8]
action1086.load_change_bus = [17]
action1086.line_ex_change_bus = [18]
action1086.line_ex_change_bus = [19]
action1086.line_ex_change_bus = [21]
action1086.line_or_change_bus = [22]
action1086.line_or_change_bus = [23]
action1086.line_or_change_bus = [27]
action1086.line_or_change_bus = [28]
actions.append(action1086)
# ---- END OF ACTION ---
action1087 = env.action_space()
action1087.gen_change_bus = [7]
action1087.gen_change_bus = [8]
action1087.line_ex_change_bus = [18]
action1087.line_ex_change_bus = [19]
action1087.line_or_change_bus = [22]
action1087.line_or_change_bus = [23]
action1087.line_or_change_bus = [27]
action1087.line_or_change_bus = [28]
action1087.line_or_change_bus = [54]
actions.append(action1087)
# ---- END OF ACTION ---
action1088 = env.action_space()
action1088.gen_change_bus = [11]
action1088.gen_change_bus = [12]
action1088.line_or_change_bus = [34]
action1088.line_or_change_bus = [38]
actions.append(action1088)
# ---- END OF ACTION ---
action1089 = env.action_space()
action1089.gen_change_bus = [5]
action1089.gen_change_bus = [7]
action1089.line_ex_change_bus = [20]
actions.append(action1089)
# ---- END OF ACTION ---
action1090 = env.action_space()
action1090.gen_change_bus = [9]
action1090.line_or_change_bus = [29]
action1090.line_or_change_bus = [36]
actions.append(action1090)
# ---- END OF ACTION ---
action1091 = env.action_space()
action1091.gen_change_bus = [5]
action1091.gen_change_bus = [7]
action1091.gen_change_bus = [8]
action1091.load_change_bus = [17]
action1091.line_ex_change_bus = [19]
action1091.line_ex_change_bus = [20]
action1091.line_or_change_bus = [22]
action1091.line_or_change_bus = [23]
action1091.line_or_change_bus = [49]
action1091.line_or_change_bus = [54]
actions.append(action1091)
# ---- END OF ACTION ---
action1092 = env.action_space()
action1092.gen_change_bus = [7]
action1092.gen_change_bus = [8]
action1092.line_or_change_bus = [28]
action1092.line_or_change_bus = [49]
action1092.line_or_change_bus = [54]
actions.append(action1092)
# ---- END OF ACTION ---
action1093 = env.action_space()
action1093.gen_change_bus = [5]
action1093.gen_change_bus = [8]
action1093.load_change_bus = [17]
action1093.line_ex_change_bus = [19]
action1093.line_or_change_bus = [22]
action1093.line_or_change_bus = [23]
action1093.line_or_change_bus = [48]
action1093.line_or_change_bus = [49]
action1093.line_or_change_bus = [54]
actions.append(action1093)
# ---- END OF ACTION ---
action1094 = env.action_space()
action1094.gen_change_bus = [6]
action1094.gen_change_bus = [7]
action1094.gen_change_bus = [8]
action1094.load_change_bus = [17]
action1094.line_ex_change_bus = [18]
action1094.line_ex_change_bus = [19]
action1094.line_or_change_bus = [22]
action1094.line_or_change_bus = [23]
action1094.line_or_change_bus = [27]
action1094.line_or_change_bus = [28]
action1094.line_or_change_bus = [48]
action1094.line_or_change_bus = [49]
actions.append(action1094)
# ---- END OF ACTION ---
action1095 = env.action_space()
action1095.gen_change_bus = [5]
action1095.gen_change_bus = [8]
action1095.load_change_bus = [17]
action1095.line_or_change_bus = [22]
action1095.line_or_change_bus = [23]
action1095.line_or_change_bus = [28]
action1095.line_or_change_bus = [48]
action1095.line_or_change_bus = [49]
action1095.line_or_change_bus = [54]
actions.append(action1095)
# ---- END OF ACTION ---
action1096 = env.action_space()
action1096.gen_change_bus = [5]
action1096.gen_change_bus = [7]
action1096.load_change_bus = [17]
action1096.line_ex_change_bus = [18]
action1096.line_ex_change_bus = [19]
action1096.line_ex_change_bus = [20]
action1096.line_or_change_bus = [22]
action1096.line_or_change_bus = [23]
action1096.line_or_change_bus = [27]
action1096.line_or_change_bus = [28]
action1096.line_or_change_bus = [48]
action1096.line_or_change_bus = [49]
action1096.line_or_change_bus = [54]
actions.append(action1096)
# ---- END OF ACTION ---
action1097 = env.action_space()
action1097.gen_change_bus = [5]
action1097.gen_change_bus = [8]
action1097.load_change_bus = [17]
action1097.line_ex_change_bus = [19]
action1097.line_ex_change_bus = [20]
action1097.line_or_change_bus = [22]
action1097.line_or_change_bus = [23]
action1097.line_or_change_bus = [27]
action1097.line_or_change_bus = [28]
action1097.line_or_change_bus = [48]
action1097.line_or_change_bus = [49]
actions.append(action1097)
# ---- END OF ACTION ---
action1098 = env.action_space()
action1098.gen_change_bus = [5]
action1098.gen_change_bus = [7]
action1098.gen_change_bus = [8]
action1098.line_ex_change_bus = [18]
action1098.line_ex_change_bus = [19]
action1098.line_or_change_bus = [22]
action1098.line_or_change_bus = [23]
action1098.line_or_change_bus = [27]
actions.append(action1098)
# ---- END OF ACTION ---
action1099 = env.action_space()
action1099.gen_change_bus = [12]
action1099.load_change_bus = [24]
action1099.line_ex_change_bus = [31]
action1099.line_or_change_bus = [32]
action1099.line_or_change_bus = [34]
actions.append(action1099)
# ---- END OF ACTION ---
action1100 = env.action_space()
action1100.gen_change_bus = [5]
action1100.gen_change_bus = [6]
actions.append(action1100)
# ---- END OF ACTION ---
action1101 = env.action_space()
action1101.gen_change_bus = [8]
action1101.line_ex_change_bus = [21]
action1101.line_or_change_bus = [27]
action1101.line_or_change_bus = [28]
actions.append(action1101)
# ---- END OF ACTION ---
action1102 = env.action_space()
action1102.line_ex_change_bus = [20]
action1102.line_or_change_bus = [22]
action1102.line_or_change_bus = [27]
action1102.line_or_change_bus = [28]
actions.append(action1102)
# ---- END OF ACTION ---
action1103 = env.action_space()
action1103.load_change_bus = [17]
action1103.line_ex_change_bus = [18]
action1103.line_ex_change_bus = [19]
action1103.line_ex_change_bus = [20]
action1103.line_ex_change_bus = [21]
action1103.line_or_change_bus = [22]
action1103.line_or_change_bus = [27]
actions.append(action1103)
# ---- END OF ACTION ---
action1104 = env.action_space()
action1104.gen_change_bus = [14]
action1104.load_change_bus = [27]
action1104.line_ex_change_bus = [37]
action1104.line_ex_change_bus = [39]
action1104.line_or_change_bus = [40]
action1104.line_or_change_bus = [41]
actions.append(action1104)
# ---- END OF ACTION ---
action1105 = env.action_space()
action1105.gen_change_bus = [7]
action1105.line_ex_change_bus = [19]
action1105.line_or_change_bus = [22]
action1105.line_or_change_bus = [23]
action1105.line_or_change_bus = [27]
action1105.line_or_change_bus = [28]
action1105.line_or_change_bus = [48]
action1105.line_or_change_bus = [49]
actions.append(action1105)
# ---- END OF ACTION ---
action1106 = env.action_space()
action1106.gen_change_bus = [5]
action1106.gen_change_bus = [6]
action1106.load_change_bus = [17]
action1106.line_ex_change_bus = [18]
action1106.line_ex_change_bus = [19]
action1106.line_ex_change_bus = [20]
action1106.line_ex_change_bus = [21]
action1106.line_or_change_bus = [22]
action1106.line_or_change_bus = [23]
action1106.line_or_change_bus = [27]
action1106.line_or_change_bus = [28]
actions.append(action1106)
# ---- END OF ACTION ---
action1107 = env.action_space()
action1107.gen_change_bus = [13]
action1107.load_change_bus = [24]
action1107.line_ex_change_bus = [31]
action1107.line_or_change_bus = [34]
action1107.line_or_change_bus = [37]
action1107.line_or_change_bus = [38]
actions.append(action1107)
# ---- END OF ACTION ---
action1108 = env.action_space()
action1108.line_or_change_bus = [22]
actions.append(action1108)
# ---- END OF ACTION ---
action1109 = env.action_space()
action1109.load_change_bus = [24]
action1109.line_or_change_bus = [34]
action1109.line_or_change_bus = [37]
actions.append(action1109)
# ---- END OF ACTION ---
action1110 = env.action_space()
action1110.load_change_bus = [14]
action1110.line_or_change_bus = [15]
action1110.line_or_change_bus = [16]
actions.append(action1110)
# ---- END OF ACTION ---
action1111 = env.action_space()
action1111.gen_change_bus = [8]
action1111.load_change_bus = [17]
action1111.line_ex_change_bus = [18]
action1111.line_ex_change_bus = [19]
action1111.line_ex_change_bus = [20]
action1111.line_or_change_bus = [22]
action1111.line_or_change_bus = [27]
action1111.line_or_change_bus = [28]
action1111.line_or_change_bus = [48]
action1111.line_or_change_bus = [49]
actions.append(action1111)
# ---- END OF ACTION ---
action1112 = env.action_space()
action1112.gen_change_bus = [14]
action1112.load_change_bus = [27]
action1112.line_ex_change_bus = [38]
action1112.line_ex_change_bus = [39]
action1112.line_or_change_bus = [40]
actions.append(action1112)
# ---- END OF ACTION ---
action1113 = env.action_space()
action1113.gen_change_bus = [5]
action1113.gen_change_bus = [8]
action1113.load_change_bus = [17]
action1113.line_ex_change_bus = [19]
action1113.line_or_change_bus = [22]
action1113.line_or_change_bus = [23]
action1113.line_or_change_bus = [27]
action1113.line_or_change_bus = [28]
action1113.line_or_change_bus = [48]
action1113.line_or_change_bus = [49]
action1113.line_or_change_bus = [54]
actions.append(action1113)
# ---- END OF ACTION ---
action1114 = env.action_space()
action1114.gen_change_bus = [5]
action1114.gen_change_bus = [8]
action1114.load_change_bus = [17]
action1114.line_or_change_bus = [22]
action1114.line_or_change_bus = [23]
action1114.line_or_change_bus = [27]
actions.append(action1114)
# ---- END OF ACTION ---
action1115 = env.action_space()
action1115.load_change_bus = [24]
action1115.line_or_change_bus = [37]
actions.append(action1115)
# ---- END OF ACTION ---
action1116 = env.action_space()
action1116.gen_change_bus = [6]
action1116.gen_change_bus = [8]
action1116.load_change_bus = [17]
action1116.line_ex_change_bus = [19]
action1116.line_ex_change_bus = [20]
action1116.line_or_change_bus = [22]
action1116.line_or_change_bus = [23]
action1116.line_or_change_bus = [28]
action1116.line_or_change_bus = [48]
action1116.line_or_change_bus = [49]
action1116.line_or_change_bus = [54]
actions.append(action1116)
# ---- END OF ACTION ---
action1117 = env.action_space()
action1117.gen_change_bus = [5]
action1117.gen_change_bus = [6]
action1117.gen_change_bus = [7]
action1117.load_change_bus = [17]
action1117.line_ex_change_bus = [19]
action1117.line_or_change_bus = [22]
action1117.line_or_change_bus = [23]
action1117.line_or_change_bus = [48]
action1117.line_or_change_bus = [49]
action1117.line_or_change_bus = [54]
actions.append(action1117)
# ---- END OF ACTION ---
action1118 = env.action_space()
action1118.line_ex_change_bus = [19]
action1118.line_or_change_bus = [23]
action1118.line_or_change_bus = [48]
action1118.line_or_change_bus = [49]
action1118.line_or_change_bus = [54]
actions.append(action1118)
# ---- END OF ACTION ---
action1119 = env.action_space()
action1119.load_change_bus = [24]
action1119.line_ex_change_bus = [31]
action1119.line_or_change_bus = [32]
action1119.line_or_change_bus = [34]
action1119.line_or_change_bus = [37]
actions.append(action1119)
# ---- END OF ACTION ---
action1120 = env.action_space()
action1120.load_change_bus = [17]
action1120.line_ex_change_bus = [19]
action1120.line_or_change_bus = [22]
action1120.line_or_change_bus = [23]
action1120.line_or_change_bus = [28]
action1120.line_or_change_bus = [48]
action1120.line_or_change_bus = [49]
action1120.line_or_change_bus = [54]
actions.append(action1120)
# ---- END OF ACTION ---
action1121 = env.action_space()
action1121.gen_change_bus = [5]
action1121.gen_change_bus = [8]
action1121.load_change_bus = [17]
action1121.line_ex_change_bus = [20]
action1121.line_or_change_bus = [22]
action1121.line_or_change_bus = [23]
action1121.line_or_change_bus = [48]
action1121.line_or_change_bus = [49]
actions.append(action1121)
# ---- END OF ACTION ---
action1122 = env.action_space()
action1122.load_change_bus = [27]
action1122.line_ex_change_bus = [38]
action1122.line_or_change_bus = [41]
action1122.line_ex_change_bus = [56]
actions.append(action1122)
# ---- END OF ACTION ---
action1123 = env.action_space()
action1123.line_ex_change_bus = [18]
action1123.line_ex_change_bus = [19]
action1123.line_or_change_bus = [23]
action1123.line_or_change_bus = [48]
action1123.line_or_change_bus = [49]
action1123.line_or_change_bus = [54]
actions.append(action1123)
# ---- END OF ACTION ---
action1124 = env.action_space()
action1124.gen_change_bus = [5]
action1124.line_ex_change_bus = [19]
action1124.line_or_change_bus = [48]
action1124.line_or_change_bus = [49]
action1124.line_or_change_bus = [54]
actions.append(action1124)
# ---- END OF ACTION ---
action1125 = env.action_space()
action1125.gen_change_bus = [5]
action1125.gen_change_bus = [6]
action1125.gen_change_bus = [8]
action1125.load_change_bus = [17]
action1125.line_or_change_bus = [28]
action1125.line_or_change_bus = [48]
actions.append(action1125)
# ---- END OF ACTION ---
action1126 = env.action_space()
action1126.gen_change_bus = [13]
action1126.load_change_bus = [24]
action1126.line_ex_change_bus = [31]
action1126.line_or_change_bus = [34]
actions.append(action1126)
# ---- END OF ACTION ---
action1127 = env.action_space()
action1127.load_change_bus = [17]
action1127.line_ex_change_bus = [19]
action1127.line_or_change_bus = [22]
action1127.line_or_change_bus = [23]
action1127.line_or_change_bus = [27]
action1127.line_or_change_bus = [48]
action1127.line_or_change_bus = [49]
action1127.line_or_change_bus = [54]
actions.append(action1127)
# ---- END OF ACTION ---
action1128 = env.action_space()
action1128.gen_change_bus = [11]
action1128.gen_change_bus = [12]
action1128.gen_change_bus = [13]
action1128.line_ex_change_bus = [31]
action1128.line_or_change_bus = [32]
action1128.line_or_change_bus = [34]
actions.append(action1128)
# ---- END OF ACTION ---
action1129 = env.action_space()
action1129.gen_change_bus = [6]
action1129.gen_change_bus = [7]
action1129.line_or_change_bus = [22]
action1129.line_or_change_bus = [23]
actions.append(action1129)
# ---- END OF ACTION ---
action1130 = env.action_space()
action1130.gen_change_bus = [8]
action1130.load_change_bus = [17]
action1130.line_ex_change_bus = [20]
action1130.line_ex_change_bus = [21]
action1130.line_or_change_bus = [22]
action1130.line_or_change_bus = [23]
action1130.line_or_change_bus = [27]
action1130.line_or_change_bus = [49]
actions.append(action1130)
# ---- END OF ACTION ---
action1131 = env.action_space()
action1131.gen_change_bus = [17]
action1131.load_change_bus = [29]
action1131.line_or_change_bus = [50]
action1131.line_or_change_bus = [51]
actions.append(action1131)
# ---- END OF ACTION ---
action1132 = env.action_space()
action1132.load_change_bus = [17]
action1132.line_ex_change_bus = [18]
actions.append(action1132)
# ---- END OF ACTION ---
action1133 = env.action_space()
action1133.gen_change_bus = [9]
action1133.load_change_bus = [22]
action1133.line_ex_change_bus = [28]
action1133.line_or_change_bus = [30]
actions.append(action1133)
# ---- END OF ACTION ---
action1134 = env.action_space()
action1134.gen_change_bus = [5]
action1134.gen_change_bus = [6]
action1134.gen_change_bus = [7]
action1134.gen_change_bus = [8]
action1134.load_change_bus = [17]
action1134.line_ex_change_bus = [18]
action1134.line_ex_change_bus = [20]
action1134.line_ex_change_bus = [21]
action1134.line_or_change_bus = [23]
action1134.line_or_change_bus = [27]
action1134.line_or_change_bus = [28]
actions.append(action1134)
# ---- END OF ACTION ---
action1135 = env.action_space()
action1135.gen_change_bus = [5]
action1135.gen_change_bus = [8]
action1135.load_change_bus = [17]
action1135.line_ex_change_bus = [18]
action1135.line_ex_change_bus = [19]
action1135.line_ex_change_bus = [20]
action1135.line_ex_change_bus = [21]
action1135.line_or_change_bus = [22]
action1135.line_or_change_bus = [23]
action1135.line_or_change_bus = [28]
action1135.line_or_change_bus = [48]
action1135.line_or_change_bus = [49]
actions.append(action1135)
# ---- END OF ACTION ---
action1136 = env.action_space()
action1136.gen_change_bus = [5]
action1136.gen_change_bus = [6]
action1136.gen_change_bus = [7]
action1136.gen_change_bus = [8]
action1136.load_change_bus = [17]
action1136.line_ex_change_bus = [20]
action1136.line_or_change_bus = [22]
action1136.line_or_change_bus = [23]
action1136.line_or_change_bus = [27]
action1136.line_or_change_bus = [28]
action1136.line_or_change_bus = [49]
actions.append(action1136)
# ---- END OF ACTION ---
action1137 = env.action_space()
action1137.line_or_change_bus = [30]
actions.append(action1137)
# ---- END OF ACTION ---
action1138 = env.action_space()
action1138.line_ex_change_bus = [28]
action1138.line_or_change_bus = [30]
action1138.line_or_change_bus = [36]
actions.append(action1138)
# ---- END OF ACTION ---
action1139 = env.action_space()
action1139.gen_change_bus = [8]
action1139.line_ex_change_bus = [19]
action1139.line_or_change_bus = [54]
actions.append(action1139)
# ---- END OF ACTION ---
action1140 = env.action_space()
action1140.gen_change_bus = [8]
action1140.line_ex_change_bus = [20]
action1140.line_or_change_bus = [27]
actions.append(action1140)
# ---- END OF ACTION ---
action1141 = env.action_space()
action1141.load_change_bus = [17]
action1141.line_ex_change_bus = [19]
action1141.line_ex_change_bus = [21]
action1141.line_or_change_bus = [22]
action1141.line_or_change_bus = [23]
action1141.line_or_change_bus = [27]
action1141.line_or_change_bus = [28]
action1141.line_or_change_bus = [48]
action1141.line_or_change_bus = [49]
actions.append(action1141)
# ---- END OF ACTION ---
action1142 = env.action_space()
action1142.gen_change_bus = [5]
action1142.gen_change_bus = [7]
action1142.load_change_bus = [17]
action1142.line_ex_change_bus = [18]
action1142.line_ex_change_bus = [19]
action1142.line_or_change_bus = [22]
action1142.line_or_change_bus = [23]
action1142.line_or_change_bus = [27]
action1142.line_or_change_bus = [28]
action1142.line_or_change_bus = [48]
action1142.line_or_change_bus = [49]
action1142.line_or_change_bus = [54]
actions.append(action1142)
# ---- END OF ACTION ---
action1143 = env.action_space()
action1143.line_ex_change_bus = [4]
action1143.line_or_change_bus = [5]
actions.append(action1143)
# ---- END OF ACTION ---
action1144 = env.action_space()
action1144.gen_change_bus = [5]
action1144.gen_change_bus = [8]
action1144.line_ex_change_bus = [19]
action1144.line_ex_change_bus = [20]
action1144.line_or_change_bus = [54]
actions.append(action1144)
# ---- END OF ACTION ---
action1145 = env.action_space()
action1145.gen_change_bus = [20]
action1145.load_change_bus = [31]
action1145.line_or_change_bus = [52]
action1145.line_ex_change_bus = [58]
actions.append(action1145)
# ---- END OF ACTION ---
action1146 = env.action_space()
action1146.gen_change_bus = [12]
action1146.line_ex_change_bus = [31]
action1146.line_or_change_bus = [32]
action1146.line_or_change_bus = [37]
action1146.line_or_change_bus = [38]
actions.append(action1146)
# ---- END OF ACTION ---
action1147 = env.action_space()
action1147.gen_change_bus = [5]
action1147.load_change_bus = [17]
action1147.line_ex_change_bus = [19]
action1147.line_ex_change_bus = [20]
action1147.line_or_change_bus = [22]
action1147.line_or_change_bus = [23]
action1147.line_or_change_bus = [27]
action1147.line_or_change_bus = [28]
action1147.line_or_change_bus = [48]
action1147.line_or_change_bus = [49]
actions.append(action1147)
# ---- END OF ACTION ---
action1148 = env.action_space()
action1148.gen_change_bus = [5]
action1148.line_ex_change_bus = [19]
action1148.line_ex_change_bus = [20]
action1148.line_ex_change_bus = [21]
action1148.line_or_change_bus = [22]
action1148.line_or_change_bus = [23]
action1148.line_or_change_bus = [28]
actions.append(action1148)
# ---- END OF ACTION ---
action1149 = env.action_space()
action1149.load_change_bus = [16]
action1149.line_or_change_bus = [21]
actions.append(action1149)
# ---- END OF ACTION ---
action1150 = env.action_space()
action1150.gen_change_bus = [14]
action1150.load_change_bus = [27]
action1150.line_ex_change_bus = [37]
action1150.line_ex_change_bus = [38]
action1150.line_ex_change_bus = [39]
actions.append(action1150)
# ---- END OF ACTION ---
action1151 = env.action_space()
action1151.gen_change_bus = [6]
action1151.gen_change_bus = [7]
action1151.gen_change_bus = [8]
action1151.load_change_bus = [17]
action1151.line_ex_change_bus = [19]
action1151.line_ex_change_bus = [20]
action1151.line_or_change_bus = [22]
action1151.line_or_change_bus = [23]
action1151.line_or_change_bus = [48]
action1151.line_or_change_bus = [49]
action1151.line_or_change_bus = [54]
actions.append(action1151)
# ---- END OF ACTION ---
action1152 = env.action_space()
action1152.line_or_change_bus = [32]
action1152.line_or_change_bus = [38]
actions.append(action1152)
# ---- END OF ACTION ---
action1153 = env.action_space()
action1153.gen_change_bus = [5]
action1153.gen_change_bus = [6]
action1153.gen_change_bus = [7]
action1153.gen_change_bus = [8]
action1153.load_change_bus = [17]
action1153.line_or_change_bus = [27]
action1153.line_or_change_bus = [28]
action1153.line_or_change_bus = [48]
action1153.line_or_change_bus = [49]
action1153.line_or_change_bus = [54]
actions.append(action1153)
# ---- END OF ACTION ---
action1154 = env.action_space()
action1154.load_change_bus = [27]
action1154.line_or_change_bus = [41]
action1154.line_ex_change_bus = [56]
actions.append(action1154)
# ---- END OF ACTION ---
action1155 = env.action_space()
action1155.gen_change_bus = [5]
action1155.gen_change_bus = [8]
action1155.line_ex_change_bus = [21]
actions.append(action1155)
# ---- END OF ACTION ---
action1156 = env.action_space()
action1156.gen_change_bus = [11]
action1156.gen_change_bus = [12]
action1156.gen_change_bus = [13]
action1156.load_change_bus = [24]
action1156.line_or_change_bus = [32]
action1156.line_or_change_bus = [37]
actions.append(action1156)
# ---- END OF ACTION ---
action1157 = env.action_space()
action1157.gen_change_bus = [7]
action1157.gen_change_bus = [8]
action1157.load_change_bus = [17]
action1157.line_ex_change_bus = [18]
action1157.line_ex_change_bus = [19]
action1157.line_ex_change_bus = [20]
action1157.line_or_change_bus = [22]
action1157.line_or_change_bus = [23]
action1157.line_or_change_bus = [48]
action1157.line_or_change_bus = [49]
actions.append(action1157)
# ---- END OF ACTION ---
action1158 = env.action_space()
action1158.gen_change_bus = [5]
action1158.gen_change_bus = [7]
action1158.gen_change_bus = [8]
action1158.load_change_bus = [17]
action1158.line_ex_change_bus = [19]
action1158.line_or_change_bus = [22]
action1158.line_or_change_bus = [23]
actions.append(action1158)
# ---- END OF ACTION ---
action1159 = env.action_space()
action1159.load_change_bus = [24]
action1159.line_or_change_bus = [32]
action1159.line_or_change_bus = [37]
actions.append(action1159)
# ---- END OF ACTION ---
action1160 = env.action_space()
action1160.gen_change_bus = [6]
action1160.gen_change_bus = [8]
action1160.load_change_bus = [17]
action1160.line_ex_change_bus = [18]
action1160.line_ex_change_bus = [19]
action1160.line_ex_change_bus = [20]
action1160.line_or_change_bus = [22]
action1160.line_or_change_bus = [23]
action1160.line_or_change_bus = [27]
action1160.line_or_change_bus = [28]
action1160.line_or_change_bus = [48]
action1160.line_or_change_bus = [49]
actions.append(action1160)
# ---- END OF ACTION ---
action1161 = env.action_space()
action1161.gen_change_bus = [5]
action1161.gen_change_bus = [6]
action1161.gen_change_bus = [7]
action1161.gen_change_bus = [8]
action1161.load_change_bus = [17]
action1161.line_ex_change_bus = [19]
action1161.line_ex_change_bus = [20]
action1161.line_or_change_bus = [54]
actions.append(action1161)
# ---- END OF ACTION ---
action1162 = env.action_space()
action1162.gen_change_bus = [5]
action1162.gen_change_bus = [7]
action1162.gen_change_bus = [8]
action1162.load_change_bus = [17]
action1162.line_or_change_bus = [48]
action1162.line_or_change_bus = [49]
actions.append(action1162)
# ---- END OF ACTION ---
action1163 = env.action_space()
action1163.gen_change_bus = [6]
action1163.load_change_bus = [17]
action1163.line_ex_change_bus = [19]
actions.append(action1163)
# ---- END OF ACTION ---
action1164 = env.action_space()
action1164.line_ex_change_bus = [49]
action1164.line_ex_change_bus = [50]
action1164.line_or_change_bus = [52]
action1164.line_ex_change_bus = [58]
actions.append(action1164)
# ---- END OF ACTION ---
action1165 = env.action_space()
action1165.gen_change_bus = [11]
action1165.gen_change_bus = [12]
action1165.load_change_bus = [24]
action1165.line_ex_change_bus = [31]
actions.append(action1165)
# ---- END OF ACTION ---
action1166 = env.action_space()
action1166.gen_change_bus = [8]
action1166.line_ex_change_bus = [19]
action1166.line_ex_change_bus = [21]
action1166.line_or_change_bus = [49]
actions.append(action1166)
# ---- END OF ACTION ---
action1167 = env.action_space()
action1167.gen_change_bus = [5]
action1167.load_change_bus = [17]
action1167.line_ex_change_bus = [18]
action1167.line_ex_change_bus = [19]
action1167.line_or_change_bus = [22]
action1167.line_or_change_bus = [23]
action1167.line_or_change_bus = [27]
action1167.line_or_change_bus = [48]
action1167.line_or_change_bus = [49]
actions.append(action1167)
# ---- END OF ACTION ---
action1168 = env.action_space()
action1168.load_change_bus = [17]
action1168.line_or_change_bus = [22]
action1168.line_or_change_bus = [23]
action1168.line_or_change_bus = [27]
action1168.line_or_change_bus = [54]
actions.append(action1168)
# ---- END OF ACTION ---
action1169 = env.action_space()
action1169.gen_change_bus = [7]
action1169.load_change_bus = [17]
action1169.line_ex_change_bus = [18]
action1169.line_ex_change_bus = [19]
action1169.line_or_change_bus = [22]
action1169.line_or_change_bus = [23]
action1169.line_or_change_bus = [28]
action1169.line_or_change_bus = [48]
action1169.line_or_change_bus = [49]
actions.append(action1169)
# ---- END OF ACTION ---
action1170 = env.action_space()
action1170.gen_change_bus = [12]
action1170.gen_change_bus = [13]
action1170.line_or_change_bus = [32]
action1170.line_or_change_bus = [37]
action1170.line_or_change_bus = [38]
actions.append(action1170)
# ---- END OF ACTION ---
action1171 = env.action_space()
action1171.gen_change_bus = [5]
action1171.gen_change_bus = [6]
action1171.load_change_bus = [17]
actions.append(action1171)
# ---- END OF ACTION ---
action1172 = env.action_space()
action1172.gen_change_bus = [5]
action1172.gen_change_bus = [8]
action1172.line_ex_change_bus = [20]
action1172.line_or_change_bus = [54]
actions.append(action1172)
# ---- END OF ACTION ---
action1173 = env.action_space()
action1173.gen_change_bus = [6]
action1173.gen_change_bus = [7]
action1173.line_or_change_bus = [22]
action1173.line_or_change_bus = [23]
action1173.line_or_change_bus = [27]
action1173.line_or_change_bus = [28]
actions.append(action1173)
# ---- END OF ACTION ---
action1174 = env.action_space()
action1174.gen_change_bus = [2]
action1174.line_or_change_bus = [18]
action1174.line_or_change_bus = [19]
actions.append(action1174)
# ---- END OF ACTION ---
action1175 = env.action_space()
action1175.load_change_bus = [27]
action1175.line_ex_change_bus = [37]
action1175.line_ex_change_bus = [38]
action1175.line_or_change_bus = [40]
action1175.line_or_change_bus = [41]
actions.append(action1175)
# ---- END OF ACTION ---
action1176 = env.action_space()
action1176.gen_change_bus = [5]
action1176.gen_change_bus = [7]
action1176.gen_change_bus = [8]
action1176.load_change_bus = [17]
action1176.line_or_change_bus = [28]
action1176.line_or_change_bus = [48]
action1176.line_or_change_bus = [49]
actions.append(action1176)
# ---- END OF ACTION ---
action1177 = env.action_space()
action1177.load_change_bus = [27]
action1177.line_ex_change_bus = [37]
action1177.line_ex_change_bus = [38]
action1177.line_ex_change_bus = [39]
action1177.line_or_change_bus = [40]
action1177.line_ex_change_bus = [56]
actions.append(action1177)
# ---- END OF ACTION ---
action1178 = env.action_space()
action1178.gen_change_bus = [8]
action1178.line_ex_change_bus = [18]
action1178.line_ex_change_bus = [19]
action1178.line_or_change_bus = [22]
action1178.line_or_change_bus = [23]
action1178.line_or_change_bus = [28]
action1178.line_or_change_bus = [49]
actions.append(action1178)
# ---- END OF ACTION ---
action1179 = env.action_space()
action1179.gen_change_bus = [7]
action1179.line_or_change_bus = [22]
action1179.line_or_change_bus = [23]
action1179.line_or_change_bus = [54]
actions.append(action1179)
# ---- END OF ACTION ---
action1180 = env.action_space()
action1180.load_change_bus = [17]
action1180.line_ex_change_bus = [19]
action1180.line_ex_change_bus = [20]
action1180.line_ex_change_bus = [21]
action1180.line_or_change_bus = [22]
action1180.line_or_change_bus = [28]
action1180.line_or_change_bus = [54]
actions.append(action1180)
# ---- END OF ACTION ---
action1181 = env.action_space()
action1181.line_ex_change_bus = [19]
action1181.line_or_change_bus = [49]
actions.append(action1181)
# ---- END OF ACTION ---
action1182 = env.action_space()
action1182.gen_change_bus = [6]
action1182.gen_change_bus = [7]
action1182.load_change_bus = [17]
action1182.line_ex_change_bus = [18]
action1182.line_ex_change_bus = [19]
action1182.line_or_change_bus = [22]
action1182.line_or_change_bus = [23]
action1182.line_or_change_bus = [48]
action1182.line_or_change_bus = [49]
actions.append(action1182)
# ---- END OF ACTION ---
action1183 = env.action_space()
action1183.line_or_change_bus = [50]
actions.append(action1183)
# ---- END OF ACTION ---
action1184 = env.action_space()
action1184.gen_change_bus = [12]
action1184.gen_change_bus = [13]
action1184.load_change_bus = [24]
action1184.line_or_change_bus = [32]
action1184.line_or_change_bus = [34]
action1184.line_or_change_bus = [38]
actions.append(action1184)
# ---- END OF ACTION ---
action1185 = env.action_space()
action1185.line_ex_change_bus = [37]
action1185.line_ex_change_bus = [38]
action1185.line_or_change_bus = [40]
action1185.line_or_change_bus = [41]
action1185.line_ex_change_bus = [56]
actions.append(action1185)
# ---- END OF ACTION ---
action1186 = env.action_space()
action1186.gen_change_bus = [5]
action1186.gen_change_bus = [6]
action1186.gen_change_bus = [7]
action1186.gen_change_bus = [8]
action1186.line_ex_change_bus = [20]
action1186.line_ex_change_bus = [21]
action1186.line_or_change_bus = [22]
action1186.line_or_change_bus = [23]
action1186.line_or_change_bus = [27]
action1186.line_or_change_bus = [28]
action1186.line_or_change_bus = [48]
action1186.line_or_change_bus = [49]
action1186.line_or_change_bus = [54]
actions.append(action1186)
# ---- END OF ACTION ---
action1187 = env.action_space()
action1187.line_or_change_bus = [27]
action1187.line_or_change_bus = [28]
actions.append(action1187)
# ---- END OF ACTION ---
action1188 = env.action_space()
action1188.gen_change_bus = [11]
action1188.line_or_change_bus = [32]
action1188.line_or_change_bus = [37]
action1188.line_or_change_bus = [38]
actions.append(action1188)
# ---- END OF ACTION ---
action1189 = env.action_space()
action1189.gen_change_bus = [5]
action1189.gen_change_bus = [8]
action1189.load_change_bus = [17]
action1189.line_or_change_bus = [48]
action1189.line_or_change_bus = [49]
action1189.line_or_change_bus = [54]
actions.append(action1189)
# ---- END OF ACTION ---
action1190 = env.action_space()
action1190.line_ex_change_bus = [31]
action1190.line_or_change_bus = [38]
actions.append(action1190)
# ---- END OF ACTION ---
action1191 = env.action_space()
action1191.line_ex_change_bus = [19]
action1191.line_ex_change_bus = [20]
action1191.line_or_change_bus = [22]
action1191.line_or_change_bus = [23]
action1191.line_or_change_bus = [48]
action1191.line_or_change_bus = [49]
actions.append(action1191)
# ---- END OF ACTION ---
action1192 = env.action_space()
action1192.gen_change_bus = [6]
action1192.gen_change_bus = [7]
action1192.gen_change_bus = [8]
action1192.load_change_bus = [17]
action1192.line_ex_change_bus = [18]
action1192.line_ex_change_bus = [19]
action1192.line_or_change_bus = [22]
action1192.line_or_change_bus = [23]
action1192.line_or_change_bus = [28]
action1192.line_or_change_bus = [48]
action1192.line_or_change_bus = [49]
actions.append(action1192)
# ---- END OF ACTION ---
action1193 = env.action_space()
action1193.gen_change_bus = [12]
action1193.line_or_change_bus = [37]
actions.append(action1193)
# ---- END OF ACTION ---
action1194 = env.action_space()
action1194.line_ex_change_bus = [18]
action1194.line_or_change_bus = [54]
actions.append(action1194)
# ---- END OF ACTION ---
action1195 = env.action_space()
action1195.gen_change_bus = [5]
action1195.gen_change_bus = [6]
action1195.gen_change_bus = [7]
action1195.gen_change_bus = [8]
action1195.load_change_bus = [17]
action1195.line_or_change_bus = [22]
action1195.line_or_change_bus = [23]
action1195.line_or_change_bus = [48]
action1195.line_or_change_bus = [49]
action1195.line_or_change_bus = [54]
actions.append(action1195)
# ---- END OF ACTION ---
action1196 = env.action_space()
action1196.gen_change_bus = [17]
action1196.gen_change_bus = [18]
action1196.load_change_bus = [29]
action1196.line_ex_change_bus = [44]
actions.append(action1196)
# ---- END OF ACTION ---
action1197 = env.action_space()
action1197.gen_change_bus = [7]
action1197.load_change_bus = [17]
action1197.line_ex_change_bus = [20]
action1197.line_or_change_bus = [22]
action1197.line_or_change_bus = [23]
action1197.line_or_change_bus = [28]
action1197.line_or_change_bus = [48]
action1197.line_or_change_bus = [49]
actions.append(action1197)
# ---- END OF ACTION ---
action1198 = env.action_space()
action1198.gen_change_bus = [5]
action1198.gen_change_bus = [8]
action1198.line_ex_change_bus = [18]
action1198.line_or_change_bus = [23]
actions.append(action1198)
# ---- END OF ACTION ---
action1199 = env.action_space()
action1199.gen_change_bus = [6]
action1199.gen_change_bus = [7]
action1199.line_ex_change_bus = [20]
actions.append(action1199)
# ---- END OF ACTION ---
action1200 = env.action_space()
action1200.gen_change_bus = [11]
action1200.gen_change_bus = [12]
action1200.gen_change_bus = [13]
action1200.line_or_change_bus = [32]
action1200.line_or_change_bus = [38]
actions.append(action1200)
# ---- END OF ACTION ---
action1201 = env.action_space()
action1201.gen_change_bus = [14]
action1201.line_ex_change_bus = [38]
action1201.line_ex_change_bus = [39]
action1201.line_or_change_bus = [40]
action1201.line_or_change_bus = [41]
actions.append(action1201)
# ---- END OF ACTION ---
action1202 = env.action_space()
action1202.line_ex_change_bus = [39]
action1202.line_or_change_bus = [40]
action1202.line_or_change_bus = [41]
action1202.line_ex_change_bus = [56]
actions.append(action1202)
# ---- END OF ACTION ---
action1203 = env.action_space()
action1203.load_change_bus = [27]
action1203.line_ex_change_bus = [38]
action1203.line_ex_change_bus = [39]
action1203.line_ex_change_bus = [56]
actions.append(action1203)
# ---- END OF ACTION ---
action1204 = env.action_space()
action1204.gen_change_bus = [5]
action1204.gen_change_bus = [6]
action1204.gen_change_bus = [7]
action1204.gen_change_bus = [8]
action1204.load_change_bus = [17]
action1204.line_ex_change_bus = [20]
action1204.line_ex_change_bus = [21]
action1204.line_or_change_bus = [23]
action1204.line_or_change_bus = [48]
action1204.line_or_change_bus = [49]
action1204.line_or_change_bus = [54]
actions.append(action1204)
# ---- END OF ACTION ---
action1205 = env.action_space()
action1205.load_change_bus = [27]
action1205.line_ex_change_bus = [37]
action1205.line_ex_change_bus = [39]
action1205.line_or_change_bus = [40]
action1205.line_ex_change_bus = [56]
actions.append(action1205)
# ---- END OF ACTION ---
action1206 = env.action_space()
action1206.gen_change_bus = [5]
action1206.gen_change_bus = [8]
action1206.load_change_bus = [17]
action1206.line_ex_change_bus = [18]
action1206.line_ex_change_bus = [20]
action1206.line_or_change_bus = [27]
actions.append(action1206)
# ---- END OF ACTION ---
action1207 = env.action_space()
action1207.load_change_bus = [26]
action1207.line_ex_change_bus = [35]
actions.append(action1207)
# ---- END OF ACTION ---
action1208 = env.action_space()
action1208.gen_change_bus = [11]
action1208.gen_change_bus = [13]
action1208.line_ex_change_bus = [31]
action1208.line_or_change_bus = [32]
action1208.line_or_change_bus = [34]
action1208.line_or_change_bus = [37]
action1208.line_or_change_bus = [38]
actions.append(action1208)
# ---- END OF ACTION ---
action1209 = env.action_space()
action1209.gen_change_bus = [8]
action1209.load_change_bus = [17]
action1209.line_ex_change_bus = [18]
action1209.line_ex_change_bus = [19]
action1209.line_or_change_bus = [22]
action1209.line_or_change_bus = [23]
actions.append(action1209)
# ---- END OF ACTION ---
action1210 = env.action_space()
action1210.gen_change_bus = [8]
action1210.load_change_bus = [17]
action1210.line_or_change_bus = [22]
action1210.line_or_change_bus = [23]
action1210.line_or_change_bus = [54]
actions.append(action1210)
# ---- END OF ACTION ---
action1211 = env.action_space()
action1211.gen_change_bus = [7]
action1211.load_change_bus = [17]
action1211.line_ex_change_bus = [21]
action1211.line_or_change_bus = [22]
action1211.line_or_change_bus = [23]
action1211.line_or_change_bus = [27]
action1211.line_or_change_bus = [28]
action1211.line_or_change_bus = [54]
actions.append(action1211)
# ---- END OF ACTION ---
action1212 = env.action_space()
action1212.gen_change_bus = [8]
action1212.load_change_bus = [17]
action1212.line_ex_change_bus = [19]
action1212.line_ex_change_bus = [21]
action1212.line_or_change_bus = [22]
action1212.line_or_change_bus = [23]
action1212.line_or_change_bus = [49]
action1212.line_or_change_bus = [54]
actions.append(action1212)
# ---- END OF ACTION ---
action1213 = env.action_space()
action1213.gen_change_bus = [5]
action1213.gen_change_bus = [8]
action1213.line_ex_change_bus = [20]
action1213.line_or_change_bus = [27]
action1213.line_or_change_bus = [54]
actions.append(action1213)
# ---- END OF ACTION ---
action1214 = env.action_space()
action1214.load_change_bus = [22]
action1214.line_ex_change_bus = [28]
action1214.line_or_change_bus = [36]
actions.append(action1214)
# ---- END OF ACTION ---
action1215 = env.action_space()
action1215.gen_change_bus = [5]
action1215.gen_change_bus = [8]
action1215.load_change_bus = [17]
action1215.line_ex_change_bus = [19]
action1215.line_or_change_bus = [22]
action1215.line_or_change_bus = [23]
action1215.line_or_change_bus = [48]
action1215.line_or_change_bus = [49]
actions.append(action1215)
# ---- END OF ACTION ---
action1216 = env.action_space()
action1216.gen_change_bus = [13]
action1216.line_ex_change_bus = [31]
action1216.line_or_change_bus = [34]
action1216.line_or_change_bus = [37]
actions.append(action1216)
# ---- END OF ACTION ---
action1217 = env.action_space()
action1217.line_ex_change_bus = [19]
action1217.line_ex_change_bus = [21]
actions.append(action1217)
# ---- END OF ACTION ---
action1218 = env.action_space()
action1218.gen_change_bus = [7]
action1218.load_change_bus = [17]
action1218.line_ex_change_bus = [20]
action1218.line_ex_change_bus = [21]
action1218.line_or_change_bus = [22]
action1218.line_or_change_bus = [48]
action1218.line_or_change_bus = [49]
actions.append(action1218)
# ---- END OF ACTION ---
action1219 = env.action_space()
action1219.load_change_bus = [27]
action1219.line_or_change_bus = [40]
action1219.line_ex_change_bus = [56]
actions.append(action1219)
# ---- END OF ACTION ---
action1220 = env.action_space()
action1220.gen_change_bus = [5]
action1220.gen_change_bus = [8]
action1220.line_ex_change_bus = [18]
action1220.line_ex_change_bus = [19]
action1220.line_ex_change_bus = [20]
action1220.line_or_change_bus = [22]
action1220.line_or_change_bus = [23]
action1220.line_or_change_bus = [27]
action1220.line_or_change_bus = [49]
action1220.line_or_change_bus = [54]
actions.append(action1220)
# ---- END OF ACTION ---
action1221 = env.action_space()
action1221.load_change_bus = [24]
action1221.line_ex_change_bus = [31]
action1221.line_or_change_bus = [32]
action1221.line_or_change_bus = [34]
action1221.line_or_change_bus = [37]
action1221.line_or_change_bus = [38]
actions.append(action1221)
# ---- END OF ACTION ---
action1222 = env.action_space()
action1222.gen_change_bus = [5]
action1222.gen_change_bus = [8]
action1222.load_change_bus = [17]
action1222.line_or_change_bus = [22]
action1222.line_or_change_bus = [23]
action1222.line_or_change_bus = [48]
action1222.line_or_change_bus = [49]
action1222.line_or_change_bus = [54]
actions.append(action1222)
# ---- END OF ACTION ---
action1223 = env.action_space()
action1223.gen_change_bus = [5]
action1223.gen_change_bus = [8]
action1223.line_or_change_bus = [22]
action1223.line_or_change_bus = [54]
actions.append(action1223)
# ---- END OF ACTION ---
action1224 = env.action_space()
action1224.gen_change_bus = [11]
action1224.gen_change_bus = [12]
action1224.gen_change_bus = [13]
action1224.load_change_bus = [24]
action1224.line_ex_change_bus = [31]
action1224.line_or_change_bus = [32]
action1224.line_or_change_bus = [37]
action1224.line_or_change_bus = [38]
actions.append(action1224)
# ---- END OF ACTION ---
action1225 = env.action_space()
action1225.gen_change_bus = [21]
action1225.load_change_bus = [33]
action1225.load_change_bus = [36]
actions.append(action1225)
# ---- END OF ACTION ---
action1226 = env.action_space()
action1226.gen_change_bus = [5]
action1226.gen_change_bus = [6]
action1226.gen_change_bus = [8]
action1226.load_change_bus = [17]
action1226.line_ex_change_bus = [18]
action1226.line_ex_change_bus = [19]
action1226.line_or_change_bus = [22]
action1226.line_or_change_bus = [23]
action1226.line_or_change_bus = [27]
action1226.line_or_change_bus = [48]
action1226.line_or_change_bus = [49]
actions.append(action1226)
# ---- END OF ACTION ---
action1227 = env.action_space()
action1227.gen_change_bus = [8]
action1227.line_or_change_bus = [27]
actions.append(action1227)
# ---- END OF ACTION ---
action1228 = env.action_space()
action1228.gen_change_bus = [12]
action1228.gen_change_bus = [13]
action1228.line_ex_change_bus = [31]
action1228.line_or_change_bus = [34]
actions.append(action1228)
# ---- END OF ACTION ---
action1229 = env.action_space()
action1229.gen_change_bus = [6]
action1229.gen_change_bus = [7]
action1229.gen_change_bus = [8]
action1229.load_change_bus = [17]
action1229.line_ex_change_bus = [20]
actions.append(action1229)
# ---- END OF ACTION ---
action1230 = env.action_space()
action1230.load_change_bus = [22]
action1230.line_ex_change_bus = [28]
action1230.line_or_change_bus = [29]
action1230.line_or_change_bus = [36]
actions.append(action1230)
# ---- END OF ACTION ---
action1231 = env.action_space()
action1231.gen_change_bus = [5]
action1231.gen_change_bus = [8]
action1231.load_change_bus = [17]
action1231.line_ex_change_bus = [19]
action1231.line_ex_change_bus = [20]
action1231.line_ex_change_bus = [21]
action1231.line_or_change_bus = [22]
action1231.line_or_change_bus = [23]
action1231.line_or_change_bus = [27]
action1231.line_or_change_bus = [28]
action1231.line_or_change_bus = [48]
action1231.line_or_change_bus = [49]
actions.append(action1231)
# ---- END OF ACTION ---
action1232 = env.action_space()
action1232.gen_change_bus = [5]
action1232.load_change_bus = [17]
action1232.line_ex_change_bus = [20]
action1232.line_or_change_bus = [22]
action1232.line_or_change_bus = [23]
action1232.line_or_change_bus = [27]
action1232.line_or_change_bus = [28]
action1232.line_or_change_bus = [48]
action1232.line_or_change_bus = [49]
action1232.line_or_change_bus = [54]
actions.append(action1232)
# ---- END OF ACTION ---
action1233 = env.action_space()
action1233.load_change_bus = [27]
action1233.line_ex_change_bus = [38]
action1233.line_ex_change_bus = [56]
actions.append(action1233)
# ---- END OF ACTION ---
action1234 = env.action_space()
action1234.gen_change_bus = [5]
action1234.gen_change_bus = [8]
action1234.line_ex_change_bus = [18]
action1234.line_ex_change_bus = [19]
action1234.line_ex_change_bus = [20]
action1234.line_or_change_bus = [22]
action1234.line_or_change_bus = [23]
action1234.line_or_change_bus = [48]
action1234.line_or_change_bus = [49]
action1234.line_or_change_bus = [54]
actions.append(action1234)
# ---- END OF ACTION ---
action1235 = env.action_space()
action1235.line_or_change_bus = [22]
action1235.line_or_change_bus = [23]
action1235.line_or_change_bus = [28]
actions.append(action1235)
# ---- END OF ACTION ---
action1236 = env.action_space()
action1236.gen_change_bus = [5]
action1236.gen_change_bus = [7]
action1236.gen_change_bus = [8]
action1236.line_ex_change_bus = [20]
action1236.line_or_change_bus = [28]
actions.append(action1236)
# ---- END OF ACTION ---
action1237 = env.action_space()
action1237.gen_change_bus = [5]
action1237.line_or_change_bus = [28]
action1237.line_or_change_bus = [54]
actions.append(action1237)
# ---- END OF ACTION ---
action1238 = env.action_space()
action1238.load_change_bus = [27]
action1238.line_ex_change_bus = [39]
action1238.line_or_change_bus = [41]
action1238.line_ex_change_bus = [56]
actions.append(action1238)
# ---- END OF ACTION ---
action1239 = env.action_space()
action1239.gen_change_bus = [5]
action1239.gen_change_bus = [8]
action1239.load_change_bus = [17]
action1239.line_ex_change_bus = [18]
action1239.line_ex_change_bus = [19]
action1239.line_ex_change_bus = [20]
action1239.line_ex_change_bus = [21]
action1239.line_or_change_bus = [22]
action1239.line_or_change_bus = [49]
action1239.line_or_change_bus = [54]
actions.append(action1239)
# ---- END OF ACTION ---
action1240 = env.action_space()
action1240.load_change_bus = [17]
action1240.line_ex_change_bus = [19]
action1240.line_ex_change_bus = [20]
action1240.line_or_change_bus = [22]
action1240.line_or_change_bus = [49]
actions.append(action1240)
# ---- END OF ACTION ---
action1241 = env.action_space()
action1241.gen_change_bus = [5]
action1241.gen_change_bus = [7]
action1241.load_change_bus = [17]
action1241.line_ex_change_bus = [19]
action1241.line_or_change_bus = [22]
action1241.line_or_change_bus = [23]
action1241.line_or_change_bus = [49]
actions.append(action1241)
# ---- END OF ACTION ---
action1242 = env.action_space()
action1242.gen_change_bus = [5]
action1242.gen_change_bus = [6]
action1242.gen_change_bus = [7]
action1242.gen_change_bus = [8]
action1242.line_ex_change_bus = [18]
action1242.line_ex_change_bus = [19]
action1242.line_ex_change_bus = [20]
action1242.line_or_change_bus = [22]
action1242.line_or_change_bus = [23]
action1242.line_or_change_bus = [48]
action1242.line_or_change_bus = [49]
actions.append(action1242)
# ---- END OF ACTION ---
action1243 = env.action_space()
action1243.load_change_bus = [17]
action1243.line_ex_change_bus = [18]
action1243.line_ex_change_bus = [19]
action1243.line_ex_change_bus = [20]
action1243.line_ex_change_bus = [21]
action1243.line_or_change_bus = [22]
action1243.line_or_change_bus = [23]
action1243.line_or_change_bus = [28]
action1243.line_or_change_bus = [48]
action1243.line_or_change_bus = [49]
action1243.line_or_change_bus = [54]
actions.append(action1243)
# ---- END OF ACTION ---
action1244 = env.action_space()
action1244.gen_change_bus = [6]
action1244.gen_change_bus = [7]
action1244.gen_change_bus = [8]
action1244.line_ex_change_bus = [18]
action1244.line_ex_change_bus = [19]
action1244.line_ex_change_bus = [20]
action1244.line_or_change_bus = [54]
actions.append(action1244)
# ---- END OF ACTION ---
action1245 = env.action_space()
action1245.load_change_bus = [17]
action1245.line_ex_change_bus = [20]
action1245.line_ex_change_bus = [21]
actions.append(action1245)
# ---- END OF ACTION ---
action1246 = env.action_space()
action1246.gen_change_bus = [5]
action1246.gen_change_bus = [6]
action1246.gen_change_bus = [7]
action1246.gen_change_bus = [8]
action1246.load_change_bus = [17]
action1246.line_ex_change_bus = [18]
action1246.line_ex_change_bus = [19]
action1246.line_or_change_bus = [22]
action1246.line_or_change_bus = [23]
action1246.line_or_change_bus = [27]
action1246.line_or_change_bus = [48]
action1246.line_or_change_bus = [49]
action1246.line_or_change_bus = [54]
actions.append(action1246)
# ---- END OF ACTION ---
action1247 = env.action_space()
action1247.load_change_bus = [24]
action1247.line_or_change_bus = [34]
action1247.line_or_change_bus = [38]
actions.append(action1247)
# ---- END OF ACTION ---
action1248 = env.action_space()
action1248.line_ex_change_bus = [20]
action1248.line_or_change_bus = [28]
action1248.line_or_change_bus = [54]
actions.append(action1248)
# ---- END OF ACTION ---
action1249 = env.action_space()
action1249.gen_change_bus = [8]
action1249.line_ex_change_bus = [20]
action1249.line_ex_change_bus = [21]
action1249.line_or_change_bus = [27]
action1249.line_or_change_bus = [28]
action1249.line_or_change_bus = [54]
actions.append(action1249)
# ---- END OF ACTION ---
action1250 = env.action_space()
action1250.gen_change_bus = [9]
action1250.line_ex_change_bus = [27]
action1250.line_or_change_bus = [30]
action1250.line_or_change_bus = [36]
actions.append(action1250)
# ---- END OF ACTION ---
action1251 = env.action_space()
action1251.gen_change_bus = [5]
action1251.gen_change_bus = [6]
action1251.gen_change_bus = [7]
action1251.gen_change_bus = [8]
action1251.load_change_bus = [17]
action1251.line_ex_change_bus = [19]
action1251.line_or_change_bus = [49]
actions.append(action1251)
# ---- END OF ACTION ---
action1252 = env.action_space()
action1252.gen_change_bus = [5]
action1252.gen_change_bus = [6]
action1252.gen_change_bus = [8]
action1252.line_ex_change_bus = [19]
action1252.line_ex_change_bus = [20]
action1252.line_or_change_bus = [27]
action1252.line_or_change_bus = [28]
actions.append(action1252)
# ---- END OF ACTION ---
action1253 = env.action_space()
action1253.gen_change_bus = [9]
action1253.line_ex_change_bus = [27]
action1253.line_ex_change_bus = [28]
action1253.line_or_change_bus = [29]
action1253.line_or_change_bus = [30]
actions.append(action1253)
# ---- END OF ACTION ---
action1254 = env.action_space()
action1254.gen_change_bus = [5]
action1254.gen_change_bus = [7]
action1254.gen_change_bus = [8]
action1254.line_ex_change_bus = [18]
action1254.line_ex_change_bus = [19]
action1254.line_ex_change_bus = [20]
action1254.line_or_change_bus = [22]
action1254.line_or_change_bus = [23]
action1254.line_or_change_bus = [48]
action1254.line_or_change_bus = [49]
action1254.line_or_change_bus = [54]
actions.append(action1254)
# ---- END OF ACTION ---
action1255 = env.action_space()
action1255.gen_change_bus = [5]
action1255.line_ex_change_bus = [21]
actions.append(action1255)
# ---- END OF ACTION ---
action1256 = env.action_space()
action1256.gen_change_bus = [7]
action1256.gen_change_bus = [8]
action1256.line_ex_change_bus = [19]
action1256.line_or_change_bus = [22]
action1256.line_or_change_bus = [23]
action1256.line_or_change_bus = [48]
action1256.line_or_change_bus = [49]
actions.append(action1256)
# ---- END OF ACTION ---
action1257 = env.action_space()
action1257.gen_change_bus = [7]
action1257.line_ex_change_bus = [18]
action1257.line_ex_change_bus = [19]
action1257.line_or_change_bus = [22]
action1257.line_or_change_bus = [23]
action1257.line_or_change_bus = [28]
action1257.line_or_change_bus = [49]
action1257.line_or_change_bus = [54]
actions.append(action1257)
# ---- END OF ACTION ---
action1258 = env.action_space()
action1258.gen_change_bus = [5]
action1258.gen_change_bus = [7]
action1258.gen_change_bus = [8]
action1258.load_change_bus = [17]
action1258.line_ex_change_bus = [19]
action1258.line_or_change_bus = [22]
action1258.line_or_change_bus = [23]
action1258.line_or_change_bus = [28]
action1258.line_or_change_bus = [48]
action1258.line_or_change_bus = [49]
action1258.line_or_change_bus = [54]
actions.append(action1258)
# ---- END OF ACTION ---
action1259 = env.action_space()
action1259.gen_change_bus = [5]
action1259.load_change_bus = [17]
action1259.line_ex_change_bus = [20]
action1259.line_or_change_bus = [22]
action1259.line_or_change_bus = [23]
action1259.line_or_change_bus = [48]
action1259.line_or_change_bus = [49]
action1259.line_or_change_bus = [54]
actions.append(action1259)
# ---- END OF ACTION ---
action1260 = env.action_space()
action1260.line_ex_change_bus = [4]
action1260.line_or_change_bus = [6]
action1260.line_ex_change_bus = [55]
actions.append(action1260)
# ---- END OF ACTION ---
action1261 = env.action_space()
action1261.gen_change_bus = [5]
action1261.gen_change_bus = [6]
action1261.gen_change_bus = [7]
action1261.gen_change_bus = [8]
action1261.load_change_bus = [17]
action1261.line_ex_change_bus = [18]
action1261.line_ex_change_bus = [19]
action1261.line_or_change_bus = [22]
action1261.line_or_change_bus = [23]
action1261.line_or_change_bus = [48]
action1261.line_or_change_bus = [49]
action1261.line_or_change_bus = [54]
actions.append(action1261)
# ---- END OF ACTION ---
action1262 = env.action_space()
action1262.gen_change_bus = [5]
action1262.gen_change_bus = [7]
actions.append(action1262)
# ---- END OF ACTION ---
action1263 = env.action_space()
action1263.load_change_bus = [17]
action1263.line_or_change_bus = [23]
actions.append(action1263)
# ---- END OF ACTION ---
action1264 = env.action_space()
action1264.gen_change_bus = [5]
action1264.gen_change_bus = [6]
action1264.gen_change_bus = [7]
action1264.gen_change_bus = [8]
action1264.line_ex_change_bus = [18]
action1264.line_ex_change_bus = [19]
action1264.line_ex_change_bus = [20]
action1264.line_or_change_bus = [22]
action1264.line_or_change_bus = [23]
action1264.line_or_change_bus = [27]
action1264.line_or_change_bus = [28]
actions.append(action1264)
# ---- END OF ACTION ---
action1265 = env.action_space()
action1265.load_change_bus = [17]
action1265.line_or_change_bus = [22]
action1265.line_or_change_bus = [23]
action1265.line_or_change_bus = [27]
action1265.line_or_change_bus = [48]
action1265.line_or_change_bus = [49]
actions.append(action1265)
# ---- END OF ACTION ---
action1266 = env.action_space()
action1266.gen_change_bus = [5]
action1266.gen_change_bus = [6]
action1266.gen_change_bus = [7]
action1266.gen_change_bus = [8]
action1266.load_change_bus = [17]
action1266.line_ex_change_bus = [18]
action1266.line_ex_change_bus = [19]
action1266.line_ex_change_bus = [20]
action1266.line_or_change_bus = [22]
action1266.line_or_change_bus = [23]
action1266.line_or_change_bus = [48]
action1266.line_or_change_bus = [49]
actions.append(action1266)
# ---- END OF ACTION ---
action1267 = env.action_space()
action1267.gen_change_bus = [7]
action1267.load_change_bus = [17]
action1267.line_ex_change_bus = [18]
action1267.line_ex_change_bus = [19]
action1267.line_or_change_bus = [28]
actions.append(action1267)
# ---- END OF ACTION ---
action1268 = env.action_space()
action1268.gen_change_bus = [11]
action1268.gen_change_bus = [12]
action1268.gen_change_bus = [13]
action1268.line_or_change_bus = [34]
actions.append(action1268)
# ---- END OF ACTION ---
action1269 = env.action_space()
action1269.gen_change_bus = [12]
action1269.load_change_bus = [24]
action1269.line_or_change_bus = [32]
action1269.line_or_change_bus = [38]
actions.append(action1269)
# ---- END OF ACTION ---
action1270 = env.action_space()
action1270.gen_change_bus = [1]
action1270.line_ex_change_bus = [7]
actions.append(action1270)
# ---- END OF ACTION ---
action1271 = env.action_space()
action1271.gen_change_bus = [5]
action1271.gen_change_bus = [6]
action1271.load_change_bus = [17]
action1271.line_ex_change_bus = [20]
action1271.line_or_change_bus = [22]
action1271.line_or_change_bus = [27]
action1271.line_or_change_bus = [28]
action1271.line_or_change_bus = [54]
actions.append(action1271)
# ---- END OF ACTION ---
action1272 = env.action_space()
action1272.gen_change_bus = [9]
action1272.line_ex_change_bus = [27]
action1272.line_ex_change_bus = [28]
action1272.line_or_change_bus = [30]
actions.append(action1272)
# ---- END OF ACTION ---
action1273 = env.action_space()
action1273.line_ex_change_bus = [27]
action1273.line_ex_change_bus = [28]
action1273.line_or_change_bus = [29]
actions.append(action1273)
# ---- END OF ACTION ---
action1274 = env.action_space()
action1274.line_ex_change_bus = [49]
action1274.line_or_change_bus = [52]
action1274.line_ex_change_bus = [58]
actions.append(action1274)
# ---- END OF ACTION ---
action1275 = env.action_space()
action1275.gen_change_bus = [6]
action1275.gen_change_bus = [7]
action1275.load_change_bus = [17]
action1275.line_ex_change_bus = [18]
action1275.line_ex_change_bus = [19]
action1275.line_ex_change_bus = [20]
action1275.line_ex_change_bus = [21]
action1275.line_or_change_bus = [22]
action1275.line_or_change_bus = [23]
action1275.line_or_change_bus = [27]
action1275.line_or_change_bus = [28]
actions.append(action1275)
# ---- END OF ACTION ---
action1276 = env.action_space()
action1276.gen_change_bus = [8]
action1276.line_ex_change_bus = [20]
action1276.line_ex_change_bus = [21]
action1276.line_or_change_bus = [54]
actions.append(action1276)
# ---- END OF ACTION ---
action1277 = env.action_space()
action1277.gen_change_bus = [7]
action1277.gen_change_bus = [8]
action1277.line_ex_change_bus = [20]
actions.append(action1277)
# ---- END OF ACTION ---
action1278 = env.action_space()
action1278.load_change_bus = [27]
action1278.line_ex_change_bus = [38]
action1278.line_or_change_bus = [40]
action1278.line_or_change_bus = [41]
actions.append(action1278)
# ---- END OF ACTION ---
action1279 = env.action_space()
action1279.gen_change_bus = [7]
action1279.gen_change_bus = [8]
action1279.line_or_change_bus = [22]
action1279.line_or_change_bus = [23]
action1279.line_or_change_bus = [48]
action1279.line_or_change_bus = [49]
action1279.line_or_change_bus = [54]
actions.append(action1279)
# ---- END OF ACTION ---
action1280 = env.action_space()
action1280.gen_change_bus = [12]
action1280.load_change_bus = [24]
action1280.line_or_change_bus = [32]
actions.append(action1280)
# ---- END OF ACTION ---
action1281 = env.action_space()
action1281.load_change_bus = [17]
action1281.line_ex_change_bus = [20]
action1281.line_or_change_bus = [27]
action1281.line_or_change_bus = [54]
actions.append(action1281)
# ---- END OF ACTION ---
action1282 = env.action_space()
action1282.gen_change_bus = [5]
action1282.gen_change_bus = [8]
action1282.line_ex_change_bus = [18]
action1282.line_or_change_bus = [22]
action1282.line_or_change_bus = [23]
action1282.line_or_change_bus = [48]
action1282.line_or_change_bus = [49]
actions.append(action1282)
# ---- END OF ACTION ---
action1283 = env.action_space()
action1283.gen_change_bus = [5]
action1283.gen_change_bus = [8]
action1283.load_change_bus = [17]
action1283.line_ex_change_bus = [18]
action1283.line_ex_change_bus = [19]
action1283.line_ex_change_bus = [20]
action1283.line_or_change_bus = [22]
action1283.line_or_change_bus = [23]
action1283.line_or_change_bus = [28]
action1283.line_or_change_bus = [48]
action1283.line_or_change_bus = [49]
actions.append(action1283)
# ---- END OF ACTION ---
action1284 = env.action_space()
action1284.gen_change_bus = [11]
action1284.gen_change_bus = [12]
action1284.gen_change_bus = [13]
action1284.line_ex_change_bus = [31]
action1284.line_or_change_bus = [34]
actions.append(action1284)
# ---- END OF ACTION ---
action1285 = env.action_space()
action1285.gen_change_bus = [8]
action1285.line_ex_change_bus = [18]
actions.append(action1285)
# ---- END OF ACTION ---
action1286 = env.action_space()
action1286.gen_change_bus = [7]
action1286.load_change_bus = [17]
action1286.line_ex_change_bus = [18]
action1286.line_ex_change_bus = [19]
action1286.line_ex_change_bus = [21]
action1286.line_or_change_bus = [22]
action1286.line_or_change_bus = [23]
action1286.line_or_change_bus = [48]
action1286.line_or_change_bus = [49]
actions.append(action1286)
# ---- END OF ACTION ---
action1287 = env.action_space()
action1287.gen_change_bus = [4]
action1287.line_or_change_bus = [15]
action1287.line_or_change_bus = [16]
actions.append(action1287)
# ---- END OF ACTION ---
action1288 = env.action_space()
action1288.gen_change_bus = [5]
action1288.gen_change_bus = [8]
action1288.line_ex_change_bus = [18]
action1288.line_ex_change_bus = [19]
action1288.line_ex_change_bus = [21]
action1288.line_or_change_bus = [54]
actions.append(action1288)
# ---- END OF ACTION ---
action1289 = env.action_space()
action1289.gen_change_bus = [11]
action1289.gen_change_bus = [12]
action1289.line_or_change_bus = [32]
action1289.line_or_change_bus = [37]
actions.append(action1289)
# ---- END OF ACTION ---
action1290 = env.action_space()
action1290.load_change_bus = [17]
action1290.line_ex_change_bus = [20]
action1290.line_or_change_bus = [22]
action1290.line_or_change_bus = [23]
action1290.line_or_change_bus = [49]
actions.append(action1290)
# ---- END OF ACTION ---
action1291 = env.action_space()
action1291.gen_change_bus = [5]
action1291.gen_change_bus = [7]
action1291.gen_change_bus = [8]
action1291.line_ex_change_bus = [18]
action1291.line_ex_change_bus = [19]
action1291.line_or_change_bus = [22]
action1291.line_or_change_bus = [23]
action1291.line_or_change_bus = [27]
action1291.line_or_change_bus = [28]
action1291.line_or_change_bus = [49]
actions.append(action1291)
# ---- END OF ACTION ---
action1292 = env.action_space()
action1292.gen_change_bus = [11]
action1292.gen_change_bus = [12]
action1292.line_ex_change_bus = [31]
action1292.line_or_change_bus = [34]
action1292.line_or_change_bus = [37]
action1292.line_or_change_bus = [38]
actions.append(action1292)
# ---- END OF ACTION ---
action1293 = env.action_space()
action1293.gen_change_bus = [5]
action1293.gen_change_bus = [6]
action1293.gen_change_bus = [7]
action1293.gen_change_bus = [8]
action1293.line_ex_change_bus = [18]
action1293.line_ex_change_bus = [19]
action1293.line_or_change_bus = [23]
action1293.line_or_change_bus = [27]
action1293.line_or_change_bus = [28]
action1293.line_or_change_bus = [54]
actions.append(action1293)
# ---- END OF ACTION ---
action1294 = env.action_space()
action1294.gen_change_bus = [5]
action1294.line_ex_change_bus = [19]
actions.append(action1294)
# ---- END OF ACTION ---
action1295 = env.action_space()
action1295.gen_change_bus = [5]
action1295.gen_change_bus = [8]
action1295.line_ex_change_bus = [18]
action1295.line_ex_change_bus = [19]
action1295.line_ex_change_bus = [20]
action1295.line_ex_change_bus = [21]
action1295.line_or_change_bus = [22]
action1295.line_or_change_bus = [23]
action1295.line_or_change_bus = [27]
action1295.line_or_change_bus = [28]
action1295.line_or_change_bus = [54]
actions.append(action1295)
# ---- END OF ACTION ---
action1296 = env.action_space()
action1296.load_change_bus = [27]
action1296.line_ex_change_bus = [37]
action1296.line_ex_change_bus = [38]
action1296.line_ex_change_bus = [39]
action1296.line_or_change_bus = [41]
actions.append(action1296)
# ---- END OF ACTION ---
action1297 = env.action_space()
action1297.gen_change_bus = [13]
action1297.line_ex_change_bus = [31]
action1297.line_or_change_bus = [32]
action1297.line_or_change_bus = [34]
actions.append(action1297)
# ---- END OF ACTION ---
action1298 = env.action_space()
action1298.line_ex_change_bus = [18]
action1298.line_ex_change_bus = [19]
action1298.line_or_change_bus = [28]
actions.append(action1298)
# ---- END OF ACTION ---
action1299 = env.action_space()
action1299.gen_change_bus = [8]
action1299.line_ex_change_bus = [18]
action1299.line_ex_change_bus = [19]
action1299.line_or_change_bus = [27]
actions.append(action1299)
# ---- END OF ACTION ---
action1300 = env.action_space()
action1300.gen_change_bus = [14]
action1300.load_change_bus = [27]
action1300.line_ex_change_bus = [37]
action1300.line_ex_change_bus = [38]
action1300.line_ex_change_bus = [39]
action1300.line_or_change_bus = [40]
action1300.line_or_change_bus = [41]
action1300.line_ex_change_bus = [56]
actions.append(action1300)
# ---- END OF ACTION ---
action1301 = env.action_space()
action1301.gen_change_bus = [5]
action1301.gen_change_bus = [6]
action1301.gen_change_bus = [7]
action1301.gen_change_bus = [8]
action1301.load_change_bus = [17]
action1301.line_ex_change_bus = [18]
action1301.line_ex_change_bus = [19]
action1301.line_or_change_bus = [22]
action1301.line_or_change_bus = [23]
actions.append(action1301)
# ---- END OF ACTION ---
action1302 = env.action_space()
action1302.gen_change_bus = [6]
action1302.gen_change_bus = [7]
action1302.gen_change_bus = [8]
action1302.line_ex_change_bus = [19]
action1302.line_or_change_bus = [23]
action1302.line_or_change_bus = [49]
action1302.line_or_change_bus = [54]
actions.append(action1302)
# ---- END OF ACTION ---
action1303 = env.action_space()
action1303.gen_change_bus = [7]
action1303.line_ex_change_bus = [19]
action1303.line_ex_change_bus = [21]
action1303.line_or_change_bus = [27]
action1303.line_or_change_bus = [28]
action1303.line_or_change_bus = [48]
actions.append(action1303)
# ---- END OF ACTION ---
action1304 = env.action_space()
action1304.gen_change_bus = [5]
action1304.gen_change_bus = [6]
action1304.gen_change_bus = [7]
action1304.gen_change_bus = [8]
action1304.line_ex_change_bus = [19]
action1304.line_or_change_bus = [22]
action1304.line_or_change_bus = [28]
actions.append(action1304)
# ---- END OF ACTION ---
action1305 = env.action_space()
action1305.gen_change_bus = [9]
action1305.line_ex_change_bus = [27]
action1305.line_or_change_bus = [29]
actions.append(action1305)
# ---- END OF ACTION ---
action1306 = env.action_space()
action1306.load_change_bus = [17]
action1306.line_ex_change_bus = [20]
action1306.line_or_change_bus = [48]
action1306.line_or_change_bus = [49]
action1306.line_or_change_bus = [54]
actions.append(action1306)
# ---- END OF ACTION ---
action1307 = env.action_space()
action1307.gen_change_bus = [14]
action1307.load_change_bus = [27]
action1307.line_or_change_bus = [40]
actions.append(action1307)
# ---- END OF ACTION ---
action1308 = env.action_space()
action1308.gen_change_bus = [14]
action1308.line_or_change_bus = [41]
actions.append(action1308)
# ---- END OF ACTION ---
action1309 = env.action_space()
action1309.gen_change_bus = [7]
action1309.gen_change_bus = [8]
action1309.line_ex_change_bus = [18]
action1309.line_ex_change_bus = [19]
action1309.line_or_change_bus = [22]
action1309.line_or_change_bus = [23]
action1309.line_or_change_bus = [48]
action1309.line_or_change_bus = [49]
actions.append(action1309)
# ---- END OF ACTION ---
action1310 = env.action_space()
action1310.gen_change_bus = [7]
action1310.line_or_change_bus = [23]
action1310.line_or_change_bus = [54]
actions.append(action1310)
# ---- END OF ACTION ---
action1311 = env.action_space()
action1311.gen_change_bus = [5]
action1311.gen_change_bus = [7]
action1311.gen_change_bus = [8]
action1311.line_ex_change_bus = [21]
action1311.line_or_change_bus = [22]
action1311.line_or_change_bus = [54]
actions.append(action1311)
# ---- END OF ACTION ---
action1312 = env.action_space()
action1312.gen_change_bus = [5]
action1312.gen_change_bus = [8]
action1312.load_change_bus = [17]
action1312.line_ex_change_bus = [18]
action1312.line_ex_change_bus = [19]
action1312.line_or_change_bus = [22]
action1312.line_or_change_bus = [23]
action1312.line_or_change_bus = [48]
action1312.line_or_change_bus = [49]
actions.append(action1312)
# ---- END OF ACTION ---
action1313 = env.action_space()
action1313.load_change_bus = [31]
action1313.line_or_change_bus = [52]
actions.append(action1313)
# ---- END OF ACTION ---
action1314 = env.action_space()
action1314.gen_change_bus = [5]
action1314.gen_change_bus = [6]
action1314.gen_change_bus = [7]
action1314.gen_change_bus = [8]
actions.append(action1314)
# ---- END OF ACTION ---
action1315 = env.action_space()
action1315.gen_change_bus = [13]
action1315.line_ex_change_bus = [31]
action1315.line_or_change_bus = [32]
action1315.line_or_change_bus = [34]
action1315.line_or_change_bus = [37]
actions.append(action1315)
# ---- END OF ACTION ---
action1316 = env.action_space()
action1316.gen_change_bus = [5]
action1316.load_change_bus = [17]
action1316.line_ex_change_bus = [18]
action1316.line_ex_change_bus = [19]
action1316.line_or_change_bus = [22]
action1316.line_or_change_bus = [23]
action1316.line_or_change_bus = [27]
action1316.line_or_change_bus = [28]
action1316.line_or_change_bus = [48]
action1316.line_or_change_bus = [49]
actions.append(action1316)
# ---- END OF ACTION ---
action1317 = env.action_space()
action1317.load_change_bus = [17]
action1317.line_or_change_bus = [27]
actions.append(action1317)
# ---- END OF ACTION ---
action1318 = env.action_space()
action1318.load_change_bus = [17]
action1318.line_ex_change_bus = [19]
action1318.line_ex_change_bus = [20]
action1318.line_ex_change_bus = [21]
action1318.line_or_change_bus = [48]
action1318.line_or_change_bus = [49]
action1318.line_or_change_bus = [54]
actions.append(action1318)
# ---- END OF ACTION ---
action1319 = env.action_space()
action1319.gen_change_bus = [5]
action1319.gen_change_bus = [6]
action1319.gen_change_bus = [7]
action1319.gen_change_bus = [8]
action1319.load_change_bus = [17]
action1319.line_ex_change_bus = [19]
action1319.line_ex_change_bus = [20]
action1319.line_or_change_bus = [22]
action1319.line_or_change_bus = [27]
action1319.line_or_change_bus = [28]
action1319.line_or_change_bus = [49]
actions.append(action1319)
# ---- END OF ACTION ---
action1320 = env.action_space()
action1320.load_change_bus = [31]
action1320.line_ex_change_bus = [49]
action1320.line_ex_change_bus = [50]
action1320.line_or_change_bus = [52]
actions.append(action1320)
# ---- END OF ACTION ---
action1321 = env.action_space()
action1321.gen_change_bus = [11]
action1321.gen_change_bus = [13]
action1321.load_change_bus = [24]
action1321.line_or_change_bus = [32]
action1321.line_or_change_bus = [37]
action1321.line_or_change_bus = [38]
actions.append(action1321)
# ---- END OF ACTION ---
action1322 = env.action_space()
action1322.gen_change_bus = [5]
action1322.gen_change_bus = [8]
action1322.load_change_bus = [17]
action1322.line_ex_change_bus = [19]
action1322.line_ex_change_bus = [21]
action1322.line_or_change_bus = [22]
action1322.line_or_change_bus = [23]
action1322.line_or_change_bus = [49]
actions.append(action1322)
# ---- END OF ACTION ---
action1323 = env.action_space()
action1323.gen_change_bus = [5]
action1323.load_change_bus = [17]
action1323.line_ex_change_bus = [18]
action1323.line_ex_change_bus = [19]
action1323.line_or_change_bus = [22]
action1323.line_or_change_bus = [23]
action1323.line_or_change_bus = [27]
action1323.line_or_change_bus = [28]
action1323.line_or_change_bus = [49]
action1323.line_or_change_bus = [54]
actions.append(action1323)
# ---- END OF ACTION ---
action1324 = env.action_space()
action1324.gen_change_bus = [5]
action1324.gen_change_bus = [8]
action1324.line_ex_change_bus = [18]
actions.append(action1324)
# ---- END OF ACTION ---
action1325 = env.action_space()
action1325.gen_change_bus = [11]
action1325.load_change_bus = [24]
action1325.line_ex_change_bus = [31]
action1325.line_or_change_bus = [34]
actions.append(action1325)
# ---- END OF ACTION ---
action1326 = env.action_space()
action1326.gen_change_bus = [5]
action1326.load_change_bus = [17]
action1326.line_ex_change_bus = [18]
action1326.line_ex_change_bus = [19]
action1326.line_ex_change_bus = [20]
action1326.line_ex_change_bus = [21]
action1326.line_or_change_bus = [22]
action1326.line_or_change_bus = [23]
action1326.line_or_change_bus = [27]
action1326.line_or_change_bus = [28]
action1326.line_or_change_bus = [48]
action1326.line_or_change_bus = [49]
action1326.line_or_change_bus = [54]
actions.append(action1326)
# ---- END OF ACTION ---
action1327 = env.action_space()
action1327.load_change_bus = [17]
action1327.line_ex_change_bus = [20]
action1327.line_or_change_bus = [27]
action1327.line_or_change_bus = [28]
action1327.line_or_change_bus = [48]
action1327.line_or_change_bus = [49]
actions.append(action1327)
# ---- END OF ACTION ---
action1328 = env.action_space()
action1328.line_ex_change_bus = [20]
action1328.line_ex_change_bus = [21]
action1328.line_or_change_bus = [27]
action1328.line_or_change_bus = [28]
action1328.line_or_change_bus = [54]
actions.append(action1328)
# ---- END OF ACTION ---
action1329 = env.action_space()
action1329.gen_change_bus = [5]
action1329.gen_change_bus = [7]
action1329.gen_change_bus = [8]
action1329.load_change_bus = [17]
action1329.line_ex_change_bus = [18]
action1329.line_ex_change_bus = [19]
action1329.line_or_change_bus = [22]
action1329.line_or_change_bus = [23]
action1329.line_or_change_bus = [27]
action1329.line_or_change_bus = [48]
action1329.line_or_change_bus = [49]
actions.append(action1329)
# ---- END OF ACTION ---
action1330 = env.action_space()
action1330.gen_change_bus = [5]
action1330.gen_change_bus = [8]
action1330.load_change_bus = [17]
action1330.line_or_change_bus = [23]
action1330.line_or_change_bus = [28]
action1330.line_or_change_bus = [49]
actions.append(action1330)
# ---- END OF ACTION ---
action1331 = env.action_space()
action1331.gen_change_bus = [8]
action1331.load_change_bus = [17]
action1331.line_ex_change_bus = [18]
action1331.line_ex_change_bus = [19]
action1331.line_ex_change_bus = [20]
action1331.line_ex_change_bus = [21]
action1331.line_or_change_bus = [22]
action1331.line_or_change_bus = [23]
action1331.line_or_change_bus = [28]
action1331.line_or_change_bus = [48]
action1331.line_or_change_bus = [49]
action1331.line_or_change_bus = [54]
actions.append(action1331)
# ---- END OF ACTION ---
action1332 = env.action_space()
action1332.gen_change_bus = [8]
action1332.load_change_bus = [17]
action1332.line_or_change_bus = [28]
action1332.line_or_change_bus = [49]
action1332.line_or_change_bus = [54]
actions.append(action1332)
# ---- END OF ACTION ---
action1333 = env.action_space()
action1333.gen_change_bus = [7]
action1333.line_ex_change_bus = [21]
action1333.line_or_change_bus = [22]
action1333.line_or_change_bus = [23]
action1333.line_or_change_bus = [48]
action1333.line_or_change_bus = [49]
actions.append(action1333)
# ---- END OF ACTION ---
action1334 = env.action_space()
action1334.gen_change_bus = [14]
action1334.line_ex_change_bus = [38]
action1334.line_or_change_bus = [40]
actions.append(action1334)
# ---- END OF ACTION ---
action1335 = env.action_space()
action1335.line_ex_change_bus = [20]
action1335.line_ex_change_bus = [21]
action1335.line_or_change_bus = [27]
action1335.line_or_change_bus = [49]
action1335.line_or_change_bus = [54]
actions.append(action1335)
# ---- END OF ACTION ---
action1336 = env.action_space()
action1336.gen_change_bus = [5]
action1336.gen_change_bus = [7]
action1336.load_change_bus = [17]
action1336.line_or_change_bus = [54]
actions.append(action1336)
# ---- END OF ACTION ---
action1337 = env.action_space()
action1337.gen_change_bus = [5]
action1337.gen_change_bus = [6]
action1337.gen_change_bus = [7]
action1337.gen_change_bus = [8]
action1337.line_ex_change_bus = [18]
action1337.line_ex_change_bus = [19]
actions.append(action1337)
# ---- END OF ACTION ---
action1338 = env.action_space()
action1338.load_change_bus = [17]
action1338.line_ex_change_bus = [20]
action1338.line_or_change_bus = [27]
action1338.line_or_change_bus = [49]
actions.append(action1338)
# ---- END OF ACTION ---
action1339 = env.action_space()
action1339.load_change_bus = [17]
action1339.line_ex_change_bus = [18]
action1339.line_ex_change_bus = [19]
action1339.line_ex_change_bus = [20]
action1339.line_or_change_bus = [22]
action1339.line_or_change_bus = [28]
actions.append(action1339)
# ---- END OF ACTION ---
action1340 = env.action_space()
action1340.gen_change_bus = [5]
action1340.gen_change_bus = [8]
action1340.load_change_bus = [17]
action1340.line_ex_change_bus = [18]
action1340.line_ex_change_bus = [19]
action1340.line_or_change_bus = [22]
action1340.line_or_change_bus = [23]
action1340.line_or_change_bus = [28]
action1340.line_or_change_bus = [48]
action1340.line_or_change_bus = [49]
action1340.line_or_change_bus = [54]
actions.append(action1340)
# ---- END OF ACTION ---
action1341 = env.action_space()
action1341.gen_change_bus = [5]
action1341.load_change_bus = [17]
action1341.line_ex_change_bus = [19]
action1341.line_ex_change_bus = [20]
action1341.line_or_change_bus = [22]
action1341.line_or_change_bus = [54]
actions.append(action1341)
# ---- END OF ACTION ---
action1342 = env.action_space()
action1342.gen_change_bus = [6]
action1342.line_or_change_bus = [49]
action1342.line_or_change_bus = [54]
actions.append(action1342)
# ---- END OF ACTION ---
action1343 = env.action_space()
action1343.gen_change_bus = [8]
action1343.line_or_change_bus = [22]
action1343.line_or_change_bus = [23]
action1343.line_or_change_bus = [27]
action1343.line_or_change_bus = [48]
action1343.line_or_change_bus = [49]
action1343.line_or_change_bus = [54]
actions.append(action1343)
# ---- END OF ACTION ---
action1344 = env.action_space()
action1344.gen_change_bus = [14]
action1344.line_ex_change_bus = [37]
action1344.line_or_change_bus = [41]
actions.append(action1344)
# ---- END OF ACTION ---
action1345 = env.action_space()
action1345.gen_change_bus = [6]
action1345.gen_change_bus = [8]
action1345.load_change_bus = [17]
action1345.line_ex_change_bus = [18]
action1345.line_ex_change_bus = [19]
action1345.line_or_change_bus = [22]
action1345.line_or_change_bus = [23]
action1345.line_or_change_bus = [27]
action1345.line_or_change_bus = [28]
action1345.line_or_change_bus = [48]
action1345.line_or_change_bus = [49]
actions.append(action1345)
# ---- END OF ACTION ---
action1346 = env.action_space()
action1346.load_change_bus = [17]
action1346.line_ex_change_bus = [19]
action1346.line_ex_change_bus = [20]
action1346.line_or_change_bus = [22]
action1346.line_or_change_bus = [23]
action1346.line_or_change_bus = [28]
action1346.line_or_change_bus = [54]
actions.append(action1346)
# ---- END OF ACTION ---
action1347 = env.action_space()
action1347.gen_change_bus = [5]
action1347.gen_change_bus = [6]
action1347.gen_change_bus = [7]
action1347.gen_change_bus = [8]
action1347.line_ex_change_bus = [18]
action1347.line_ex_change_bus = [19]
action1347.line_or_change_bus = [28]
actions.append(action1347)
# ---- END OF ACTION ---
action1348 = env.action_space()
action1348.load_change_bus = [31]
action1348.line_ex_change_bus = [49]
action1348.line_ex_change_bus = [50]
action1348.line_or_change_bus = [52]
action1348.line_ex_change_bus = [58]
actions.append(action1348)
# ---- END OF ACTION ---
action1349 = env.action_space()
action1349.gen_change_bus = [5]
action1349.gen_change_bus = [8]
action1349.line_ex_change_bus = [19]
action1349.line_ex_change_bus = [20]
action1349.line_ex_change_bus = [21]
action1349.line_or_change_bus = [22]
action1349.line_or_change_bus = [27]
action1349.line_or_change_bus = [48]
action1349.line_or_change_bus = [49]
actions.append(action1349)
# ---- END OF ACTION ---
action1350 = env.action_space()
action1350.gen_change_bus = [7]
action1350.load_change_bus = [17]
action1350.line_ex_change_bus = [20]
action1350.line_ex_change_bus = [21]
action1350.line_or_change_bus = [22]
action1350.line_or_change_bus = [23]
action1350.line_or_change_bus = [27]
action1350.line_or_change_bus = [28]
action1350.line_or_change_bus = [48]
action1350.line_or_change_bus = [49]
action1350.line_or_change_bus = [54]
actions.append(action1350)
# ---- END OF ACTION ---
action1351 = env.action_space()
action1351.gen_change_bus = [5]
action1351.gen_change_bus = [6]
action1351.gen_change_bus = [7]
action1351.line_ex_change_bus = [18]
action1351.line_ex_change_bus = [19]
action1351.line_or_change_bus = [27]
action1351.line_or_change_bus = [28]
actions.append(action1351)
# ---- END OF ACTION ---
action1352 = env.action_space()
action1352.gen_change_bus = [13]
action1352.line_or_change_bus = [32]
action1352.line_or_change_bus = [38]
actions.append(action1352)
# ---- END OF ACTION ---
action1353 = env.action_space()
action1353.gen_change_bus = [5]
action1353.gen_change_bus = [8]
action1353.load_change_bus = [17]
action1353.line_ex_change_bus = [18]
action1353.line_ex_change_bus = [20]
action1353.line_or_change_bus = [22]
action1353.line_or_change_bus = [23]
action1353.line_or_change_bus = [27]
action1353.line_or_change_bus = [28]
action1353.line_or_change_bus = [48]
action1353.line_or_change_bus = [49]
actions.append(action1353)
# ---- END OF ACTION ---
action1354 = env.action_space()
action1354.gen_change_bus = [5]
action1354.gen_change_bus = [7]
action1354.gen_change_bus = [8]
action1354.line_or_change_bus = [22]
action1354.line_or_change_bus = [23]
action1354.line_or_change_bus = [27]
action1354.line_or_change_bus = [28]
action1354.line_or_change_bus = [48]
action1354.line_or_change_bus = [49]
action1354.line_or_change_bus = [54]
actions.append(action1354)
# ---- END OF ACTION ---
action1355 = env.action_space()
action1355.gen_change_bus = [11]
action1355.gen_change_bus = [12]
action1355.line_ex_change_bus = [31]
actions.append(action1355)
# ---- END OF ACTION ---
action1356 = env.action_space()
action1356.line_or_change_bus = [25]
actions.append(action1356)
# ---- END OF ACTION ---
action1357 = env.action_space()
action1357.gen_change_bus = [12]
action1357.gen_change_bus = [13]
action1357.load_change_bus = [24]
action1357.line_or_change_bus = [32]
action1357.line_or_change_bus = [37]
actions.append(action1357)
# ---- END OF ACTION ---
action1358 = env.action_space()
action1358.gen_change_bus = [11]
action1358.gen_change_bus = [12]
action1358.gen_change_bus = [13]
action1358.line_or_change_bus = [32]
action1358.line_or_change_bus = [34]
action1358.line_or_change_bus = [38]
actions.append(action1358)
# ---- END OF ACTION ---
action1359 = env.action_space()
action1359.gen_change_bus = [11]
action1359.load_change_bus = [24]
action1359.line_or_change_bus = [32]
action1359.line_or_change_bus = [37]
action1359.line_or_change_bus = [38]
actions.append(action1359)
# ---- END OF ACTION ---
action1360 = env.action_space()
action1360.gen_change_bus = [8]
action1360.load_change_bus = [17]
action1360.line_ex_change_bus = [20]
action1360.line_or_change_bus = [22]
action1360.line_or_change_bus = [27]
action1360.line_or_change_bus = [54]
actions.append(action1360)
# ---- END OF ACTION ---
action1361 = env.action_space()
action1361.gen_change_bus = [8]
action1361.load_change_bus = [17]
action1361.line_ex_change_bus = [20]
action1361.line_or_change_bus = [48]
action1361.line_or_change_bus = [49]
actions.append(action1361)
# ---- END OF ACTION ---
action1362 = env.action_space()
action1362.gen_change_bus = [7]
action1362.load_change_bus = [17]
action1362.line_ex_change_bus = [18]
action1362.line_ex_change_bus = [19]
action1362.line_or_change_bus = [22]
action1362.line_or_change_bus = [23]
action1362.line_or_change_bus = [28]
action1362.line_or_change_bus = [48]
action1362.line_or_change_bus = [49]
action1362.line_or_change_bus = [54]
actions.append(action1362)
# ---- END OF ACTION ---
action1363 = env.action_space()
action1363.line_or_change_bus = [10]
actions.append(action1363)
# ---- END OF ACTION ---
action1364 = env.action_space()
action1364.gen_change_bus = [12]
action1364.gen_change_bus = [13]
action1364.load_change_bus = [24]
action1364.line_or_change_bus = [37]
actions.append(action1364)
# ---- END OF ACTION ---
action1365 = env.action_space()
action1365.line_ex_change_bus = [4]
actions.append(action1365)
# ---- END OF ACTION ---
action1366 = env.action_space()
action1366.gen_change_bus = [8]
action1366.load_change_bus = [17]
action1366.line_ex_change_bus = [18]
action1366.line_ex_change_bus = [19]
action1366.line_or_change_bus = [22]
action1366.line_or_change_bus = [23]
action1366.line_or_change_bus = [28]
actions.append(action1366)
# ---- END OF ACTION ---
action1367 = env.action_space()
action1367.gen_change_bus = [8]
action1367.load_change_bus = [17]
action1367.line_or_change_bus = [22]
action1367.line_or_change_bus = [28]
action1367.line_or_change_bus = [48]
action1367.line_or_change_bus = [49]
actions.append(action1367)
# ---- END OF ACTION ---
action1368 = env.action_space()
action1368.gen_change_bus = [5]
action1368.gen_change_bus = [6]
action1368.gen_change_bus = [8]
action1368.line_ex_change_bus = [20]
actions.append(action1368)
# ---- END OF ACTION ---
action1369 = env.action_space()
action1369.load_change_bus = [27]
action1369.line_ex_change_bus = [37]
action1369.line_ex_change_bus = [56]
actions.append(action1369)
# ---- END OF ACTION ---
action1370 = env.action_space()
action1370.gen_change_bus = [5]
action1370.gen_change_bus = [6]
action1370.gen_change_bus = [7]
action1370.gen_change_bus = [8]
action1370.load_change_bus = [17]
action1370.line_ex_change_bus = [19]
action1370.line_ex_change_bus = [20]
action1370.line_ex_change_bus = [21]
action1370.line_or_change_bus = [22]
action1370.line_or_change_bus = [23]
action1370.line_or_change_bus = [27]
actions.append(action1370)
# ---- END OF ACTION ---
action1371 = env.action_space()
action1371.gen_change_bus = [5]
action1371.gen_change_bus = [8]
action1371.line_ex_change_bus = [18]
action1371.line_ex_change_bus = [19]
action1371.line_or_change_bus = [22]
action1371.line_or_change_bus = [23]
action1371.line_or_change_bus = [27]
action1371.line_or_change_bus = [28]
actions.append(action1371)
# ---- END OF ACTION ---
action1372 = env.action_space()
action1372.gen_change_bus = [11]
action1372.line_or_change_bus = [32]
action1372.line_or_change_bus = [34]
action1372.line_or_change_bus = [37]
actions.append(action1372)
# ---- END OF ACTION ---
action1373 = env.action_space()
action1373.gen_change_bus = [5]
action1373.line_or_change_bus = [22]
actions.append(action1373)
# ---- END OF ACTION ---
action1374 = env.action_space()
action1374.gen_change_bus = [5]
action1374.gen_change_bus = [6]
action1374.gen_change_bus = [7]
action1374.gen_change_bus = [8]
action1374.line_ex_change_bus = [18]
action1374.line_ex_change_bus = [19]
action1374.line_or_change_bus = [22]
action1374.line_or_change_bus = [23]
action1374.line_or_change_bus = [49]
actions.append(action1374)
# ---- END OF ACTION ---
action1375 = env.action_space()
action1375.gen_change_bus = [5]
action1375.gen_change_bus = [6]
action1375.gen_change_bus = [7]
action1375.gen_change_bus = [8]
action1375.load_change_bus = [17]
action1375.line_ex_change_bus = [20]
action1375.line_or_change_bus = [22]
action1375.line_or_change_bus = [27]
action1375.line_or_change_bus = [28]
actions.append(action1375)
# ---- END OF ACTION ---
action1376 = env.action_space()
action1376.load_change_bus = [22]
action1376.line_or_change_bus = [29]
actions.append(action1376)
# ---- END OF ACTION ---
action1377 = env.action_space()
action1377.gen_change_bus = [15]
actions.append(action1377)
# ---- END OF ACTION ---
action1378 = env.action_space()
action1378.gen_change_bus = [11]
action1378.gen_change_bus = [13]
action1378.load_change_bus = [24]
action1378.line_ex_change_bus = [31]
action1378.line_or_change_bus = [32]
action1378.line_or_change_bus = [37]
actions.append(action1378)
# ---- END OF ACTION ---
action1379 = env.action_space()
action1379.gen_change_bus = [5]
action1379.gen_change_bus = [6]
action1379.gen_change_bus = [7]
action1379.gen_change_bus = [8]
action1379.line_ex_change_bus = [18]
action1379.line_ex_change_bus = [19]
action1379.line_or_change_bus = [27]
action1379.line_or_change_bus = [28]
action1379.line_or_change_bus = [48]
action1379.line_or_change_bus = [49]
actions.append(action1379)
# ---- END OF ACTION ---
action1380 = env.action_space()
action1380.gen_change_bus = [5]
action1380.gen_change_bus = [7]
action1380.gen_change_bus = [8]
action1380.load_change_bus = [17]
action1380.line_ex_change_bus = [19]
action1380.line_ex_change_bus = [20]
action1380.line_or_change_bus = [22]
action1380.line_or_change_bus = [23]
action1380.line_or_change_bus = [28]
action1380.line_or_change_bus = [48]
action1380.line_or_change_bus = [49]
action1380.line_or_change_bus = [54]
actions.append(action1380)
# ---- END OF ACTION ---
action1381 = env.action_space()
action1381.gen_change_bus = [7]
action1381.gen_change_bus = [8]
actions.append(action1381)
# ---- END OF ACTION ---
action1382 = env.action_space()
action1382.gen_change_bus = [5]
action1382.gen_change_bus = [7]
action1382.gen_change_bus = [8]
action1382.load_change_bus = [17]
action1382.line_ex_change_bus = [18]
action1382.line_ex_change_bus = [19]
action1382.line_ex_change_bus = [20]
action1382.line_or_change_bus = [22]
action1382.line_or_change_bus = [23]
action1382.line_or_change_bus = [27]
action1382.line_or_change_bus = [28]
action1382.line_or_change_bus = [48]
action1382.line_or_change_bus = [49]
actions.append(action1382)
# ---- END OF ACTION ---
action1383 = env.action_space()
action1383.line_ex_change_bus = [37]
action1383.line_ex_change_bus = [39]
action1383.line_ex_change_bus = [56]
actions.append(action1383)
# ---- END OF ACTION ---
action1384 = env.action_space()
action1384.load_change_bus = [17]
action1384.line_ex_change_bus = [19]
action1384.line_ex_change_bus = [20]
action1384.line_ex_change_bus = [21]
action1384.line_or_change_bus = [27]
action1384.line_or_change_bus = [28]
actions.append(action1384)
# ---- END OF ACTION ---
action1385 = env.action_space()
action1385.gen_change_bus = [11]
action1385.gen_change_bus = [12]
action1385.gen_change_bus = [13]
action1385.line_or_change_bus = [32]
action1385.line_or_change_bus = [37]
action1385.line_or_change_bus = [38]
actions.append(action1385)
# ---- END OF ACTION ---
action1386 = env.action_space()
action1386.gen_change_bus = [2]
actions.append(action1386)
# ---- END OF ACTION ---
action1387 = env.action_space()
action1387.gen_change_bus = [5]
action1387.gen_change_bus = [6]
action1387.gen_change_bus = [8]
action1387.line_ex_change_bus = [19]
action1387.line_ex_change_bus = [20]
actions.append(action1387)
# ---- END OF ACTION ---
action1388 = env.action_space()
action1388.gen_change_bus = [5]
action1388.gen_change_bus = [6]
action1388.gen_change_bus = [7]
action1388.gen_change_bus = [8]
action1388.line_ex_change_bus = [19]
action1388.line_or_change_bus = [22]
action1388.line_or_change_bus = [23]
action1388.line_or_change_bus = [48]
action1388.line_or_change_bus = [49]
actions.append(action1388)
# ---- END OF ACTION ---
action1389 = env.action_space()
action1389.gen_change_bus = [5]
action1389.load_change_bus = [17]
action1389.line_ex_change_bus = [19]
action1389.line_or_change_bus = [48]
action1389.line_or_change_bus = [49]
actions.append(action1389)
# ---- END OF ACTION ---
action1390 = env.action_space()
action1390.gen_change_bus = [5]
action1390.gen_change_bus = [8]
action1390.load_change_bus = [17]
action1390.line_ex_change_bus = [18]
action1390.line_ex_change_bus = [19]
action1390.line_ex_change_bus = [20]
action1390.line_or_change_bus = [27]
action1390.line_or_change_bus = [48]
action1390.line_or_change_bus = [49]
actions.append(action1390)
# ---- END OF ACTION ---
action1391 = env.action_space()
action1391.line_ex_change_bus = [2]
action1391.line_ex_change_bus = [4]
action1391.line_or_change_bus = [5]
action1391.line_or_change_bus = [6]
action1391.line_ex_change_bus = [55]
actions.append(action1391)
# ---- END OF ACTION ---
action1392 = env.action_space()
action1392.gen_change_bus = [5]
action1392.gen_change_bus = [8]
action1392.load_change_bus = [17]
action1392.line_ex_change_bus = [19]
action1392.line_ex_change_bus = [20]
action1392.line_or_change_bus = [22]
action1392.line_or_change_bus = [23]
action1392.line_or_change_bus = [48]
action1392.line_or_change_bus = [49]
actions.append(action1392)
# ---- END OF ACTION ---
action1393 = env.action_space()
action1393.load_change_bus = [17]
action1393.line_or_change_bus = [28]
action1393.line_or_change_bus = [49]
actions.append(action1393)
# ---- END OF ACTION ---
action1394 = env.action_space()
action1394.gen_change_bus = [5]
action1394.gen_change_bus = [8]
action1394.line_or_change_bus = [22]
action1394.line_or_change_bus = [23]
action1394.line_or_change_bus = [27]
action1394.line_or_change_bus = [28]
action1394.line_or_change_bus = [48]
action1394.line_or_change_bus = [49]
action1394.line_or_change_bus = [54]
actions.append(action1394)
# ---- END OF ACTION ---
action1395 = env.action_space()
action1395.gen_change_bus = [5]
action1395.gen_change_bus = [6]
action1395.gen_change_bus = [7]
action1395.gen_change_bus = [8]
action1395.line_ex_change_bus = [19]
action1395.line_or_change_bus = [22]
action1395.line_or_change_bus = [23]
actions.append(action1395)
# ---- END OF ACTION ---
action1396 = env.action_space()
action1396.gen_change_bus = [14]
action1396.line_ex_change_bus = [37]
action1396.line_ex_change_bus = [38]
action1396.line_ex_change_bus = [39]
action1396.line_or_change_bus = [40]
action1396.line_or_change_bus = [41]
action1396.line_ex_change_bus = [56]
actions.append(action1396)
# ---- END OF ACTION ---
action1397 = env.action_space()
action1397.load_change_bus = [17]
action1397.line_or_change_bus = [48]
action1397.line_or_change_bus = [54]
actions.append(action1397)
# ---- END OF ACTION ---
action1398 = env.action_space()
action1398.gen_change_bus = [5]
action1398.gen_change_bus = [6]
action1398.gen_change_bus = [7]
action1398.gen_change_bus = [8]
action1398.line_ex_change_bus = [18]
action1398.line_ex_change_bus = [19]
action1398.line_or_change_bus = [22]
action1398.line_or_change_bus = [23]
action1398.line_or_change_bus = [27]
action1398.line_or_change_bus = [28]
action1398.line_or_change_bus = [49]
action1398.line_or_change_bus = [54]
actions.append(action1398)
# ---- END OF ACTION ---
action1399 = env.action_space()
action1399.line_ex_change_bus = [19]
action1399.line_or_change_bus = [48]
action1399.line_or_change_bus = [49]
action1399.line_or_change_bus = [54]
actions.append(action1399)
# ---- END OF ACTION ---
action1400 = env.action_space()
action1400.gen_change_bus = [2]
action1400.gen_change_bus = [3]
action1400.line_ex_change_bus = [10]
action1400.line_or_change_bus = [18]
action1400.line_or_change_bus = [19]
actions.append(action1400)
# ---- END OF ACTION ---
action1401 = env.action_space()
action1401.gen_change_bus = [7]
action1401.line_ex_change_bus = [20]
action1401.line_ex_change_bus = [21]
action1401.line_or_change_bus = [22]
action1401.line_or_change_bus = [23]
action1401.line_or_change_bus = [49]
action1401.line_or_change_bus = [54]
actions.append(action1401)
# ---- END OF ACTION ---
action1402 = env.action_space()
action1402.gen_change_bus = [11]
action1402.gen_change_bus = [12]
action1402.load_change_bus = [24]
action1402.line_ex_change_bus = [31]
action1402.line_or_change_bus = [32]
action1402.line_or_change_bus = [34]
action1402.line_or_change_bus = [37]
action1402.line_or_change_bus = [38]
actions.append(action1402)
# ---- END OF ACTION ---
action1403 = env.action_space()
action1403.gen_change_bus = [8]
action1403.load_change_bus = [17]
action1403.line_ex_change_bus = [19]
action1403.line_or_change_bus = [48]
action1403.line_or_change_bus = [49]
actions.append(action1403)
# ---- END OF ACTION ---
action1404 = env.action_space()
action1404.gen_change_bus = [12]
action1404.gen_change_bus = [13]
action1404.load_change_bus = [24]
action1404.line_ex_change_bus = [31]
action1404.line_or_change_bus = [32]
actions.append(action1404)
# ---- END OF ACTION ---
action1405 = env.action_space()
action1405.line_ex_change_bus = [18]
action1405.line_ex_change_bus = [19]
action1405.line_or_change_bus = [48]
action1405.line_or_change_bus = [49]
actions.append(action1405)
# ---- END OF ACTION ---
action1406 = env.action_space()
action1406.line_ex_change_bus = [37]
action1406.line_or_change_bus = [40]
action1406.line_or_change_bus = [41]
action1406.line_ex_change_bus = [56]
actions.append(action1406)
# ---- END OF ACTION ---
action1407 = env.action_space()
action1407.line_ex_change_bus = [19]
action1407.line_or_change_bus = [27]
action1407.line_or_change_bus = [49]
actions.append(action1407)
# ---- END OF ACTION ---
action1408 = env.action_space()
action1408.gen_change_bus = [5]
action1408.line_ex_change_bus = [18]
action1408.line_ex_change_bus = [19]
action1408.line_or_change_bus = [22]
action1408.line_or_change_bus = [23]
action1408.line_or_change_bus = [48]
action1408.line_or_change_bus = [49]
actions.append(action1408)
# ---- END OF ACTION ---
action1409 = env.action_space()
action1409.gen_change_bus = [5]
action1409.gen_change_bus = [6]
action1409.gen_change_bus = [7]
action1409.gen_change_bus = [8]
action1409.line_ex_change_bus = [18]
action1409.line_ex_change_bus = [19]
action1409.line_or_change_bus = [22]
action1409.line_or_change_bus = [23]
action1409.line_or_change_bus = [48]
action1409.line_or_change_bus = [49]
actions.append(action1409)
# ---- END OF ACTION ---
action1410 = env.action_space()
action1410.gen_change_bus = [8]
action1410.line_ex_change_bus = [18]
action1410.line_ex_change_bus = [19]
action1410.line_or_change_bus = [22]
action1410.line_or_change_bus = [23]
action1410.line_or_change_bus = [48]
action1410.line_or_change_bus = [49]
actions.append(action1410)
# ---- END OF ACTION ---
action1411 = env.action_space()
action1411.load_change_bus = [17]
action1411.line_ex_change_bus = [20]
action1411.line_ex_change_bus = [21]
action1411.line_or_change_bus = [22]
action1411.line_or_change_bus = [23]
action1411.line_or_change_bus = [48]
action1411.line_or_change_bus = [49]
actions.append(action1411)
# ---- END OF ACTION ---
action1412 = env.action_space()
action1412.load_change_bus = [24]
action1412.line_ex_change_bus = [31]
action1412.line_or_change_bus = [32]
action1412.line_or_change_bus = [37]
actions.append(action1412)
# ---- END OF ACTION ---
action1413 = env.action_space()
action1413.load_change_bus = [27]
action1413.line_or_change_bus = [40]
action1413.line_or_change_bus = [41]
actions.append(action1413)
# ---- END OF ACTION ---
action1414 = env.action_space()
action1414.line_ex_change_bus = [27]
action1414.line_or_change_bus = [29]
action1414.line_or_change_bus = [36]
actions.append(action1414)
# ---- END OF ACTION ---
action1415 = env.action_space()
action1415.gen_change_bus = [7]
action1415.load_change_bus = [17]
action1415.line_ex_change_bus = [20]
action1415.line_or_change_bus = [22]
action1415.line_or_change_bus = [48]
action1415.line_or_change_bus = [49]
actions.append(action1415)
# ---- END OF ACTION ---
action1416 = env.action_space()
action1416.gen_change_bus = [8]
action1416.load_change_bus = [17]
action1416.line_or_change_bus = [22]
action1416.line_or_change_bus = [23]
action1416.line_or_change_bus = [28]
action1416.line_or_change_bus = [48]
action1416.line_or_change_bus = [49]
action1416.line_or_change_bus = [54]
actions.append(action1416)
# ---- END OF ACTION ---
action1417 = env.action_space()
action1417.load_change_bus = [24]
action1417.line_ex_change_bus = [31]
action1417.line_or_change_bus = [38]
actions.append(action1417)
# ---- END OF ACTION ---
action1418 = env.action_space()
action1418.line_ex_change_bus = [18]
action1418.line_ex_change_bus = [19]
action1418.line_ex_change_bus = [20]
action1418.line_or_change_bus = [27]
action1418.line_or_change_bus = [28]
actions.append(action1418)
# ---- END OF ACTION ---
action1419 = env.action_space()
action1419.line_or_change_bus = [42]
action1419.line_or_change_bus = [43]
actions.append(action1419)
# ---- END OF ACTION ---
action1420 = env.action_space()
action1420.line_ex_change_bus = [38]
action1420.line_ex_change_bus = [39]
action1420.line_or_change_bus = [40]
action1420.line_or_change_bus = [41]
actions.append(action1420)
# ---- END OF ACTION ---
action1421 = env.action_space()
action1421.gen_change_bus = [7]
action1421.line_ex_change_bus = [18]
action1421.line_ex_change_bus = [19]
action1421.line_ex_change_bus = [20]
action1421.line_or_change_bus = [22]
action1421.line_or_change_bus = [23]
action1421.line_or_change_bus = [28]
action1421.line_or_change_bus = [48]
action1421.line_or_change_bus = [49]
actions.append(action1421)
# ---- END OF ACTION ---
action1422 = env.action_space()
action1422.load_change_bus = [27]
action1422.line_ex_change_bus = [37]
action1422.line_ex_change_bus = [39]
action1422.line_or_change_bus = [40]
action1422.line_or_change_bus = [41]
action1422.line_ex_change_bus = [56]
actions.append(action1422)
# ---- END OF ACTION ---
action1423 = env.action_space()
action1423.gen_change_bus = [6]
action1423.gen_change_bus = [7]
action1423.load_change_bus = [17]
action1423.line_ex_change_bus = [20]
action1423.line_or_change_bus = [49]
actions.append(action1423)
# ---- END OF ACTION ---
action1424 = env.action_space()
action1424.gen_change_bus = [11]
action1424.gen_change_bus = [12]
action1424.gen_change_bus = [13]
action1424.load_change_bus = [24]
action1424.line_ex_change_bus = [31]
action1424.line_or_change_bus = [32]
actions.append(action1424)
# ---- END OF ACTION ---
action1425 = env.action_space()
action1425.gen_change_bus = [7]
action1425.line_or_change_bus = [27]
actions.append(action1425)
# ---- END OF ACTION ---
action1426 = env.action_space()
action1426.load_change_bus = [24]
action1426.line_or_change_bus = [32]
actions.append(action1426)
# ---- END OF ACTION ---
action1427 = env.action_space()
action1427.load_change_bus = [17]
action1427.line_ex_change_bus = [20]
action1427.line_or_change_bus = [22]
action1427.line_or_change_bus = [23]
action1427.line_or_change_bus = [49]
action1427.line_or_change_bus = [54]
actions.append(action1427)
# ---- END OF ACTION ---
action1428 = env.action_space()
action1428.line_ex_change_bus = [19]
action1428.line_ex_change_bus = [21]
action1428.line_or_change_bus = [27]
action1428.line_or_change_bus = [54]
actions.append(action1428)
# ---- END OF ACTION ---
action1429 = env.action_space()
action1429.gen_change_bus = [12]
action1429.gen_change_bus = [13]
action1429.load_change_bus = [24]
action1429.line_ex_change_bus = [31]
action1429.line_or_change_bus = [32]
action1429.line_or_change_bus = [37]
action1429.line_or_change_bus = [38]
actions.append(action1429)
# ---- END OF ACTION ---
action1430 = env.action_space()
action1430.gen_change_bus = [6]
action1430.line_or_change_bus = [54]
actions.append(action1430)
# ---- END OF ACTION ---
action1431 = env.action_space()
action1431.gen_change_bus = [11]
action1431.gen_change_bus = [12]
action1431.gen_change_bus = [13]
action1431.load_change_bus = [24]
action1431.line_ex_change_bus = [31]
action1431.line_or_change_bus = [34]
action1431.line_or_change_bus = [37]
action1431.line_or_change_bus = [38]
actions.append(action1431)
# ---- END OF ACTION ---
action1432 = env.action_space()
action1432.gen_change_bus = [11]
action1432.load_change_bus = [24]
action1432.line_or_change_bus = [37]
action1432.line_or_change_bus = [38]
actions.append(action1432)
# ---- END OF ACTION ---
action1433 = env.action_space()
action1433.load_change_bus = [27]
action1433.line_ex_change_bus = [37]
action1433.line_ex_change_bus = [38]
action1433.line_or_change_bus = [40]
action1433.line_ex_change_bus = [56]
actions.append(action1433)
# ---- END OF ACTION ---
action1434 = env.action_space()
action1434.gen_change_bus = [13]
action1434.load_change_bus = [24]
action1434.line_ex_change_bus = [31]
action1434.line_or_change_bus = [32]
action1434.line_or_change_bus = [34]
actions.append(action1434)
# ---- END OF ACTION ---
action1435 = env.action_space()
action1435.load_change_bus = [17]
action1435.line_or_change_bus = [22]
action1435.line_or_change_bus = [23]
action1435.line_or_change_bus = [28]
action1435.line_or_change_bus = [48]
action1435.line_or_change_bus = [49]
action1435.line_or_change_bus = [54]
actions.append(action1435)
# ---- END OF ACTION ---
action1436 = env.action_space()
action1436.gen_change_bus = [6]
action1436.gen_change_bus = [7]
action1436.load_change_bus = [17]
action1436.line_ex_change_bus = [19]
action1436.line_ex_change_bus = [20]
action1436.line_or_change_bus = [22]
action1436.line_or_change_bus = [23]
action1436.line_or_change_bus = [28]
action1436.line_or_change_bus = [48]
action1436.line_or_change_bus = [49]
action1436.line_or_change_bus = [54]
actions.append(action1436)
# ---- END OF ACTION ---
action1437 = env.action_space()
action1437.gen_change_bus = [12]
action1437.line_ex_change_bus = [31]
action1437.line_or_change_bus = [32]
action1437.line_or_change_bus = [34]
action1437.line_or_change_bus = [38]
actions.append(action1437)
# ---- END OF ACTION ---
action1438 = env.action_space()
action1438.line_ex_change_bus = [21]
action1438.line_or_change_bus = [54]
actions.append(action1438)
# ---- END OF ACTION ---
action1439 = env.action_space()
action1439.gen_change_bus = [7]
action1439.load_change_bus = [17]
action1439.line_ex_change_bus = [19]
action1439.line_or_change_bus = [22]
action1439.line_or_change_bus = [23]
action1439.line_or_change_bus = [48]
action1439.line_or_change_bus = [49]
actions.append(action1439)
# ---- END OF ACTION ---
action1440 = env.action_space()
action1440.gen_change_bus = [5]
action1440.line_ex_change_bus = [18]
action1440.line_ex_change_bus = [19]
action1440.line_or_change_bus = [22]
action1440.line_or_change_bus = [23]
action1440.line_or_change_bus = [28]
action1440.line_or_change_bus = [49]
actions.append(action1440)
# ---- END OF ACTION ---
action1441 = env.action_space()
action1441.gen_change_bus = [5]
action1441.gen_change_bus = [6]
action1441.gen_change_bus = [7]
action1441.gen_change_bus = [8]
action1441.line_ex_change_bus = [18]
action1441.line_ex_change_bus = [19]
action1441.line_or_change_bus = [22]
action1441.line_or_change_bus = [27]
action1441.line_or_change_bus = [28]
action1441.line_or_change_bus = [54]
actions.append(action1441)
# ---- END OF ACTION ---
action1442 = env.action_space()
action1442.load_change_bus = [14]
action1442.line_or_change_bus = [15]
actions.append(action1442)
# ---- END OF ACTION ---
action1443 = env.action_space()
action1443.line_ex_change_bus = [31]
action1443.line_or_change_bus = [37]
actions.append(action1443)
# ---- END OF ACTION ---
action1444 = env.action_space()
action1444.gen_change_bus = [5]
action1444.gen_change_bus = [7]
action1444.line_ex_change_bus = [20]
action1444.line_or_change_bus = [54]
actions.append(action1444)
# ---- END OF ACTION ---
action1445 = env.action_space()
action1445.gen_change_bus = [14]
action1445.load_change_bus = [27]
action1445.line_ex_change_bus = [38]
action1445.line_or_change_bus = [41]
actions.append(action1445)
# ---- END OF ACTION ---
action1446 = env.action_space()
action1446.gen_change_bus = [8]
action1446.load_change_bus = [17]
action1446.line_or_change_bus = [54]
actions.append(action1446)
# ---- END OF ACTION ---
action1447 = env.action_space()
action1447.gen_change_bus = [12]
action1447.gen_change_bus = [13]
actions.append(action1447)
# ---- END OF ACTION ---
action1448 = env.action_space()
action1448.gen_change_bus = [14]
action1448.load_change_bus = [27]
action1448.line_ex_change_bus = [37]
actions.append(action1448)
# ---- END OF ACTION ---
action1449 = env.action_space()
action1449.gen_change_bus = [5]
action1449.gen_change_bus = [8]
action1449.load_change_bus = [17]
action1449.line_ex_change_bus = [18]
action1449.line_ex_change_bus = [19]
action1449.line_ex_change_bus = [20]
action1449.line_or_change_bus = [27]
action1449.line_or_change_bus = [28]
action1449.line_or_change_bus = [49]
action1449.line_or_change_bus = [54]
actions.append(action1449)
# ---- END OF ACTION ---
action1450 = env.action_space()
action1450.gen_change_bus = [5]
action1450.gen_change_bus = [8]
action1450.load_change_bus = [17]
action1450.line_ex_change_bus = [18]
action1450.line_ex_change_bus = [19]
action1450.line_ex_change_bus = [21]
action1450.line_or_change_bus = [22]
action1450.line_or_change_bus = [23]
action1450.line_or_change_bus = [27]
action1450.line_or_change_bus = [28]
action1450.line_or_change_bus = [48]
action1450.line_or_change_bus = [49]
action1450.line_or_change_bus = [54]
actions.append(action1450)
# ---- END OF ACTION ---
action1451 = env.action_space()
action1451.gen_change_bus = [11]
action1451.gen_change_bus = [13]
action1451.load_change_bus = [24]
action1451.line_or_change_bus = [32]
actions.append(action1451)
# ---- END OF ACTION ---
action1452 = env.action_space()
action1452.gen_change_bus = [7]
action1452.load_change_bus = [17]
action1452.line_ex_change_bus = [18]
action1452.line_ex_change_bus = [19]
action1452.line_or_change_bus = [22]
action1452.line_or_change_bus = [23]
action1452.line_or_change_bus = [27]
action1452.line_or_change_bus = [28]
action1452.line_or_change_bus = [48]
action1452.line_or_change_bus = [54]
actions.append(action1452)
# ---- END OF ACTION ---
action1453 = env.action_space()
action1453.gen_change_bus = [5]
action1453.line_ex_change_bus = [18]
action1453.line_ex_change_bus = [19]
action1453.line_or_change_bus = [48]
action1453.line_or_change_bus = [49]
actions.append(action1453)
# ---- END OF ACTION ---
action1454 = env.action_space()
action1454.load_change_bus = [27]
action1454.line_ex_change_bus = [37]
action1454.line_ex_change_bus = [38]
action1454.line_ex_change_bus = [39]
action1454.line_or_change_bus = [40]
action1454.line_or_change_bus = [41]
action1454.line_ex_change_bus = [56]
actions.append(action1454)
# ---- END OF ACTION ---
action1455 = env.action_space()
action1455.gen_change_bus = [15]
action1455.load_change_bus = [28]
action1455.line_or_change_bus = [42]
actions.append(action1455)
# ---- END OF ACTION ---
action1456 = env.action_space()
action1456.gen_change_bus = [20]
action1456.line_or_change_bus = [52]
action1456.line_ex_change_bus = [58]
actions.append(action1456)
# ---- END OF ACTION ---
action1457 = env.action_space()
action1457.gen_change_bus = [8]
action1457.line_or_change_bus = [49]
actions.append(action1457)
# ---- END OF ACTION ---
action1458 = env.action_space()
action1458.gen_change_bus = [5]
action1458.gen_change_bus = [8]
action1458.line_ex_change_bus = [18]
action1458.line_or_change_bus = [23]
action1458.line_or_change_bus = [27]
action1458.line_or_change_bus = [28]
actions.append(action1458)
# ---- END OF ACTION ---
action1459 = env.action_space()
action1459.gen_change_bus = [7]
action1459.gen_change_bus = [8]
action1459.load_change_bus = [17]
action1459.line_or_change_bus = [54]
actions.append(action1459)
# ---- END OF ACTION ---
action1460 = env.action_space()
action1460.gen_change_bus = [5]
action1460.gen_change_bus = [6]
action1460.gen_change_bus = [7]
action1460.gen_change_bus = [8]
action1460.load_change_bus = [17]
action1460.line_ex_change_bus = [20]
action1460.line_or_change_bus = [22]
action1460.line_or_change_bus = [27]
action1460.line_or_change_bus = [28]
action1460.line_or_change_bus = [54]
actions.append(action1460)
# ---- END OF ACTION ---
action1461 = env.action_space()
action1461.gen_change_bus = [5]
action1461.gen_change_bus = [8]
action1461.line_ex_change_bus = [20]
action1461.line_ex_change_bus = [21]
action1461.line_or_change_bus = [27]
action1461.line_or_change_bus = [28]
actions.append(action1461)
# ---- END OF ACTION ---
action1462 = env.action_space()
action1462.load_change_bus = [17]
action1462.line_ex_change_bus = [20]
action1462.line_or_change_bus = [48]
action1462.line_or_change_bus = [49]
actions.append(action1462)
# ---- END OF ACTION ---

actions62 = []

for i in range(0,62):
  vect = actions[i].to_vect()
  actions62.append(vect)
actions62 = np.asarray(actions62)

actions146 = []
for i in range(62,62+146):
  vect = actions[i].to_vect()
  actions146.append(vect)
actions146 = np.asarray(actions146)

actions1255 = []
for i in range(62+146,len(actions)):
  vect = actions[i].to_vect()
  actions1255.append(vect)
actions1255 = np.asarray(actions1255)

print(actions62.shape)
print(actions146.shape)
print(actions1255.shape)

np.save('actions62',actions62)
np.save('actions146',actions146)
np.save('actions1255',actions1255)

print("OK")
