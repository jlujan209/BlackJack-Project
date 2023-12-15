from Card import card
from Player import player
import random

class deck:
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
    
    def printDeck(self):
        for card in self.cards:
            card.printCard()
            
    def shuffleCards(self):
        for i in range(len(self.cards)):
            randIndx = random.randint(0,51)

            #swap cards at random
            currCard = self.cards[i]
            self.cards[i] = self.cards[randIndx]
            self.cards[randIndx] = currCard

    def dealCard(self, user):
        user.addCardToHand(self.cards.pop())