with open('data.txt', 'r') as f:
    data = f.readlines()
    numIncrease = 0
    lastEntry = float('inf')
    for num in data:
        num = int(num)
        if num > lastEntry:
            numIncrease += 1
        lastEntry = num
    print(numIncrease)