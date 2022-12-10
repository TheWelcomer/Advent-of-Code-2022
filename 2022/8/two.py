with open("data.txt") as data:
    array = []
    bestSight = 0
    for line in data.readlines():
        line = line.replace("\n", "")
        numList = [*line]
        array.append(numList)

    for row in range(len(array)):
        for col in range(len(array[0])):
            height = array[row][col]
            sightMult = []
            numVisible = 0

            for i in range(col):
                if array[row][i] < height:
                    numVisible += 1
                else:
                    break
            sightMult.append(numVisible)
            numVisible = 0

            for i in range(len(array[0]) - 1 - col):
                if array[row][i] < height:
                    numVisible += 1
                else:
                    break
            sightMult.append(numVisible)
            numVisible = 0

            for i in range(row):
                if array[i][col] < height:
                    numVisible += 1
                else:
                    break
            sightMult.append(numVisible)
            numVisible = 0

            for i in range(len(array) - 1 - row):
                if array[i][col] < height:
                    numVisible += 1
                else:
                    break
            sightMult.append(numVisible)
            
            currentSight = 1
            for i in sightMult:
                currentSight *= i
            if currentSight > bestSight:
                bestSight = currentSight
    
    print(bestSight)
