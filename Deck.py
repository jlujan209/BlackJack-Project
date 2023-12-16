from Card import card
from Player import player
import random

class deck:
    #Initializes the game deck with the card file and holds all cards in a list 
    #that will be used as a stack.
    def __init__(self, filename):
        self.cards = list()
        
        CardFile = open(filename, 'r')
        lines = CardFile.readlines()

        #read cards into deck's list
        for line in lines:
            details = line.split(" ")
            cardNum = int(details[0])
            cardType = details[1].rstrip('\r\n')
            currCard = card(cardNum, cardType)
            self.cards.append(currCard)
    
    #Prints the current deck (Used for testing purposes)
    def printDeck(self):
        for card in self.cards:
            card.printCard()
    
    #Shuffles the cards in the deck
    def shuffleCards(self):
        for i in range(len(self.cards)):
            randIndx = random.randint(0,51)

            #swap cards at random
            currCard = self.cards[i]
            self.cards[i] = self.cards[randIndx]
            self.cards[randIndx] = currCard

    #Deals cards from top of the deck to either house or player
    def dealCard(self, user):
        user.addCardToHand(self.cards.pop())