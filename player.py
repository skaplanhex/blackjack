from deck import *

class Player:
    def __init__(self,tempName):
        self.name = tempName
        self.hand = []
    def addToHand(self,card):
        self.hand.append(card)
    def nextHand(self):
        self.hand = []
    def total(self):
        currentTotal=0
        for card in self.hand:
            currentTotal += card.getValue()
        return currentTotal
    def getHandStrs(self):
        l = [ card.getStr() for card in self.hand]
        return tuple(l)
    def firstCardStr(self):
        return self.hand[0].getStr()