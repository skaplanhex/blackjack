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
    def getHandStrTuple(self):
        l = [ card.getStr() for card in self.hand]
        return tuple(l)
    def firstCardStr(self):
        return self.hand[0].getStr()
    def getTotalString(self):
        tot = self.total()
        if tot > 0 and tot <= 21: # i.e. no ace and didn't bust
            return "Your total is %i."%tot
        elif tot > 21:
            return "Your total is %i. Bust!"%tot
        else:
            tot += 1000
            if len(self.hand) == 2 and tot+11 == 21:
                return "Blackjack!!!"
            else:
                return "Your total is a soft %i."%(tot+11)
    def getHandStr(self):
        if len(self.hand) == 2:
            return "Your cards are the %s and the %s."%player.getHandStrTuple()
        else:
            tempStr = "Your cards are the %s"%self.hand[0].getStr()
            for i,card in enumerate(self.hand):
                if i == 0:
                    continue
                elif i == len(self.hand)-1:
                    tempStr += ", and the %s."%card.getStr()
                else:
                    tempStr += ", the %s"%card.getStr()
            return tempStr