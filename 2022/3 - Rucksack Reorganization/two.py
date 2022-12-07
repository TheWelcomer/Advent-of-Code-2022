valDict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
}
with open("items.txt") as items:
    badges = []
    firstElf = ''
    secondElf = ''
    thirdElf = ''
    groupingNum = 1
    for line in items.readlines():
        line = line.replace('\n', '')
        if groupingNum % 3 == 1:
            firstElf = line
        if groupingNum % 3 == 2:
            secondElf = line
        if groupingNum % 3 == 0:
            thirdElf = line
            for letter in firstElf:
                if letter in secondElf and letter in thirdElf:
                    common = letter
                    break
            firstElf = ''
            secondElf = ''
            thirdElf = ''
            badges.append(common)
        groupingNum += 1
value = 0
for item in badges:
    value += valDict.get(item)
print(value)