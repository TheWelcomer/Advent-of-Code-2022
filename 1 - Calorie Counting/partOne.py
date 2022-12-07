with open("data.txt") as data:

    firstCalories = 0
    secondCalories = 0
    thirdCalories = 0
    currentCalories = 0
    for line in data.readlines():
        if line != "\n":
            currentCalories += int(line)
        else:
            if currentCalories > firstCalories:
                firstCalories = currentCalories
            currentCalories = 0

print(firstCalories)