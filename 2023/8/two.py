import re

def complete(locations):
    for location in locations:
        if location[2] != 'Z':
            return False
    return True

with open("data.txt", 'r') as f:
    graph = {}
    data = f.read()
    locations = []
    traversal = re.findall(r'\w*', data)[0]
    mapPattern = re.compile(r'(\w\w\w)\s=\s\((\w\w\w),\s(\w\w\w)\)')
    locationPattern = re.compile(r'(\w\wA)\s=')
    rawLocations = locationPattern.finditer(data)
    matches = mapPattern.finditer(data)
    for match in matches:
        graph[match.group(1)] = (match.group(2), match.group(3))
    for location in rawLocations:
        locations.append(location.group(1))
    i = 0
    while True:
        explored = set()
        newLocations = []
        for j in range(len(locations)):
            if locations[j] not in explored:
                if traversal[i % len(traversal)] == 'L':
                    turn = 0
                else:
                    turn = 1
                newLocations.append(graph[locations[j]][turn])
                explored.add(locations[j])
        locations = newLocations
        i += 1
        print(locations)
        if complete(locations): break
    print(i)