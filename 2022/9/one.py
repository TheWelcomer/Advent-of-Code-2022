with open('bridgeDirections.txt', 'r') as f:
    visited = set()
    head = [0, 0]
    tail = [0, 0]
    for line in f.readlines():
        line = line.strip('\n')
        direciton = line[0]
        distance = int(line[2:])
        for i in range(distance):
            visited.add(tuple(tail))
            if direciton == 'R':
                head[0] += 1
            elif direciton == 'L':
                head[0] -= 1
            elif direciton == 'U':
                head[1] += 1
            elif direciton == 'D':
                head[1] -= 1
            if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
                continue
            if head[0] - tail[0] == 0 and head[1] - tail[1] > 0:
                tail[1] += 1
                continue
            if head[0] - tail[0] == 0 and head[1] - tail[1] < 0:
                tail[1] -= 1
                continue
            if head[1] - tail[1] == 0 and head[0] - tail[0] > 0:
                tail[0] += 1
                continue
            if head[1] - tail[1] == 0 and head[0] - tail[0] < 0:
                tail[0] -= 1
                continue
            
            if head[0] - tail[0] > 0 and head[1] - tail[1] > 0:
                tail[0] += 1
                tail[1] += 1
                continue
            if head[0] - tail[0] > 0 and head[1] - tail[1] < 0:
                tail[0] += 1
                tail[1] += -1
                continue
            if head[0] - tail[0] < 0 and head[1] - tail[1] > 0:
                tail[0] += -1
                tail[1] += 1
                continue
            if head[0] - tail[0] < 0 and head[1] - tail[1] < 0:
                tail[0] += -1
                tail[1] += -1
                continue

            visited.add(tuple(tail))
    print(len(visited))
