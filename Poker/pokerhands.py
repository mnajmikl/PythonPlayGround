"""
Module pokerhands
Poker hand rank evaluation

@author: Mohammad Najmi
@version 0.0.1
"""

from cards import cardsvalues, suitnames, facechars

def hasflush(hand: list):
    """
    Check for player hand for flush (all cards are in the same suit)
    Returns True if hasstraightflush(hand) or hasroyalflush(hand) is True

    Parameters:
    hand (list): The poker cards

    Returns:
    bool: True if hand is a Flush
    """
    if len(hand) == 5:
        cardfaces = []
        checksuit = hand[0][1]
        for card in hand:
            cardfaces.append(suitnames[suitnames.index(card[1])])
        cardfaces.sort()
        return cardfaces.count(checksuit) == 5
    return False

def hasstraight(hand: list):
    """
    Check for player hand for straight
        e.g. {3, 4, 5, 6, 7} or {9, 10, J, Q, K}
    Returns True if hasstraightflush(hand) or hasroyalflush(hand) is True

    Parameters:
    hand (list): The poker cards

    Returns:
    bool: True if hand is a Straight
    """
    if len(hand) == 5:
        cardincrementone = 0
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        cardval.sort()
        has_ace = False
        if cardval[0] == 1:
            has_ace = True
        checkstart = 0
        checkend = len(cardval) - 1
        if has_ace:
            checkstart = 1
            if cardval[1] != 2 and cardval[1] != 10:
                return False
        for i in range(checkstart, checkend):
            if cardval[i] == cardval[i+1] - 1:
                cardincrementone += 1
        if (has_ace and cardincrementone == 3) or cardincrementone == 4:
            return True
    return False

def hasstraightflush(hand: list):
    """
    Check if hand for straight flush
    Returns True if hasroyalflush(hand) is True

    Parameters:
    hand (list): The poker cards

    Returns:
    bool: True if hand is a Straight Flush
    """
    return hasflush(hand) and hasstraight(hand)

def hasroyalflush(hand: list):
    """
    Check if hand has royal flush
    Royal Flush is a straight flush that consists of A, 10, J, Q, K

    Parameters:
    hand (list): The poker cards

    Returns:
    bool: True if hand is a Royal Flush
    """
    if len(hand) == 5:
        isroyal = False
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        cardval.sort()
        # Royal if hand conists of A, 10, J, Q, K (1, 10, 11, 12, 13)
        if (cardval[0] == 1 and cardval[1] == 10 and cardval[2] == 11
                and cardval[3] == 12 and cardval[4] == 13):
            isroyal = True

    return hasstraightflush(hand) and isroyal

def hasfourofakind(hand: list):
    """
    Check for player hand for four of a kind

    Parameters:
    hand (list): The poker cards

    Returns:
    bool: True if hand is a Four Of A Kind
    """
    if len(hand) == 5:
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        if cardval.count(cardval[0]) == 4 or cardval.count(cardval[1]) == 4:
            return True
    return False

def hasthreeofakind(hand: list):
    """
    Check for player hand for three of a kind

    Parameters:
    hand (list): The poker cards

    Returns:
    bool: True if hand is a Three Of A Kind
    """
    if len(hand) == 5:
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        cardval.sort()
        if (cardval.count(cardval[0]) == 3 or cardval.count(cardval[1]) == 3
                or cardval.count(cardval[2]) == 3):
            return True
    return False

def hasonepair(hand: list):
    """
    Check for player hand for a pair

    Parameters:
    hand (list): The poker cards

    Returns:
    bool: True if hand is a Pair
    """
    if len(hand) == 5:
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        cardval.sort()
        if (cardval.count(cardval[0]) == 2 or cardval.count(cardval[1]) == 2
                or cardval.count(cardval[2]) == 2 or
                    cardval.count(cardval[3]) == 2):
            return True
    return False

def hastwopairs(hand: list):
    """
    Check for player hand for two pairs

    Parameters:
    hand (list): The poker cards

    Returns:
    bool: True if hand is a Two Pair
    """
    if len(hand) == 5:
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
    cardval.sort()
    if ((cardval.count(cardval[0]) == 2 and
            (cardval.count(cardval[2]) == 2 or cardval.count(cardval[3]) == 2))
            or (cardval.count(cardval[1]) == 2 and cardval.count(cardval[3]) == 2)):
        return True
    return False

def hasfullhouse(hand: list):
    """
    Check for player hand for full house (one pair and three of a kind)

    Parameters:
    hand (list): The poker cards

    Returns:
    bool: True if hand is a Full House
    """
    return hasonepair(hand) and hasthreeofakind(hand)

def handscore(hand: list):
    """
    Count the hand score
    Return a tuple of hand score and type of poker hand

    Parameters:
    hand (list): The poker cards

    Returns:
    tuple(int, str): tuple of score and poker rank
    """
    handvalue = 0
    if len(hand) == 5:
        for card in hand:
            val = facechars.index(card[0])
            handvalue += cardsvalues[val]
            # If the card value is 1 (Ace), add another 13
            if cardsvalues[val] == 1:
                handvalue += 13

    if hasroyalflush(hand):
        return handvalue + 5000, "Royal Flush"
    if hasstraightflush(hand):
        return handvalue + 4000, "Straight Flush"
    if hasfourofakind(hand):
        return handvalue + 3000, "Four Of A Kind"
    if hasfullhouse(hand):
        return handvalue + 2000, "Full House"
    if hasflush(hand):
        return handvalue + 1000, "Flush"
    if hasstraight(hand):
        return handvalue + 750, "Straight"
    if hasthreeofakind(hand):
        return handvalue + 500, "Three Of A Kind"
    if hastwopairs(hand):
        return handvalue + 250, "Two Pair"
    if hasonepair(hand):
        return handvalue + 100, "Pair"
    return handvalue, "High Card"