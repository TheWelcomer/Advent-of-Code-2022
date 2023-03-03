import math
with open("noops.txt") as data:
    signalStrengths = []
    multFactors = [20, 60, 100, 140, 180, 220]
    cycle = 20
    regVal = 1
    for line in data.readlines():
        line = line.strip("\n")
        if cycle % 40 == 0:
            signalStrengths.append(regVal)
        if line == "noop":
            cycle += 1
            continue
        changeNum = int(line[5:])
        cycle += 1
        if cycle % 40 == 0:
            signalStrengths.append(regVal)
        cycle += 1
        if cycle % 40 == 0:
            signalStrengths.append(regVal)
        regVal += changeNum
    result = 0
    results = []
    for i in range(6):
        results.append(signalStrengths[i] * multFactors[i])
    for i in range(6):
        result += signalStrengths[i] * multFactors[i]
print(signalStrengths)
print(results)
print(result)