from Deck import deck
from Player import player

def Game():
    done = False
    cardDeck = deck('cards.txt')
    cardDeck.shuffleCards()
    
    playerOne = player('Jorge')
    cardDeck.dealCard(playerOne)
    cardDeck.dealCard(playerOne)
    cardDeck.dealCard(playerOne)
    playerOne.printHand()
    print(f'Current Sum: {playerOne.getSum()}')


def main():
    Game()
    

if __name__ == '__main__':
    main()