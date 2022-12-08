with open("data.txt") as data:
    array = []
    visibleTrees = []
    for line in data.readlines():
        line = line.replace("\n", "")
        numList = [*line]
        array.append(numList)
    for col in range(len(array[0])):
        highestTree = -1
        for row in range(len(array)):
            currentTree = int(array[row][col])
            if currentTree > highestTree:
                highestTree = currentTree
                treeCoords = (row, col)
                print(treeCoords)
                if treeCoords not in visibleTrees:
                    visibleTrees.append(treeCoords)
    for col in range(len(array[0])):
        highestTree = -1
        for row in range(len(array)):
            currentTree = int(array[len(array) - 1 - row][col])
            if currentTree > highestTree:
                highestTree = currentTree
                treeCoords = (len(array) - 1 - row, col)
                print(treeCoords)
                if treeCoords not in visibleTrees:
                    visibleTrees.append(treeCoords)
    for row in range(len(array)):
        highestTree = -1
        for col in range(len(array[0])):
            currentTree = int(array[row][col])
            if currentTree > highestTree:
                highestTree = currentTree
                treeCoords = (row, col)
                print(treeCoords)
                if treeCoords not in visibleTrees:
                    visibleTrees.append(treeCoords)
    for row in range(len(array)):
        highestTree = -1
        for col in range(len(array[0])):
            currentTree = int(array[row][(len(array[col])) - 1 - col])
            if currentTree > highestTree:
                highestTree = currentTree
                treeCoords = (row, (len(array[col])) - 1 - col)
                print(treeCoords)
                if treeCoords not in visibleTrees:
                    visibleTrees.append(treeCoords)
    print(len(visibleTrees))