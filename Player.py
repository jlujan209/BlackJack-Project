from Card import card

class player:
    def __init__(self, name):
        self.name = name
        self.hand = list()
        self.cardSum = 0

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

    def printHand(self):
        for card in self.hand:
            card.printCard()
        
    def getSum(self):
        return self.cardSum
    
    def bust(self):
        return self.cardSum > 21