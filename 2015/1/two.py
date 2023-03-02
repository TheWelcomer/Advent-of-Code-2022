with open("data.txt", "r") as f:
    data = f.read()
    floor = 0
    
    for i in range(len(data)):
        if floor == -1:
            print(i)
            break
        if data[i] == "(":
            floor += 1
        else:
            floor -= 1
