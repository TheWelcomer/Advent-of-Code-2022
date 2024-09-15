import re

with open("data.txt", 'r') as f:
    graph = {}
    data = f.read()
    traversal = re.findall(r'\w*', data)[0]
    mapPattern = re.compile(r'(\w\w\w)\s=\s\((\w\w\w),\s(\w\w\w)\)')
    matches = mapPattern.finditer(data)
    for match in matches:
        graph[match.group(1)] = (match.group(2), match.group(3))
    i = 0
    location = 'AAA'
    while location != 'ZZZ':
        if traversal[i % len(traversal)] == 'L':
            turn = 0  
        else:
            turn = 1
        location = graph[location][turn]
        print(location)
        i += 1
        print(i)
        if i == 1000000000: break
    print(i)