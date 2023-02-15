# This script will run a simple card game that asks the player to predict card values

# Reference:
    # Object-Oriented Python by Irv Kalb
    # Chapter 1

# Made with Mu v.1.0.3
    # December 2022

# Variables:
    # Global: SUIT_TUPLE, RANK_TUPLE, NUMBERCARDS, Score, StartingDeckList   
    # Local (for Loop): suit 
        # Local (nested for Loop): thisValue, cardDict, rank, suit, value
    # Local (while Loop): gameDeckList, currentCardDict, currentCardRank, currentCardValue, currentCardSuit
        # Local (nested for loop): cardNumber, answer, nextCardDict, nextCardRank, 
    # Local (functions): deckListIn, deckListOut
    
import random
    
SUIT_TUPLE = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
RANK_TUPLE = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
NUMBERCARDS = 8
Score = 50 

StartingDeckList = []

for suit in SUIT_TUPLE:
    """This for loop will """
    for thisValue, rank in enumerate(RANK_TUPLE):
        """This for loop will """
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue+1}
        StartingDeckList.append(cardDict)

def getCard(deckListIn):
    """This function will """
    thisCard = deckListIn.pop() # pop card of the top of the deck, aka pop last value off the stack
    return thisCard
   
def shuffle(deckListIn):
    """This function will """
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

while True:
    """This while loop will """
    print()
    gameDeckList = shuffle(StartingDeckList) # calls shuffle function
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + 'of' + currentCardSuit)
    print()
    
    for cardNumber in range(0,NUMBERCARDS):
    # This for loop will
        answer = input('Will the next card be higher or lower in value than ' + currentCardRank + 'of' + currentCardSuit + '? enter H or L ')
        answer = answer.casefold() # force input to lowercase
        nextCardDict = getCard(gameDeckList) # calls getCard function 
        nextCardRank = nextCardDict['rank']
        nextCardValue = nextCardDict['value']
        nextCardSuit = nextCardDict['suit']
        print('Next card is: ' + nextCardRank + 'of' + nextCardSuit)
            
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                Score = Score + 20
            else:
                print('Sorry, it was not higher')
                Score = Score - 15
                  
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                Score = Score + 20
                print('You got it right, it was lower')
            else:
                print('Sorry, it was not lower')
        print('Your score is:', Score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
            
    goAgain = input('To play again, press ENTER or "q" to quit: ')
    if goAgain == 'q':
        break
print('Ok, bye')
    
