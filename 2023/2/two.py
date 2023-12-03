with open("data.txt", 'r') as f:
    colormap = {
        'r': 0,
        'g': 1,
        'b': 2
    }
    result = 0
    lines = f.readlines()
    for i in range(len(lines)):
        outcont = False
        games = lines[i].split(": ")[1].strip("\n").split("; ")
        maxrgb = [0, 0, 0]
        for game in games:
            numrgb = [0, 0, 0]
            blocks = game.split(", ")
            for block in blocks:
                block = block.replace("red", "r").replace("green", "g").replace("blue", "b")
                numrgb[colormap[block[-1]]] += int(block.split(" ")[0])
            for i in range(3):
                maxrgb[i] = max(numrgb[i], maxrgb[i])
        result += maxrgb[0] * maxrgb[1] * maxrgb[2]
    print(result)