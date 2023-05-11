with open("data.txt", "r") as file:
    # Memoization will have the key be a list key with
    data = file.readlines()
    memoized = {}
    pipeMap = {}
    for line in data:
        line = line.replace(" has flow rate=", ",").replace(", ", ",").replace("Valve ", "").replace("; tunnels lead to valves ", ",").replace("; tunnel leads to valve ", ",").strip("\n")
        valveComponents = line.split(",")
        pipeMap[valveComponents[0]] = (int(valveComponents[1]), valveComponents[2:])
        