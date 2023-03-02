with open("data.txt", "r") as f:
    data = f.read()
    paperTotal = 0
    for line in data.splitlines():
        line = line.split("x")
        l = int(line[0])
        w = int(line[1])
        h = int(line[2])
        paperTotal += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    print(paperTotal)