directoryIndexMap = {}
with open("rootDirectory.txt") as root:
    for line in root.readlines():
        root = []
        line.strip("\n")
        if line.startswith("$cd "): focusedDirectory = line[4:]
        if line.startswith("$ ls"):
            record = True
        while record:
            