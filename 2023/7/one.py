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
    'J': 'j', 
    'T': 'i', 
    '9': 'h', 
    '8': 'g', 
    '7': 'f', 
    '6': 'e', 
    '5': 'd', 
    '4': 'c', 
    '3': 'b', 
    '2': 'a'
}

with open("data.txt", 'r') as f:
    result = 0
    hands = []
    data = f.readlines()
    for i in range(len(data)):
        hand, bid = data[i].strip('\n').split(' ')
        sortedHand = sorted(hand)
        numCards = {}
        for card in sortedHand:
            numCards[card] = numCards.get(card, 0) + 1
        typeVal = ''
        for val in numCards.values():
            typeVal += str(val)
        typeVal = types[''.join(sorted(typeVal, reverse=True))]
        cardVal = ''
        for card in hand:
            cardVal += str(cardVals[card])
        hands.append((typeVal, cardVal, bid))
    hands.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(hands)):
        result += (i + 1) * int(hands[i][2])
    print(result)