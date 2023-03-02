with open("data.txt", "r") as f:
    data = f.read()
    floor = 0
    for char in data:
        if char == "(":
            floor += 1
        else:
            floor -= 1
    print(floor)