import os
file = open("info", "w")
file.write("What's up?")
file.close()
with open("data.txt") as data:

    firstCalories = 0
    secondCalories = 0
    thirdCalories = 0
    currentCalories = 0
    for line in data.readline():
        if line != "":
            currentCalories += line
        else:
            if currentCalories > firstCalories:
                thirdCalories = secondCalories
                secondCalories = firstCalories
                firstCalories = currentCalories
            elif currentCalories > secondCalories:
                thirdCalories = secondCalories
                secondCalories = currentCalories
            elif currentCalories > thirdCalories:
                thirdCalories = currentCalories
            currentCalories = 0
