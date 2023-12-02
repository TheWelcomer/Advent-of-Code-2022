with open("data.txt", 'r') as f:
    result = 0
    nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    for line in f.readlines():
        fchar, lchar = None, None
        for char in line:
            if char in nums:
                if not fchar: 
                    fchar = char
                lchar = char
        result += int(fchar + lchar)
    print(result)