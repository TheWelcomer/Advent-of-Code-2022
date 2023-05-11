with open("data.txt", "r") as f:
    data = f.read()
    sensorCoverage = []
    for line in data.readlines():
        line = line.replace("Sensor at ", "")
        line = line.replace(": closest beacon is at ", ",")
        line = line.replace(", ", ",")
        line = line.strip("\n")
        sensorX, sensorY, beaconX, beaconY = line.split(",")
        sensorCoverage.append((sensorX, sensorY), (beaconX - sensorX) + (beaconY - sensorY))
    