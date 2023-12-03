with open("data.txt", 'r') as f:
    colormap = {
        'r': 0,
        'g': 1,
        'b': 2
    }
    cubecap = [12, 13, 14]
    result = 0
    lines = f.readlines()
    for i in range(len(lines)):
        outcont = False
        games = lines[i].split(": ")[1].strip("\n").split("; ")
        numrgb = [0, 0, 0]
        for game in games:
            blocks = game.split(", ")
            for block in blocks:
                block = block.replace("red", "r").replace("green", "g").replace("blue", "b")
                numrgb[colormap[block[-1]]] += int(block.split(" ")[0])
            for j in range(3):
                if cubecap[j] < numrgb[j]:
                    outcont = True
            numrgb = [0, 0, 0]
            if outcont: break
        if outcont: continue
        result += i + 1
    print(result)