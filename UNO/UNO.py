from collections import namedtuple
from random import choice, shuffle, seed, random

# Card colors
colors: list[str] = "Blue Green Red Yellow".split()

# Card face values and types
numbers: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
actions: list = ['Draw_2','Reverse', 'Skip']
wilds: list = ['Wild', 'Wild_Draw_4']

#Card collections
NumberCards: namedtuple = namedtuple('NumberCard', ['number', 'color'])
ActionCards: namedtuple = namedtuple('ActionCard', ['action', 'color'])
WildCards: namedtuple = namedtuple('Wildcard', ['action','color'])

# Collection (list) of all UNO cards above
UNOCards: list = []

# Curent player number#
playerturn: int = 0

# Game direction
gamedirection: str = 'Normal'

# Number of players
numPlayers: int = 4

# Current play action
currentaction: str = 'None'

# Number of cards for the next player to draw
numDrawCards: int = 0

# Play card color
playcolor: str = 'Any'

"""
Gameplay actions (Reverse, Skip, Next, Wild, Wild Draw 4)
First player number is 0, second is 1, third is 2 etc
"""
def getCurrentAction() -> str:
    return currentaction
"""
def getNextAction() -> str:
    return nextaction
"""

def getPlayColor() -> str:
    return playcolor

def getNumDrawCard() -> int:
    return numDrawCards

def getGameDirection() -> str:
    return gamedirection

def setCurrentAction(action: str='None') -> None:
    global currentaction
    currentaction = action

def setPlayColor(color: str) -> None:
    global playcolor
    playcolor = color

def setNumDrawCard() -> None:
    global numDrawCards
    if (getCurrentAction() == 'Draw_2'):
        numDrawCards += 2
    elif (getCurrentAction() == 'Wild_Draw_4'):
        numDrawCards = 4
    elif (getCurrentAction() == 'Draw_1'):
        numDrawCards = 1
    else:
        numDrawCards = 0

def playNewColor() -> None:
    print(f"Player{playerturn+1} to set color to play")
    for i in range(0, len(colors)):
        print(f"{i}: {colors[i]}")
    colortoplay = int(input("Enter color to play: "))
    setPlayColor(colors[colortoplay])
    print(f"Color to play: {getPlayColor()}")

# This function skips one player or determine the next player to move
def skip() -> None:
    global playerturn
    
    if gamedirection == 'Normal':
        playerturn += 1
        if playerturn >= numPlayers:
            playerturn = firstplayer()

    if gamedirection == 'Reverse':
        playerturn -= 1
        if playerturn < 0:
            playerturn = lastplayer()

# This reverses the game play direction and pause the game
# To resume play, call nextplayer()
def reverse() -> None:
    global gamedirection

    if gamedirection == 'Normal':
        gamedirection = 'Reverse'
    else:
        gamedirection = 'Normal'
    skip()

# This return the logical player turn i.e playerturn  + 1
def currentplayer() -> int:
    return playerturn + 1

def firstplayer() -> int:
    return 0

def lastplayer() -> int:
    return numPlayers - 1

"""
Gameplay functions:
Check discard pile and play deck for cards
Check for playable cards, how many playable cards, draw cards,
play a card and show cards hand
"""
def ispileempty(pile: list) -> bool:
    if len(pile) == 0:
        return True
    else:
        return False

def numCards(playerhand: list) -> int:
    return len(playerhand)

# Get discard/play card pile topmost card
# Discard pile is facing up. Hence, the last card appended is the top card
def getPileTopCard(pile: list, discard: bool = True) -> tuple:
    if not (ispileempty(pile)):
        if discard:
            return pile[-1]
        else:
            return pile[0]
    else:
        return None

# Check whether a card is playable against another
def cardplayable(playcard: tuple, matchcard: tuple) -> bool:
    if isinstance(matchcard, NumberCards):
        if (isinstance(playcard, NumberCards) and
                    (playcard.color == getPlayColor() or
                     playcard.number == matchcard.number)):
            return True
        elif (isinstance(playcard, ActionCards) and
                      (playcard.color == getPlayColor())):
            return True
        elif isinstance(playcard, WildCards):
            return True
    elif isinstance(matchcard, ActionCards):
        if (isinstance(playcard, ActionCards) and
                        playcard.action == matchcard.action):
            return True
        elif (isinstance(playcard, NumberCards) and
                        playcard.color == getPlayColor()):
            return True
    elif isinstance(matchcard, WildCards) and matchcard.action == 'Wild':
        if playcard.color == getPlayColor() or getPlayColor() == 'Any':
            return True
    else:
        # Card is not playable be default
        return False

# Check whether players have at least one playable card in their hands
def canplay(hand: list, topcard: tuple) -> bool:
    if ispileempty(hand):
        print("Player hand is empty")
        return False

    numPlayable = 0
    if len(hand) > 0:
        for i in range(0, len(hand)):
            if cardplayable(hand[i], topcard):
                numPlayable += 1
    # Player have at least one playable card
    if (numPlayable > 0):
        return True
    else:
        return False

def numPlayableCards(hand: list, topcard: tuple) -> int:
    if ispileempty(hand):
        print("Player hand is empty")
        return 0

    numPlayable = 0
    if len(hand) > 0:
        for i in range(0, len(hand)):
            if cardplayable(hand[i], topcard):
                numPlayable += 1
    # Player have at least one playable card
    return numPlayable
    
