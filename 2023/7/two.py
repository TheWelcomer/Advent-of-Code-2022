types = {
    '5': 6,
    '41': 5,
    '32': 4,
    '311': 3,
    '221': 2,
    '2111': 1,
    '11111': 0
}

cardVals = {
    'A': 'm', 
    'K': 'l',
    'Q': 'k',  
    'T': 'j', 
    '9': 'i', 
    '8': 'h', 
    '7': 'g', 
    '6': 'f', 
    '5': 'e', 
    '4': 'd', 
    '3': 'c', 
    '2': 'b',
    'J': 'a'
}

with open("data.txt", 'r') as f:
    result = 0
    hands = []
    data = f.readlines()
    for i in range(len(data)):
        hand, bid = data[i].strip('\n').split(' ')
        sortedHand = sorted(hand)
        numCards = {}
        jokers = 0
        for card in sortedHand:
            if card == 'J':
                jokers += 1
            else:
                numCards[card] = numCards.get(card, 0) + 1
        typeVal = ''
        for val in numCards.values():
            typeVal += str(val)
        notFunny = ''.join(sorted(typeVal, reverse=True))
        funny = str((int(notFunny[0]) if len(notFunny) > 0 else 0) + jokers) + notFunny[1:]
        typeVal = types[funny]
        cardVal = ''
        for card in hand:
            cardVal += str(cardVals[card])
        hands.append((typeVal, cardVal, bid))
    hands.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(hands)):
        result += (i + 1) * int(hands[i][2])
    print(result)