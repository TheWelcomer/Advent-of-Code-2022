with open("data.txt", 'r') as f:
    result = 0
    nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    wordnums = {
        'one': '1', 
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    for line in f.readlines():
        fchar, lchar = None, None
        for i in range(len(line)):
            char = None
            if line[i] in nums:
                char = line[i]
            for j in range(2, 5):
                if i >= j and line[i - j: i + 1] in wordnums.keys():
                    char = wordnums[line[i - j: i + 1]]
            if char:
                if not fchar: 
                    fchar = char
                lchar = char
        result += int(fchar + lchar)
    print(result)