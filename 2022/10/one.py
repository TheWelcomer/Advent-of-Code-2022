monkeyZero = {
    "startingItems": [74, 64, 74, 63, 53],
    "operation": "old * 7",
    "test": 5,
    "ifTrue": 1,
    "ifFalse": 6,
    "throws": 0 
}

monkeyOne = {
    "startingItems": [69, 99, 95, 62],
    "operation": "old * old",
    "test": 17,
    "ifTrue": 2,
    "ifFalse": 5,
    "throws": 0
}

monkeyTwo = {
    "startingItems": [59, 81],
    "operation": "old + 8",
    "test": 7,
    "ifTrue": 4,
    "ifFalse": 3,
    "throws": 0
}

monkeyThree = {
    "startingItems": [50, 67, 63, 57, 63, 83, 97],
    "operation": "old + 4",
    "test": 13,
    "ifTrue": 0,
    "ifFalse": 7,
    "throws": 0
}

monkeyFour = {
    "startingItems": [61, 94, 85, 52, 81, 90, 94, 70],
    "operation": "old + 3",
    "test": 19,
    "ifTrue": 7,
    "ifFalse": 3,
    "throws": 0
}

monkeyFive = {
    "startingItems": [69],
    "operation": "old + 5",
    "test": 3,
    "ifTrue": 4,
    "ifFalse": 2,
    "throws": 0
}

monkeySix = {
    "startingItems": [54, 55, 58],
    "operation": "old + 7",
    "test": 11,
    "ifTrue": 1,
    "ifFalse": 5,
    "throws": 0
}

monkeySeven = {
    "startingItems": [79, 51, 83, 88, 93, 76],
    "operation": "old * 3",
    "test": 2,
    "ifTrue": 0,
    "ifFalse": 6,
    "throws": 0
}

monkeys = [monkeyZero, monkeyOne, monkeyTwo, monkeyThree, monkeyFour, monkeyFive, monkeySix, monkeySeven]

for i in range(10000):
    for monkey in monkeys:
        while len(monkey.get("startingItems")) > 0:
            old = monkey.get("startingItems").pop(0)
            new = eval(monkey.get("operation")) % 9699690
            if new % monkey.get("test") == 0:
                monkeys[monkey.get("ifTrue")].get("startingItems").append(new)
                monkey["throws"] = monkey.get("throws") + 1
            else:
                monkeys[monkey.get("ifFalse")].get("startingItems").append(new)
                monkey["throws"] = monkey.get("throws") + 1

firstMost = 0
secondMost = 0
for monkey in monkeys:
    print(monkey.get("throws"))
for monkey in monkeys:
    if(monkey.get("throws") > firstMost):
        secondMost = firstMost
        firstMost = monkey.get("throws")
    elif(monkey.get("throws") > secondMost):
        secondMost = monkey.get("throws")
print(firstMost * secondMost)
    
    