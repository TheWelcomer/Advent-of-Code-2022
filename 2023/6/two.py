# y < (c - x)x = cx - x^2
# 0 < -x^2 + cx - y
# x < (-c +- sqrt(c^2 - 4y)) / -2
import math
import functools
with open("data.txt", 'r') as f:
    lines = f.readlines()
    result = 1
    race = []
    for i in range(2):
        race.append(int(functools.reduce(lambda a, b: a + b, list(filter(lambda x: False if x == ' ' or x == '' else True, lines[i].strip('Time:      \nDistance:   ').split(' '))))))
    c, y = race
    upper, lower = (-c - math.sqrt(pow(c, 2) - 4 * y)) / -2, (-c + math.sqrt(pow(c, 2) - 4 * y)) / -2
    if upper % 1 == 0:
        upper = upper - 1
    else: 
        upper = math.floor(upper)
    if lower % 1 == 0:
        lower = lower + 1
    else: 
        lower = math.ceil(lower)
    if upper - lower + 1 >= 0:
        result *= upper - lower + 1
    print(int(result))