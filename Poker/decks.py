"""
decks.py

@author: Mohammad Najmi
@version 0.0.1
"""
from random import random, shuffle, seed
from cards import cardsvalues, suitnames, facechars

def createdeck() -> list:
    """
    Cards in deck are stored in the following format:
        [(face, suit, value),     -> 1st card
         (face, suit, value),  -> 2nd card
        ... ]             -> nth card
    """
    deck = [(facechars[i], s, cardsvalues[i]) for s in suitnames
                for i in range(len(cardsvalues))]
    return deck

def createplaydeck(deck: list, numdecks: int = 1) -> None:
    for _ in range(numdecks):
        deck.extend(createdeck())

def shuffledeck(deck: list, numshuffle: int = 10) -> None:
    for _ in range(numshuffle):
        seed(random())
        shuffle(deck)

def clearcards(discardpile: list, playerscards: list) -> None:
    for _ in range(len(playerscards)):
        discardpile.append(playerscards.pop())

def recyclecards(deck: list, discardpile: list) -> None:
    shuffledeck(discardpile)
    for _ in range(len(discardpile)):
        deck.append(discardpile.pop())