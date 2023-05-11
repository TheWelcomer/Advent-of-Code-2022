with open("data.txt", "r") as f:
    waterfall = [["." for i in range(1024)] for i in range(1024)]
    data = f.readlines()
    highestY = 0
    for line in data:
        line = line.strip("\n")
        previousTracer = []
        tracer = []
        line = line.replace(" -> ", "*")
        line = line.split("*")
        for coord in line:
            coords = coord.split(",")
            tracer = [int(coords[1]), int(coords[0])]
            highestY = max(highestY, tracer[0])
            if previousTracer == []:
                previousTracer = tracer
                continue
            if tracer[0] == previousTracer[0]:
                for i in range(min(previousTracer[1], tracer[1]), max(previousTracer[1], tracer[1]) + 1):
                    waterfall[tracer[0]][i] = "#"
            else:
                for i in range(min(previousTracer[0], tracer[0]), max(previousTracer[0], tracer[0]) + 1):
                    waterfall[i][tracer[1]] = "#"
            previousTracer = tracer
    for i in range(0, 1024):
        waterfall[highestY + 2][i] = "#"
    sandGrains = 0
    outerBreak = False
    while True:
        sand = [500, 0]
        while True:
            if waterfall[sand[1] + 1][sand[0]] == ".":
                sand[1] = sand[1] + 1
            elif waterfall[sand[1] + 1][sand[0] - 1] == ".":
                sand[0] = sand[0] - 1
                sand[1] = sand[1] + 1
            elif waterfall[sand[1] + 1][sand[0] + 1] == ".":
                sand[0] = sand[0] + 1
                sand[1] = sand[1] + 1
            else:
                waterfall[sand[1]][sand[0]] = "#"
                if sand == [500, 0]:
                    outerBreak = True
                break
        sandGrains += 1
        if outerBreak: break
    print(sandGrains)
    
    #View Map
    """    
    for i in range(0, 10):
        for j in range(494, 504):
            mapView += waterfall[i][j]
        mapView += "\n"
    print(mapView)
    """