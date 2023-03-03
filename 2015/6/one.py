with open("data.txt", "r") as f:
    data = f.readlines()
    for line in data:
        grid = [[0 for i in range(1000)] for i in range(1000)]
        startLine = line[0:8]
        line = line.strip()
        line = line.replace(" through ", ",")
        line = line.replace("turn off ", "")
        line = line.replace("turn on ", "")
        line = line.replace("toggle ", "")
        fromToNums = line.split(",")
        fromX = int(fromToNums[0])
        fromY = int(fromToNums[1])
        toX = int(fromToNums[2])
        toY = int(fromToNums[3])
        if "turn off" in startLine:
            for y in range(fromY, toY + 1):
                for x in range(fromX, toX + 1):
                    grid[y][x] = 0
        elif "turn on" in startLine:
            for y in range(fromY, toY + 1):
                for x in range(fromX, toX + 1):
                    grid[y][x] = 1
        elif "toggle" in startLine:
            for y in range(fromY, toY + 1):
                for x in range(fromX, toX + 1):
                    if grid[y][x] == 0:
                        grid[y][x] = 1
                    else:
                        grid[y][x] = 0
        numLit = 0
        for row in grid:
            for light in row:
                numLit += light
    print(numLit)