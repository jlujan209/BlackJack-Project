from Card import card

class player:
    #totalPoints holds the 'money' that the user can bet
    #name holds the user's name for the prupose of tracking high scores
    #hand holds the cards that form part of the user's current hand
    #cardSum holds the sum of the values of the cards in the user's current hand
    #tokens holds the 'chips' that the user is able to bet
    def __init__(self, name):
        self.totalPoints = 2500
        self.name = name
        self.hand = list()
        self.cardSum = 0
        self.tokens = {50 : 4, 100 : 4, 200 : 2, 500 : 1, 1000 : 1}

    #Displays the tokens that the user currently has
    def printTokens(self):
        print(f'Total Tokens: {self.totalPoints}')
        print(f'\t1) Token 50, Quantity :  {self.tokens[50]}')
        print(f'\t2) Token 100, Quantity : {self.tokens[100]}')
        print(f'\t3) Token 200, Quantity : {self.tokens[200]}')
        print(f'\t4) Token 500, Quantity : {self.tokens[500]}')
        print(f'\t5) Token 1000, Quantity : {self.tokens[1000]}')
    
    #Determines if the user can place the selected token, based on if the user has that token in posession
    def canPlaceToken(self, selection):
        if selection == 1:
            return self.tokens[50] > 0
        elif selection == 2:
            return self.tokens[100] > 0
        elif selection == 3:
            return self.tokens[200] > 0
        elif selection == 4:
            return self.tokens[500] > 0
        elif selection == 5:
            return self.tokens[1000] > 0

    #Returns the player's current points
    def getPlayerPoints(self):
        return self.totalPoints
    
    #Receives a list of tokens to be placed and subtracts them from players tokens (chips)
    def placeBet(self, token):
        self.tokens[token] -= 1
        self.totalPoints -= token

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

    #Prints the user's current hand
    def printHand(self):
        for card in self.hand:
            card.printCard()
    
    #Returns the sum of the values of the user's current hand
    def getSum(self):
        return self.cardSum
    
    #Determines if the user's sum is past 21
    def bust(self):
        return self.cardSum > 21
    
    #Clears the user's hand between rounds
    def clearHand(self):
        self.hand.clear()
        self.cardSum = 0

    #Awards the user with the current pool, used if the user wins a round
    def giveCurrPool(self, currPool):
        self.tokens[50] += currPool[50]
        self.tokens[100] += currPool[100]
        self.tokens[200] += currPool[200]
        self.tokens[500] += currPool[500]
        self.tokens[1000] += currPool[1000]
        self.totalPoints += (50 * currPool[50])
        self.totalPoints += (100 * currPool[100])
        self.totalPoints += (200 * currPool[200])
        self.totalPoints += (500 * currPool[500])
        self.totalPoints += (1000 * currPool[1000])