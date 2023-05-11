letterHeightMap = {
    "S": 0,
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    "E": 25
}
with open("data.txt", "r") as f:
    data = f.readlines()
    lowestPoints = []
    endPos = [0, 0]
    hillMap = []
    for y in range(len(data)):
        data[y] = data[y].strip()
        hillRow = []
        for x in range(len(data[y])):
            hillRow.append(data[y][x])
            if data[y][x] in "Sa":
                lowestPoints.append([x, y])
            elif data[y][x] == "E":
                endPos = [x, y]
        hillMap.append(hillRow)
    trueShortestPath = 100000000
    for startPos in lowestPoints:
        pathX = 0
        pathY = 0
        newPathX = 0
        newPathY = 0
        previouslySearched = set()
        frontier = set(((tuple(startPos),),))
        shortestPath = None
        newFrontier = set()
        while True:
            if frontier == set():
                shortestPath = 1000000000
                break
            for path in frontier:
                pathX = path[-1][0]
                pathY = path[-1][1]
                if hillMap[pathY][pathX] == "E":
                    shortestPath = len(path) - 1
                    break
                if pathX != 0:
                    newPath = list(path)
                    newPathX = pathX - 1
                    newPathY = pathY
                    if letterHeightMap[hillMap[newPathY][newPathX]] - letterHeightMap[hillMap[pathY][pathX]] <= 1:
                        newPath.append((newPathX, newPathY))
                        newPath = tuple(newPath)
                        if not newPath[-1] in previouslySearched and not newPath in frontier:
                            newFrontier.add(newPath)
                            previouslySearched.add(newPath[-1])
                if pathX != len(hillMap[0]) - 1:
                    newPath = list(path)
                    newPathX = pathX + 1
                    newPathY = pathY
                    if letterHeightMap[hillMap[newPathY][newPathX]] - letterHeightMap[hillMap[pathY][pathX]] <= 1:
                        newPath.append((newPathX, newPathY))
                        newPath = tuple(newPath)
                        if not newPath[-1] in previouslySearched:
                            newFrontier.add(newPath)
                            previouslySearched.add(newPath[-1])
                if pathY != 0:
                    newPath = list(path)
                    newPathX = pathX
                    newPathY = pathY - 1
                    if letterHeightMap[hillMap[newPathY][newPathX]] - letterHeightMap[hillMap[pathY][pathX]] <= 1:
                        newPath.append((newPathX, newPathY))
                        newPath = tuple(newPath)
                        if not newPath[-1] in previouslySearched:
                            newFrontier.add(newPath)
                            previouslySearched.add(newPath[-1])
                if pathY != len(hillMap) - 1:
                    newPath = list(path)
                    newPathX = pathX
                    newPathY = pathY + 1
                    if letterHeightMap[hillMap[newPathY][newPathX]] - letterHeightMap[hillMap[pathY][pathX]] <= 1:
                        newPath.append((newPathX, newPathY))
                        newPath = tuple(newPath)
                        if not newPath[-1] in previouslySearched:
                            newFrontier.add(newPath)
                            previouslySearched.add(newPath[-1])
            if shortestPath != None:
                break
            frontier = newFrontier.copy()
            newFrontier = set()
        trueShortestPath = min(trueShortestPath, shortestPath)
    print(trueShortestPath)