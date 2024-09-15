with open('data.txt', 'r') as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = int(data[i])
    numIncrease = 0
    lastSum = data[0] + data[1] + data[2]
    sum = data[1] + data[2] + data[3]
    for i in range(1, len(data) - 3):
        if sum > lastSum:
            numIncrease += 1
        lastSum = sum
        sumTail = data[i]
        sumHead = data[i + 3]
        sum = sum - sumTail + sumHead
    if sum > lastSum:
        numIncrease += 1
    print(numIncrease)