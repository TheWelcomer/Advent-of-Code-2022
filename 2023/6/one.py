# y < (c - x)x = cx - x^2
# 0 < -x^2 + cx - y
# x < (-c +- sqrt(c^2 - 4y)) / -2
import math

with open("data.txt", 'r') as f:
    lines = f.readlines()
    parsedlines = []
    races = []
    result = 1
    for i in range(2):
        parsedlines.append(list(filter(lambda x: False if x == ' ' or x == '' else True, lines[i].strip('Time:      \nDistance:   ').split(' '))))
    for i in range(len(parsedlines[0])):
        races.append((int(parsedlines[0][i]), int(parsedlines[1][i])))
    for race in races:
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