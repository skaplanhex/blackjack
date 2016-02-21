from deck import *
from player import *
import sys

def drawCard(deck,player):
    player.addToHand( deck.getNextCard() )

def deal(deck,player,dealer):
    player.nextHand()
    dealer.nextHand()
    drawCard(deck,player)
    drawCard(deck,dealer)
    drawCard(deck,player)
    drawCard(deck,dealer)
def quitGame():
    print "OK, thanks for playing!"
    sys.exit(0)

def checkIfQuit(s):
    if s == 'quit':
        quitGame()
def playHand(deck,player,dealer):
    deal(deck,player,dealer)
    # calculate player total
    playerTotal = player.total()
    softHand = False
    if playerTotal < 0:
        playerTotal += 1000
        softHand = True
    print " "
    print "The cards have been dealt!"
    print "Your cards are the %s and the %s."%player.getHandStrTuple()
    print player.getTotalString()
    print "The dealer has the %s showing."%dealer.firstCardStr()
    print " "
    nextAction = raw_input("Would you like to hit or stay? ").lower()
    checkIfQuit(nextAction)
    while nextAction not in ['hit','stay']:
        nextAction = raw_input("Please choose either hit, stay, or quit: ").lower()
        checkIfQuit(nextAction)
    if nextAction == 'hit':
        drawCard(deck,player)
        print player.getHandStr()
        print player.getTotalString()



def main():
    # deck = Deck(1)
    # card = deck.drawCard()
    # print "first card: " + card.rank + " of " + card.suit
    debug = True

    print "****************************************"
    print "*                                      *"
    print "*         Welcome to Blackjack         *"
    print "*          by Steven M. Kaplan         *"
    print "*                                      *"
    print "****************************************"

    playerName = "Steve"
    if not debug:
        playerName = raw_input('Please enter your name: ')
    print "Welcome %s!"%playerName
    toPlay = 'y'
    if not debug:
        toPlay = raw_input('Would you like to start playing now? ').lower() #make lowercase

    if toPlay not in ['y','yes','eys','ye','ys']:
        print "OK then...thanks for visiting I guess!"
        sys.exit(0)
    else:
        numDecks = 5
        if not debug:
            print "Excellent! To quit at any time, just type quit."
            numDecks = raw_input("OK, how many decks do you want to play with? ")
            checkIfQuit(numDecks)
            numDecks = int(numDecks)
        print "Great; creating a shoe made of %i decks. Let's play!"%numDecks
        deck = Deck(numDecks)
        donePlaying = False
        player = Player(playerName)
        dealer = Player("Dealer")
        while not donePlaying:
            playHand(deck,player,dealer)
            keepPlaying = raw_input("Would you like to continue playing? ")
            if keepPlaying not in ['y','yes','eys','ye','ys']:
                quitGame()

if __name__ == "__main__":
    main()

