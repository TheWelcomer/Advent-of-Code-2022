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
        if firstElfOne >= firstElfTwo and lastElfOne <= lastElfTwo:
            fullyContains += 1
        elif firstElfTwo >= firstElfOne and lastElfTwo <= lastElfOne:
            fullyContains += 1
    print(fullyContains)