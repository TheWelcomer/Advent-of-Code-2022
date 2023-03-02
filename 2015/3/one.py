with open("data.txt", "r") as f:
    data = f.read()
    houseLocations = set((0, 0))
    xLocation = 0
    yLocation = 0
    for char in data:
        if char == ">":
            xLocation += 1
        elif char == "<":
            xLocation -= 1
        elif char == "^":
            yLocation += 1
        elif char == "v":
            yLocation -= 1
        houseLocations.add((xLocation, yLocation))
    print(len(houseLocations))