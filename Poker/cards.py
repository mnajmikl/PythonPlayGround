"""
cards.py

@author: Mohammad Najmi
@version 0.0.1
"""

# Suits and faces of a deck of cards
suitchars: list = "♠ ♣ ♥ ♦".split()
suitnames: list = "Clubs Spades Hearts Diamonds".split()
facechars: list = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

# Card values
cardsvalues: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Card outlines
horizline13: str = "─"*13
horizline11: str = "─"*11
vertline: str = "│"
topright: str = "┌"
topleft: str = "┐"
bottomleft: str = "└"
bottomright: str = "┘"
sideborders = f"{vertline:14}{vertline}"
blankborders = f"{vertline}{vertline}ӀѺѺѺѺѺѺѺѺѺӀ{vertline}{vertline}"
cardtop: str = f"{topright}{horizline13}{topleft}"
cardtop2: str = f"{vertline}{topright}{horizline11}{topleft}{vertline}"
cardbottom: str = f"{bottomleft}{horizline13}{bottomright}"
cardbottom2: str = f"{vertline}{bottomleft}{horizline11}{bottomright}{vertline}"

def printhands(cards: list, start: int = 0, col: int = 5):
    """
    Print the hands/cards that a player have
    printhands(cards: list, start: int = 0, col: int = 5)
    
   Parameters:
        cards: the list containing cards
        start: the start index of the cards to be shown
        col: number of cards to be shown per column
    """
    for p in range(start, len(cards), col):
        topface = ""
        topsuit = ""
        lowface = ""
        lowsuit = ""
        centersuit = ""
        # Check the number of printable cards at max{col}
        n = len(cards[p:p+col])
        print(cardtop*n)
        for x in cards[p:p+col]:
            # Find the matching suit character
            for idx, val in enumerate(suitnames):
                if x[1] == val:
                    topface += f"{vertline}{x[0]:<2}{vertline:>12}"
                    topsuit += f"{vertline}{suitchars[idx]:<2}{vertline:>12}"
                    lowface += f"{vertline:12}{x[0]:>2}{vertline}"
                    lowsuit += f"{vertline:12}{suitchars[idx]:>2}{vertline}"
                    centersuit += f"{vertline}{suitchars[idx].center(13)}{vertline}"
        print(topface)
        print(topsuit)
        for _ in range(0, 2):
            print(sideborders*n)
        print(centersuit)
        for _ in range(0, 2):
            print(sideborders*n)
        print(lowsuit)
        print(lowface)
        print(cardbottom*n)

def printsinglecard(card: tuple):
    """
    Print the a single card
    printsinglecard(card: tuple)
    
    Parameters
    ----------
        card: tuple
            Cards
    """
    if not isinstance(card, tuple):
        return
    topface = ""
    topsuit = ""
    lowface = ""
    lowsuit = ""
    centersuit = ""
    for idx, val in enumerate(suitnames):
        if card[1] == val:
            topface += f"{vertline}{card[0]:<2}{vertline:>12}"
            topsuit += f"{vertline}{suitchars[idx]:<2}{vertline:>12}"
            lowface += f"{vertline:12}{card[0]:>2}{vertline}"
            lowsuit += f"{vertline:12}{suitchars[idx]:>2}{vertline}"
            centersuit += f"{vertline}{suitchars[idx].center(13)}{vertline}"
    print(cardtop)
    print(topface)
    print(topsuit)
    for _ in range(2):
        print(sideborders)
    print(centersuit)
    for _ in range(2):
        print(sideborders)
    print(lowsuit)
    print(lowface)
    print(cardbottom)

def printholecard(number_of_card: int = 1):
    """
    Print a hole card (face down card)
    
    Parameter
    ----------
        number_of_card: int
            Number of hole cards
    """
    print(cardtop*number_of_card)
    print(cardtop2*number_of_card)
    for _ in range(6):
        print(blankborders*number_of_card)
    print(cardbottom2*number_of_card)
    print(cardbottom*number_of_card)