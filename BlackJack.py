from Deck import deck
from Player import player
from House import house
import os

#TODO: 
##Fix error where House never hits
##Add draw situation and implement so that player doesn't win/lose points
##In Bet() need to account for when user has no more tokens to bet, current situation gets user stuck in an infinite loop 

#Clears the terminal for test purposes
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Adds Double of the User's bet to the current Pool
def updateCurrentPool(currPool, bet):
    currPool[bet] += 2

#Determine if the player is the winner of the game
def playerWins(House, Player, Deck):
    #Determines whether the house 'hits' or 'stands' 
    #and draws cards while the house 'hits' and does not pass 21
    while House.hit() and not House.bust():             ###########FIXME: Possible error, House never hits
        Deck.dealCard(House)

    #Checks win conditions and determines if the player wins the game
    if(House.bust()):
        return True
    elif Player.getSum() > House.getSum():
        return True
    else:
        return False
    
#Outputs the current status of the game
def printCurrGameStatus(House, Player):
    #Shows the dealer's upcard
    print('Delear\'s Up Card:')
    House.showUpCard()

    #Shows the player's current hand
    print('\nYour current Hand: ')
    Player.printHand()
    print(f'\nCurrent sum of your hand: {Player.getSum()}')

#Allows the user to choose between hit/stand/quit and returns the selected choice
#Main purpose of this function is to ensure proper user input
def hitOrStand():
    print('Would you like to \'Hit\', \'Stand\' or quit? (h/s/q):')
    inp = str(input())
    while inp != "h" and inp != "s" and inp != "q":
        print('Please enter a valid input (h/s/q):')
        inp = str(input())
    return inp

#Allows player to place a bet at the beginning of each round
def Bet(player, currPool):
    clear_console()
    print(f'Current points: {player.getPlayerPoints()}')
    bet = 0
    done = False

    #Loop allows user to bet multiple tokens in one round
    while not done:
        clear_console()
        print(f'Current Bet: {bet} points')
        print('These are your current Tokens: ')
        player.printTokens()
        print('Choose tokens to place (1-5): ')
        inp = int(input())

        #Checks for proper user input
        while not(inp >= 0 and inp <= 5) or not player.canPlaceToken(inp):
            print('Please enter valid input (1-5): ')
            inp = int(input())

        #Uses the user's choice to place the bet and updates the pool of points to win/lose
        if inp == 1:
            bet += 50
            player.placeBet(50)
            updateCurrentPool(currPool,50)
        elif inp == 2:
            bet += 100
            player.placeBet(100)
            updateCurrentPool(currPool,100)
        elif inp == 3:
            bet += 200
            player.placeBet(200)
            updateCurrentPool(currPool,200)
        elif inp == 4:
            bet += 500
            player.placeBet(500)
            updateCurrentPool(currPool,500)
        elif inp == 5:
            bet += 1000
            player.placeBet(1000)
            updateCurrentPool(currPool,1000)

        #Shows the status of points and the current bet placed
        print(f'Current points: {player.getPlayerPoints()}')
        print(f'Current Bet: {bet} points')

        #Asks the user if they wish to up their bet
        print('Are you done betting? (y/n):')
        option = str(input())
        
        #Ensures proper user input
        while(option != "y" and option != "n"):
            print('Please enter a valid option (y/n):')
            option = str(input())

        #Ends loop if user is done betting
        if(option == "y"):
            done = True

        


def Game():
    done = False
    name = str(input("What is your name: "))
    playerOne = player(name)
    clear_console()

    #Loop for Game Round, keeps running while player doesn't choose to quit
    #and while player still has points to bet
    while not done and playerOne.getPlayerPoints() > 0:
        
        #Clears the player's hand between rounds
        playerOne.clearHand()

        #Keeps the current pool, which keeps the points to win/lose
        currPool = {50 : 0, 100 : 0, 200 : 0, 500 : 0, 1000 : 0}
        House = house()

        #Initiates game deck and reshuffles at the start of each round, also deals
        #initial cards to player and house
        gameDeck = deck('cards.txt')
        gameDeck.shuffleCards()
        gameDeck.dealCard(playerOne)
        gameDeck.dealCard(playerOne)
        gameDeck.dealCard(House)
        gameDeck.dealCard(House)
        
        #Allows the player to bet before seeing the cards dealt
        Bet(playerOne, currPool)
        clear_console()

        #Once bet has been placed game starts and hand is shown to player
        printCurrGameStatus(House, playerOne)

        #Allow player to keep drawing cards from stack while sum doesn't pass 21
        while not playerOne.bust():

            #Asks the user whether to hit, stand, or quit game
            hitOption = hitOrStand()
            clear_console()

            #If 'hit' player is dealt a card
            if hitOption == "h" and not playerOne.bust():
                gameDeck.dealCard(playerOne)
                printCurrGameStatus(House, playerOne)

            #Allows player to stand or quit
            if playerOne.bust() or hitOption == "s":
                break
            elif hitOption == "q":
                done = True
                break

        clear_console()

        #if user selected 'quit', ends the current game
        if done:
            break     

        #Once there are no more decisions to be made, house's hand is revealed to player
        print('House\'s hand: ')
        House.printHand()
        print(f'House\'s total Sum: {House.getSum()}')
        print('\nYour hand: ')
        playerOne.printHand()
        print(f'Your total sum: {playerOne.getSum()}')

        #Gives player the current pool if the player wins
        if playerWins(House, playerOne, gameDeck) and not playerOne.bust():
            playerOne.giveCurrPool(currPool)
            print('\nYou Win!!')
        else:
            print('\nYou Lose')

        #If user has no more points to bet, the game is ended
        if playerOne.getPlayerPoints() == 0:
            continue

        #Displays the user's current points and asks the user
        #if they wish to move onto the next round
        print(f'\nCurrent Points: {playerOne.getPlayerPoints()}')
        print('\nWould you like to continue? (y/n)')
        cont = str(input())

        while(cont != "y" and cont != "n"):
            print('Please enter valid input (y/n):')
            cont = str(input())

        clear_console()

        if(cont == "n"):
            done = True
        else: 
            done = False
    
    #Gives the user their final score if the game is ended
    clear_console()
    print(f'Final Score: {playerOne.getPlayerPoints()}')



def main():
    print('Welcome! Do you want to play Blackjack?(y/n)')
    choice = str(input())

    #Ensure valid input from user
    while(choice != "y" and choice != "n"):
        print('Please enter a valid choice (y/n):')
        choice = str(input())
    
    #Call the main game loop and allow user to start new games
    while choice == "y":
        Game()
        print('Would you like to play a new game (y/n):')
        choice = str(input())
        while(choice != "y" and choice != "n"):
            print('Please enter a valid choice (y/n):')
            choice = str(input())
    
    print('Thanks for playing')
    
    

if __name__ == '__main__':
    main()