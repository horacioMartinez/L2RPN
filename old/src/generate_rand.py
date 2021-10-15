import random
import numpy as np

np.set_printoptions(suppress=True)

lowest = 0.1
highest = 0.9
highest_first = 0.15

numbers = []
NUM_RANDOM_NUMBERS = 7
spins = 100

for a in range(0, spins):
    numbers = []
    for i in range(0, NUM_RANDOM_NUMBERS):
        if i == 0:
            r = random.uniform(lowest, highest_first)
        else:
            r = random.uniform(lowest, highest)
        if len(numbers) == 0:
            numbers.append(r)
        else:
            while r < numbers[i - 1]:
                r = random.uniform(lowest, highest)
            numbers.append(r)
    formatted_numbers = [("%.2f" % elem).strip("'") for elem in numbers]
    formatted_numbers = formatted_numbers[::-1]
    str = '"['
    for number in formatted_numbers:
        str += number
        str += ","
    str = str[:-1]
    str += ']"'
    print(str)
