def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

def sum(value):
    total = 0
    for item in value:
        if type(item) == int:
                total += item
        else:
            total += sum(dirSizes.get(item))
    return total

with open("rootDirectory.txt") as root:
    dirStack = ['/']
    dirSizes = {}
    dirIntSizes = {}
    for line in root.readlines():
        line = line.strip("\n")
        if line.startswith("$ cd .."):
            dirStack.pop()
        elif line.startswith("$ cd "): 
            dirStack.append(line[5:])
        elif line.startswith("$ ls"):
            dirSizes.update({str(dirStack[-1]): []})
        else:
            if containsNumber(line):
                dirSizes[dirStack[-1]].append(int(line[:line.index(" ")]))
            else:
                dirSizes[dirStack[-1]].append(line[4:])

    for key, value in dirSizes.items():
        total = sum(value)
        dirIntSizes.update({key: total})

    print(dirIntSizes)

    smallStackSize = 0
    for value in dirIntSizes.values():
        if value <= 100000:
            smallStackSize += value
    print(smallStackSize)