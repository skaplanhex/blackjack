import random

class Card:
    def __init__(self,tempRank,tempSuit):
        self.rank = tempRank
        self.suit = tempSuit

# dictionary that gives each type of card a number identifier to be used with the random number generator
deckDict = {
    0 : Card("2","hearts"),
    1 : Card("3","hearts"),
    2 : Card("4","hearts"),
    3 : Card("5","hearts"),
    4 : Card("6","hearts"),
    5 : Card("7","hearts"),
    6 : Card("8","hearts"),
    7 : Card("9","hearts"),
    8 : Card("10","hearts"),
    9 : Card("jack","hearts"),
    10 : Card("queen","hearts"),
    11 : Card("king","hearts"),
    12 : Card("ace","hearts"),
    13 : Card("2","diamonds"),
    14 : Card("3","diamonds"),
    15 : Card("4","diamonds"),
    16 : Card("5","diamonds"),
    17 : Card("6","diamonds"),
    18 : Card("7","diamonds"),
    19 : Card("8","diamonds"),
    20 : Card("9","diamonds"),
    21 : Card("10","diamonds"),
    22 : Card("jack","diamonds"),
    23 : Card("queen","diamonds"),
    24 : Card("king","diamonds"),
    25 : Card("ace","diamonds"),
    26 : Card("2","clubs"),
    27 : Card("3","clubs"),
    28 : Card("4","clubs"),
    29 : Card("5","clubs"),
    30 : Card("6","clubs"),
    31 : Card("7","clubs"),
    32 : Card("8","clubs"),
    33 : Card("9","clubs"),
    34 : Card("10","clubs"),
    35 : Card("jack","clubs"),
    36 : Card("queen","clubs"),
    37 : Card("king","clubs"),
    38 : Card("ace","clubs"),
    39 : Card("2","spades"),
    40 : Card("3","spades"),
    41 : Card("4","spades"),
    42 : Card("5","spades"),
    43 : Card("6","spades"),
    44 : Card("7","spades"),
    45 : Card("8","spades"),
    46 : Card("9","spades"),
    47 : Card("10","spades"),
    48 : Card("jack","spades"),
    49 : Card("queen","spades"),
    50 : Card("king","spades"),
    51 : Card("ace","spades")
}

# return a list of the numbers [0,51] in random order that will be the result of "shuffling" the deck
def getDecks(numDecks,toShuffle=True):
    deck = [ deckDict[i%52] for i in range(52*numDecks) ]
    if toShuffle:
        random.shuffle(deck)
    return deck

def getDeck(toShuffle=True):
    return getDecks(1,toShuffle)

class Deck:
    def __init__(self,numDecks,shuffle=True):
        self.deck = getDecks(numDecks,shuffle)
    def numCards(self):
        return len(self.deck)
    def reshuffle(self):
        random.shuffle(self.deck)
    def drawCards(self,num):
        cardsToReturn = []
        for i in range(num):
            cardsToReturn.append( self.deck.pop(0) )
        return cardsToReturn
    def drawCard(self):
        return self.drawCards(1)[0]