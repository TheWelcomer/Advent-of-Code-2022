with open("data.txt", 'r') as f:
    result = 0
    nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    schematic = f.readlines()
    for i in range(len(schematic)):
        schematic[i] = schematic[i].strip("\n")
    for y in range(len(schematic)):
        for x in range(len(schematic[0])):
            char = schematic[y][x]
            if char in nums or char == '.':
                continue
            visited = set()
            for scanY in range(y - 1, y + 2):
                for scanX in range(x - 1, x + 2):
                    if scanY >= 0 and scanY < len(schematic) and scanX >= 0 and scanX < len(schematic[0]) and schematic[scanY][scanX] in nums and (scanX, scanY) not in visited:
                        nearChar = schematic[scanY][scanX]
                        numbuff = ''
                        while (scanX > 0 and schematic[scanY][scanX - 1] in nums):
                            scanX -= 1
                        while (scanX < len(schematic[0]) and schematic[scanY][scanX] in nums):
                            visited.add((scanX, scanY))
                            numbuff += schematic[scanY][scanX]
                            scanX += 1
                        if numbuff != '': result += int(numbuff)
    print(result)