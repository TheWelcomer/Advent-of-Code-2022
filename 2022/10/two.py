with open("noops.txt", "r") as f:
    with open("noopOutput.txt", "w") as o:
        data = f.readlines()
        writeString = ""
        timesVals = []
        intermediateVals = []
        x = 1
        clockCycle = 0
        for line in data:
            line = line.strip()
            if line == "noop":
                clockCycle += 1
                column = clockCycle % 40 - 1
                if column == 0:
                    writeString += "\n"
                if abs(x - column) <= 1:
                    writeString += "#"
                else:
                    writeString += "."
                #beam
            else:
                clockCycle += 1
                column = clockCycle % 40 - 1
                if column == 0:
                    writeString += "\n"
                if abs(x - column) <= 1:
                    writeString += "#"
                else:
                    writeString += "."
                #beam
                clockCycle += 1
                column = clockCycle % 40 - 1
                if column == 0:
                    writeString += "\n"
                if abs(x - column) <= 1:
                    writeString += "#"
                else:
                    writeString += "."
                #beam
                casted = line[5:]
                x += int(line[5:])
        o.write(writeString)
        