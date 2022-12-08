with open("sectionsList.txt") as sectionsList:
    fullyContains = 0
    for sections in sectionsList.readlines():
        sections = sections.replace("\n", "")
        secSplit = sections.split(",")
        elfOne = secSplit[0]
        elfListOne = elfOne.split("-")
        firstElfOne = int(elfListOne[0])
        lastElfOne = int(elfListOne[1])
        elfTwo = secSplit[1]
        elfListTwo = elfTwo.split("-")
        firstElfTwo = int(elfListTwo[0])
        lastElfTwo = int(elfListTwo[1])
        if lastElfOne < firstElfTwo:
            continue
        elif lastElfTwo < firstElfOne:
            continue
        fullyContains += 1
    print(fullyContains)
    """
    [10, 15] [11, 14]
    [10, 15] [11, 16]
    [10, 15] [9, 14]
    [10, 15] [9, 16]
    """