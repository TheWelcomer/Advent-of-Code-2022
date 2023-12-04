with open("data.txt", 'r') as f:
    result = 0
    i = 1
    for line in f.readlines():
        matches = 0
        for j in range(len(line)):
            if line[j] == ':':
                j += 2
                break
        
        win, have = line[j:].strip().split(' | ')
        win = set(win.split(' '))
        have = have.split(' ')
        for num in have:
            if num != ' ' and num != '' and num in win:
                matches += 1
        if matches > 0: result += pow(2, matches - 1)
        i += 1
    print(result)