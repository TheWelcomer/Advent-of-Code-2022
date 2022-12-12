with open('bridgeDirections.txt', 'r') as f:
    visited = set()
    knotList = []
    for i in range(10):
        knotList.append([0, 0])
    for line in f.readlines():
        line = line.strip('\n')
        direciton = line[0]
        distance = int(line[2:])
        for i in range(distance):
            if direciton == 'R':
                knotList[0][0] += 1
            elif direciton == 'L':
                knotList[0][0] -= 1
            elif direciton == 'U':
                knotList[0][1] += 1
            elif direciton == 'D':
                knotList[0][1] -= 1
            for knot in range(9):
                head = knotList[knot]
                tail = knotList[knot + 1]
                if knot == 8:
                    visited.add(tuple(tail))
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
            if knot == 8:
                visited.add(tuple(tail))
    print(len(visited))
