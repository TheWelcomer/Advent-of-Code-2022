with open("data.txt", "r") as f:
    data = f.readlines()
    numNice = 0
    for line in data:
        naughtyCombo = False
        appearTwice = False
        numVowels = 0
        for i in range(len(line)):
            if i != len(line) - 1:
                liner = line[i:i + 2]
                if liner in ["ab", "cd", "pq", "xy"]:
                    naughtyCombo = True
                    break
                if line[i + 1] == line[i]:
                    appearTwice = True
            if line[i] in ["a", "e", "i", "o", "u"]:
                numVowels += 1
        if (not naughtyCombo) and appearTwice and numVowels >= 3:
            numNice += 1
    print(numNice)