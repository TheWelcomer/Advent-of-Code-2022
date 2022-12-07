with open("strategy.txt") as strategy_file:
    score = 0
    x = ["A Y", "B X", "C Z"]
    y = ["A Z", "B Y", "C X"]
    z = ["B Z", "C Y", "A X"]
    loss = ["A X", "B X", "C X"]
    tie = ["A Y", "B Y", "C Y"]
    win = ["A Z", "B Z", "C Z"]
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