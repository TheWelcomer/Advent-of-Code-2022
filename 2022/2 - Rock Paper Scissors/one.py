with open("strategy.txt") as strategy_file:
    score = 0
    win = ["A Y", "B Z", "C X"]
    tie = ["A X", "B Y", "C Z"]
    loss = ["B X", "C Y", "A Z"]
    x = ["A X", "B X", "C X"]
    y = ["A Y", "B Y", "C Y"]
    z = ["A Z", "B Z", "C Z"]
    for line in strategy_file.readlines():
        line = line.replace("\n", "")
        if(line in win):
            score += 6
        elif(line in tie):
            score += 3
        else:
            score += 0
        if(line in x):
            score += 1
        elif(line in y):
            score += 2
        else:
            score += 3
    
    print(score)