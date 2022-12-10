with open("data.txt") as data:
    #creates a 2d array of the data and initializes an answer set
    array = []
    visibleTrees = set()
    for line in data.readlines():
        line = line.replace("\n", "")
        numList = [*line]
        array.append(numList)
    
    #finds trees visible from the top
    for col in range(len(array[0])):
        highestTree = -1
        for row in range(len(array)):
            currentTree = int(array[row][col])
            if currentTree > highestTree:
                highestTree = currentTree
                treeCoords = (row, col)
                visibleTrees.add(treeCoords)
                    
        #finds trees visible from the bottom
    for col in range(len(array[0])):
        highestTree = -1
        for row in range(len(array)):
            currentTree = int(array[len(array) - 1 - row][col])
            if currentTree > highestTree:
                highestTree = currentTree
                treeCoords = (len(array) - 1 - row, col)
                visibleTrees.add(treeCoords)
    
    #finds trees visible from the left
    for row in range(len(array)):
        highestTree = -1
        for col in range(len(array[0])):
            currentTree = int(array[row][col])
            if currentTree > highestTree:
                highestTree = currentTree
                treeCoords = (row, col)
                visibleTrees.add(treeCoords)
    
    #finds trees visible from the right
    for row in range(len(array)):
        highestTree = -1
        for col in range(len(array[0])):
            currentTree = int(array[row][len(array) - 1 - col])
            if currentTree > highestTree:
                highestTree = currentTree
                treeCoords = (row, len(array) - 1 - col)
                visibleTrees.add(treeCoords)
    
    #prints the number of visible trees (set automatically removes duplicates)
    print(len(visibleTrees))