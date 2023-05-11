letterElevation = {
    'a': 0,
    'S': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25,
    'E': 25
}
def surrounding(location):
    if location[0]
map = []
with open("data.txt") as data:
    start = []
    end = []
    currentRow = 0
    for line in data.readlines():
        currentCol = 0
        line = line.strip('\n')
        row = []
        for letter in line:
            if letter == 'S':
                start.append(currentRow)
                start.append(currentCol)
            elif letter == 'E':
                end.append(currentRow)
                end.append(currentCol)
            row.append(letterElevation[letter])
            currentCol += 1
        map.append(row)
        currentRow += 1
    
    location = start
    
    
    print(start, end, map)
    