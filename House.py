from Card import card
import random

class house:
    #cardSum holds the sum of the values of the cards in the house's current hand
    #hand holds the cards that form part of the house's current hand
    def __init__(self):
        self.cardSum = 0
        self.hand = list()

    #Dealer only shows one card from his hand to the player
    def showUpCard(self):
        currCard = self.hand[-1]
        currCard.printCard()

    def addCardToHand(self, card):
        #Count J, Q, & K as 10 points
        if card.getValue() > 10:
            self.cardSum += 10

        #Count A's as 1 or 21 depending on the points that the user currently has
        elif card.getValue() == 1:
            if self.cardSum + card.getValue() > 21:
                self.cardSum += 1
            else:
                self.cardSum += 11
        
        #Count regular cards as the value on the card
        else:
            self.cardSum += card.getValue()

        #Add card to hand
        self.hand.append(card)

    #Return the house's current sum for their hand
    def getSum(self):
        return self.cardSum
    
    #Checks if the house's total sum has passed 21
    def bust(self):
        return self.cardSum > 21
    
    #Determines if the house will 'hit' or 'stand'
    def hit(self):      ##FIXME: possible error, house never 'hits'
        if self.cardSum >= 17:
            return False
        elif self.cardSum <= 13:
            return True
        else:
            if random.randint(0,1) == 1:
                return True
            else:
                return False
    #Clears the house's hand
    def clearHand(self):
        self.hand.clear()

    #Prints the house's hand
    def printHand(self):
        for card in self.hand:
            card.printCard()
    