DATA = """HIDDEN"""

cleanedData = DATA.splitlines()

tot = 0
matchTable = []
for card in cleanedData:
    tempcards = card.split(" ")
    tempcards = tempcards[2:]
    valMyCard = []
    valOpened = []
    myCard = True
    for item in tempcards:
        if item == "|":
            myCard = False
            continue
        if item != "":
            if myCard:
                valMyCard.append(item)
            else:
                valOpened.append(item)
    print((len(valMyCard), len(valOpened)))
    print(valMyCard)
    setMyCard = set(valMyCard)
    setOpened = set(valOpened)
    matches = len(setMyCard.intersection(setOpened))
    matchTable.append(matches)
    # if matches >= 1:
    #    tot += (2 ** (matches-1))
cardTable = [1 for i in range(0, len(matchTable))]
print(matchTable)
for i in range(0, len(matchTable)):
    iterCards = cardTable[i]
    iterMatches = matchTable[i]
    for j in range(i+1, i+iterMatches+1):
        try:
            cardTable[j] += iterCards
        except IndexError:
            pass
print(tot)
print(cardTable)
print(sum(cardTable))
