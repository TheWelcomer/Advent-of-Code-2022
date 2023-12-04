with open("data.txt", 'r') as f:
    result = 0
    lines = f.readlines()
    cards = [1 for i in range(len(lines))]
    for i in range(len(lines)):
        matches = 0
        for j in range(len(lines[i])):
            if lines[i][j] == ':':
                j += 2
                break
        win, have = lines[i][j:].strip().split(' | ')
        win = set(win.split(' '))
        have = have.split(' ')
        for num in have:
            if num != ' ' and num != '' and num in win:
                matches += 1
        for j in range(i + 1, i + 1 + matches):
            cards[j] += cards[i]
        result += cards[i]
    print(result)