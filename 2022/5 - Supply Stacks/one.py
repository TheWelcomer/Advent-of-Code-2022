one = ['n', 'c', 'r', 't', 'm', 'z', 'p']
two = ['d', 'n', 't', 's', 'b', 'z']
three = ['m', 'h', 'q', 'r', 'f', 'c', 't', 'g']
four = ['g', 'r', 'z']
five = ['z', 'n', 'r', 'h']
six = ['f', 'h', 's', 'w', 'p', 'z', 'l', 'd']
seven = ['w', 'd', 'z', 'r', 'c', 'g', 'm']
eight = ['s', 'j', 'f', 'l', 'h', 'w', 'z', 'q']
nine = ['s', 'q', 'p', 'w', 'n']

craneMappings = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine
}

with open("craneInstructions.txt") as instructions:
    for line in instructions.readlines():
        line = line.strip("\n")
        words = line.split(" ")
        numMoved = int(words[1])
        moveFrom = int(words[3])
        moveTo = int(words[5])
        for i in range(numMoved):
            movedCrate = craneMappings.get(moveFrom).pop()
            craneMappings.get(moveTo).append(movedCrate)
    
    print(one[-1], two[-1], three[-1], four[-1], five[-1], six[-1], seven[-1], eight[-1], nine[-1])