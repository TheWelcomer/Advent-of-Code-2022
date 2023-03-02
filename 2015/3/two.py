with open("data.txt", "r") as f:
    data = f.read()
    
    houseLocations = set()
    houseLocations.add((0, 0))
    santaXLocation = 0
    santaYLocation = 0
    roboXLocation = 0
    roboYLocation = 0
    turnTracker = 0
    
    for char in data:
        if turnTracker % 2 == 0:
            if char == ">":
                santaXLocation += 1
            elif char == "<":
                santaXLocation -= 1
            elif char == "^":
                santaYLocation += 1
            elif char == "v":
                santaYLocation -= 1
            houseLocations.add((santaXLocation, santaYLocation))
            
        else:
            if char == ">":
                roboXLocation += 1
            elif char == "<":
                roboXLocation -= 1
            elif char == "^":
                roboYLocation += 1
            elif char == "v":
                roboYLocation -= 1
            houseLocations.add((roboXLocation, roboYLocation))
            
        turnTracker += 1
        
    print(len(houseLocations))