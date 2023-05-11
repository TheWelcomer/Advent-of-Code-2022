with open("data.txt", "r") as f:
    data = f.readlines()
    grid = [[0 for i in range(1000)] for i in range(1000)]
    for line in data:
        startLine = line[0:8]
        line = line.strip()
        activation = line.split(" ")
        line = line.replace(" through ", ",")
        line = line.replace("turn off ", "")
        line = line.replace("turn on ", "")
        line = line.replace("toggle ", "")
        fromToNums = line.split(",")
        fromX = int(min(int(fromToNums[0]), int(fromToNums[2])))
        fromY = int(min(int(fromToNums[1]), int(fromToNums[3])))
        toX = int(max(int(fromToNums[0]), int(fromToNums[2])))
        toY = int(max(int(fromToNums[1]), int(fromToNums[3])))
        if (activation[0] == "toggle"):
            for yPos in range(fromY, toY + 1):
                for xPos in range(fromX, toX + 1):
                    grid[yPos][xPos] = 1 if grid[yPos][xPos] == 0 else 0
        elif (activation[1] == "off"):
            for yPos in range(fromY, toY + 1):
                for xPos in range(fromX, toX + 1):
                    grid[yPos][xPos] = 0
        elif (activation[1] == "on"):
            for yPos in range(fromY, toY + 1):
                for xPos in range(fromX, toX + 1):
                    grid[yPos][xPos] = 1
    
    count = 0
    for y in grid:
        for light in y:
            count += light
    print(count)