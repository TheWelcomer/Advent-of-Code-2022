with open("data.txt", "r") as f:
    data = f.read()
    ribbonTotal = 0
    for line in data.splitlines():
        line = line.split("x")
        l = int(line[0])
        w = int(line[1])
        h = int(line[2])
        ribbonTotal += l*w*h + 2*min(l+w, w+h, h+l)
    print(ribbonTotal)