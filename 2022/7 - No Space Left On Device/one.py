
with open("data.txt", "r") as f:
    directoryMap = {}
    filesizeMap = {}
    filepathStack = []
    data = f.readlines()
    for line in data:
        line = line.strip()
        if "$ cd .." in line:
            filepathStack.pop()
        elif "$ cd /" in line:
            filepathStack = ["/"]
            if not str(filepathStack) in directoryMap:
                directoryMap[str(filepathStack)] = [0 , []]
        elif "$ cd" in line:
            currentDir = line[5:]
            filepathStack.append(currentDir)
            if not str(filepathStack) in directoryMap:
                directoryMap[str(filepathStack)] = [0 , []]
        elif "$ ls" in line:
            continue
        elif "dir" in line:
            directoryList = directoryMap.get(str(filepathStack))
            filename = filepathStack[:]
            filename.append(line[4:])
            directoryList[1].append(str(filename))
            directoryMap[str(filepathStack)] = directoryList
        else:
            directoryList = directoryMap.get(str(filepathStack))
            filesize = int(line.split(" ")[0])
            directoryList[0] += filesize
            directoryMap[str(filepathStack)] = directoryList    
    dirsizeMap = {}
    def dirsizeFinder(bigDirectory):
        if directoryMap[bigDirectory][1] == []:
            return directoryMap[bigDirectory][0]
        else:
            bigDirsize = directoryMap[bigDirectory][0]
            for littleDirectory in directoryMap[bigDirectory][1]:
                if littleDirectory in dirsizeMap:
                    bigDirsize += dirsizeMap[littleDirectory]
                else:
                    littleDirsize = dirsizeFinder(littleDirectory)
                    dirsizeMap[littleDirectory] = littleDirsize
                    bigDirsize += littleDirsize
            dirsizeMap[bigDirectory] = bigDirsize
            return bigDirsize
    totalDirsize = 0
    for directory in directoryMap.keys():
        dirsize = dirsizeFinder(directory)
        if dirsize <= 100000:
            totalDirsize += dirsize
    print(totalDirsize)