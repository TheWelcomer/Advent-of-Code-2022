import re

valids = []
ligmaValids = []

with open("data.txt", "r") as f:
    data = f.readlines()
    count = 0
    for word in data:
        if re.search('(?:[aeiou].*){3}',word)==None:
            continue
        if re.search('(.)\\1',word)==None:
            continue
        if not re.search('(?:ab|cd|pq|xy)',word)==None:
            continue
        count += 1
        valids.append(word)
    print(count)
    print(valids)

with open("data.txt", "r") as f:
    data = f.readlines()
    naughty = ["ab", "cd", "pq", "xy"]
    numNice = 0
    for line in data:
        naughtyCombo = False
        appearTwice = False
        numVowels = 0
        for i in range(len(line)):
            if i != len(line) - 1:
                if line[i:i + 1] in ["ab", "cd", "pq", "xy"]:
                    naughtyCombo = True
                    break
                if line[i + 1] == line[i]:
                    appearTwice = True
            if line[i] in ["a", "e", "i", "o", "u"]:
                numVowels += 1
        if (not naughtyCombo) and appearTwice and numVowels >= 3:
            numNice += 1
            if line in valids:
                ligmaValids.append(line)
    print(numNice)
    for valid in valids:
        if valid in ligmaValids:
            ligmaValids.remove(valid)
    print(ligmaValids)
    """
    B(b - 1 - c) - tc - k = 0
    Bb - B - Bc - tc - k = 0
    Bb - B - k = tc + Bc
    Bb - B - k = c(t + B)
    c = (Bb - B - k)/(t + B)
    
    """