with open('data.txt', 'r') as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip().split()
        data[i][1] = int(data[i][1])
    depth = 0
    horizontalPosition = 0
    for move in data:
        direction, distance = move
        if direction == 'forward':
            horizontalPosition += distance
        if direction == 'down':
            depth += distance
        if direction == 'up':
            depth -= distance
    result = depth*horizontalPosition
    print(result)