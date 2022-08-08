"""
pokergame.py

@author: Mohammad Najmi
@version 0.0.1
"""
from pokerhands import handscore

cards = [('10', 'Hearts'), ('A', 'Diamonds'), ('K', 'Spades'),
             ('Q', 'Diamonds'), ('J', 'Clubs')]

def main():
    """
    Main program function

    Parameters
    -----------
    None.

    Returns
    -------
    None.
    """
    score, rank = handscore(cards)
    print(f"Hand value is {score}")
    print(f"Hand rank is {rank}")

if __name__ == "__main__":
    main()
