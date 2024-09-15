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
    numOnes = [0 for i in range(len(data[0].strip()))]
    for binary in data:
        binary = binary.strip()
        for i in range(len(binary)):
            if binary[i] == '1':
                numOnes[i] += 1
    gamma = ''
    epsilon = ''
    for i in range(len(numOnes)):
        if numOnes[i] > (len(data)//2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma = binaryToDecimal(int(gamma))
    epsilon = binaryToDecimal(int(epsilon))
    result = gamma*epsilon
    print(result, gamma, epsilon, numOnes)