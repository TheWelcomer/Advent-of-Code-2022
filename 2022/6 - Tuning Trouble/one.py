with open("signal.txt") as signal:
    signal = signal.read()
    marker = []
    readChars = 0
    for char in signal:
        breakOut = True
        if len(marker) < 4:
            marker.append(char)
            readChars += 1
            continue
        for markerChar in marker:
            if marker.count(markerChar) > 1:
                breakOut = False
        if breakOut:
            break
        marker.pop(0)
        marker.append(char)
        readChars += 1
        
    print(readChars)
        