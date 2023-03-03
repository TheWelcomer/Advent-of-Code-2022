with open("noops.txt", "r") as f:
    data = f.readlines()
    timesVals = [20, 60, 100, 140, 180, 220]
    intermediateVals = []
    x = 1
    clockCycle = 0
    for line in data:
        line = line.strip()
        if line == "noop":
            clockCycle += 1
            if (clockCycle - 20) % 40 == 0:
                intermediateVals.append(x)
        else:
            clockCycle += 1
            if (clockCycle - 20) % 40 == 0:
                intermediateVals.append(x)
            clockCycle += 1
            if (clockCycle - 20) % 40 == 0:
                intermediateVals.append(x)
            casted = line[5:]
            x += int(line[5:])
    result = 0
    for i in range(len(intermediateVals)):
        result += intermediateVals[i] * timesVals[i]
    print(result)