with open('data.txt', 'r') as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip().split()
        data[i][1] = int(data[i][1])
    depth = 0
    horizontalPosition = 0
    aim = 0
    for move in data:
        direction, distance = move
        if direction == 'forward':
            horizontalPosition += distance
            depth += aim*distance
        if direction == 'down':
            aim += distance
        if direction == 'up':
            aim -= distance
    result = depth*horizontalPosition
    print(result)