# Attempt to draw cards from deck
def drawcards(deck: list, hand: list, cardstodraw: int) -> bool:
    if ((len(deck) > 0) and (len(deck) >= cardstodraw)):
        for i in range(0, cardstodraw):
            hand.append(deck.pop(i))
        return True
    else:
        # Default is no card drawn
        return False

# Check whether card choosen is playable
def playcard(discardpile: list, hand: list, nextplayer: list,
                                 cardindex: int=-1) -> bool:
    if len(discardpile) > 0:
        if canplay(hand, discardpile[-1]):
            discardpile.append(hand.pop(cardindex))
            # Check the new card on top of the pile
            if isinstance(discardpile[-1], ActionCards):
                setCurrentAction(discardpile[-1].action)
                if (discardpile[-1].action == 'Draw_2'):
                    getNumDrawCard()
                elif discardpile[-1].action == 'Skip':
                    skip()
                elif discardpile[-1].action == 'Reverse':
                    reverse()
            elif (isinstance(discardpile[-1], WildCards)):
                setCurrentAction(discardpile[-1].action)
                if (discardpile[-1].action == 'Wild'):
                    playNewColor()
                elif (discardpile[-1].action == 'Wild_Draw_4'):
                    playNewColor()
                    setNumDrawCard()
            return True
    # Default is card is not playable
    return False

def showhand(hand: list) -> None:
    if ispileempty(hand):
        print("No card left")
    else:
        for i in range(0, len(hand)):
            if isinstance(hand[i], NumberCards):
                print(f"{i:2} {hand[i].color} {hand[i].number}")
            elif isinstance(hand[i], ActionCards):
                print(f"{i:2} {hand[i].color} {hand[i].action}")
            elif isinstance(hand[i], WildCards):
                print(f"{i:2} {hand[i].action}")

def main():
#Create all the cards with number face
    for number in numbers:
        for color in colors:
            UNOCards.append(NumberCards(number, color))
            if int(number) != 0:
                UNOCards.append(NumberCards(number, color))

    for action in actions:
        for color in colors:
            for i in range (0, 2):
                UNOCards.append(ActionCards(action, color))

    for wild in wilds:
        for i in range(0, 4):
            UNOCards.append(WildCards(wild, 'Any'))

    # Shuffle the deck
    seed()
    shuffle(UNOCards)

    # Create players and draw 7 card each
    player1 = []
    drawcards(UNOCards, player1, 7)

    player2 = []
    drawcards(UNOCards, player2, 7)

    player3 = []
    drawcards(UNOCards, player3, 7)

    player4 = []
    drawcards(UNOCards, player4, 7)


    # Create a discard pile
    discard = []
    discard.append(UNOCards.pop(0))

    # Redrawing card if the first card is a Wild_Draw_ 4
    if (isinstance(discard[-1], WildCards) and
                    discard[-1].action == 'Wild_Draw_4'):
        UNOCards.append(discard.pop(-1))

        for i in range(0, len(UNOCards)):
            if (isinstance(UNOCards[i], WildCards) and
                        UNOCards[i].action == 'Wild_Draw_4'):
                continue
            else:
                discard.append(UNOCards[i])
                break

    setPlayColor(discard[-1].color)
    
    if isinstance(discard[-1], ActionCards):
        setCurrentAction(discard[-1].action)
        if (getCurrentAction() == 'Reverse'):
            reverse()
        elif (getCurrentAction() == 'Skip'):
            skip()
        elif (getCurrentAction() == 'Draw_2'):
            setNumDrawCard()
            match (playerturn):
                case 0:
                    drawcards(UNOCards, player1, getNumDrawCard())
                case 1:
                    drawcards(UNOCards, player2, getNumDrawCard())
                case 2:
                    drawcards(UNOCards, player3, getNumDrawCard())
                case 3:
                    drawcards(UNOCards, player4, getNumDrawCard())
                    
    elif isinstance(discard[-1], WildCards):
        if discard[-1].action == 'Wild':
            playNewColor()
        elif discard[-1].action == 'Wild_Draw_4':
            playNewColor()
            setNumDrawCard()

    print("Player1 hand")
    showhand(player1)
    print("\nPlayer2 hand")
    showhand(player2)
    print("\nPlayer3 hand")
    showhand(player3)
    print("\nPlayer4 hand")
    showhand(player4)
    print("\nDiscard pile")
    showhand(discard)
    print(f"\nNumber of playable cards of Player1: ",
              numPlayableCards(player1, discard[-1]))
    print(f"Number of playable cards of Player2: ",
              numPlayableCards(player2, discard[-1]))
    print(f"Number of playable cards of Player3: ",
              numPlayableCards(player3, discard[-1]))
    print(f"Number of playable cards of Player4: ",
              numPlayableCards(player4, discard[-1]))
    print("\n=========================================")
    print("Game information:\n")
    print(f"Color to play: {getPlayColor()}")
    print(f"Game play direction: {getGameDirection()}")
    print(f"Game current action: {getCurrentAction()}")
    print(f"Current player #: {currentplayer()}")
    print(f"Number of cards to draw for current Player #",
              currentplayer(), ": ", getNumDrawCard())

if __name__ == "__main__":
    main()
