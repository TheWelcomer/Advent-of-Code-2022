with open("data.txt", "r") as f:
    data = f.readlines()
    numNice = 0
    for line in data:
        pairs = set()
        pairOfPairs = False
        sandwichPair = False
        previousPair = ""
        for i in range(len(line) - 1):
            currentPair = line[i: i + 2]
            if currentPair in pairs:
                pairOfPairs = True
                break
            pairs.add(previousPair)
            previousPair = currentPair
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                sandwichPair = True
                break
        if pairOfPairs and sandwichPair:
            numNice += 1
    print(numNice)