class card:
    #Value holds the number associated with the card, not necessarily how much each card is worth
    #Example: King is associated with '13' and is worth '10'; Value acts as an identifier
    #Type holds the card's type such as : clubs, spades, diamonds, and hearts
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    #Returns the cards identifier
    def getValue(self):
        return self.value

    #Returns the cards type
    def getType(self):
        return self.type

    #Prints the card using the identifier to determine what card it is and the type
    def printCard(self):
        if self.value == 1: 
            print(f'\tA {self.type}')
        elif self.value == 11:
            print(f'\tJ {self.type}')
        elif self.value == 12:
            print(f'\tQ {self.type}')
        elif self.value == 13:
            print(f'\tK {self.type}')
        else:
            print(f'\t{self.value} {self.type}')

