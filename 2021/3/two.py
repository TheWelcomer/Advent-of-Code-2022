def binaryToDecimal(binary):
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

with open("data.txt", 'r') as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
    calcList = [True, False]
    for i in range(2):
        bitPosition = 0
        calcOxygen = calcList[i]
        filtered = data
        while len(filtered) != 1:
            numOnes = 0
            for binary in filtered:
                binary = binary.strip()
                if binary[bitPosition] == '1':
                    numOnes += 1
            numZeros = len(filtered) - numOnes
            if numOnes >= numZeros and calcOxygen:
                requiredBit = '1'
            if numOnes < numZeros and calcOxygen:
                requiredBit = '0'
            if numOnes >= numZeros and not calcOxygen:
                requiredBit = '0'
            if numOnes < numZeros and not calcOxygen:
                requiredBit = '1'
            newFiltered = []
            for binary in filtered:
                if binary[bitPosition] == requiredBit:
                    newFiltered.append(binary)
            filtered = newFiltered
            bitPosition += 1
        if calcOxygen:
            oxygen = filtered[0]
        else:
            scrubber = filtered[0]
    print(oxygen, scrubber)
    oxygen = binaryToDecimal(int(oxygen))
    scrubber = binaryToDecimal(int(scrubber))
    result = oxygen*scrubber
    print(result, oxygen, scrubber)