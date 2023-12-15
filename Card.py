class card:
    
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def getValue(self):
        return self.value

    def getType(self):
        return self.type

    def setValue(self, val):
        self.value = val 

    def setType(self, type):
        self.type = type

    def printCard(self):
        if self.value == 1: 
            print(f'A {self.type}')
        elif self.value == 11:
            print(f'J {self.type}')
        elif self.value == 12:
            print(f'Q {self.type}')
        elif self.value == 13:
            print(f'K {self.type}')
        else:
            print(f'{self.value} {self.type}')

