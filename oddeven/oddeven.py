"""
NAME
    oddeven

DESCRIPTION
    Return the count and lists of odd and even numbers

    :copyright: (c) 2022 Mohammad Najmi Bachok
    :license: MIT license

FUNCTIONS
    oddnumbers  - returns count of odd numbers
    evennumbers - returns count of even numbers
    oddeven     - returns lists of odd and even numbers

VERSION
    0.0.1

AUTHOR
    Mohammad Najmi Bachok

FILE
    oddeven.py
"""

def oddnumbers(start: int, end: int, /) -> int:
    """
    Returns the count of odd numbers in range of start to end
    Parameters:
    start (int): The start of the range
    end   (int): The end of the range
    """
    return len(range((start if start%2==1 else start+1), end+1, 2))

def evennumbers(start: int, end: int, /) -> int:
    """
    Returns the count of even numbers in range of start to end
    Parameters:
    start (int): The start of the range
    end   (int): The end of the range
    """
    return len(range((start if start%2==0 else start+1), end+1, 2))

def oddevens(start: int, end: int, /) -> tuple:
    """
    Returns a tuple of lists of odd and even numbers
    Parameters:
    start (int): The start of the range
    end   (int): The end of the range
    """
    number_range = list(range(start, end+1))
    number_dict = {"Odds": list(filter(lambda x: x%2 ==1, number_range)),
                   "Evens": list(filter(lambda x: x%2 ==0, number_range))}
    return (number_dict["Odds"], number_dict["Evens"])

def odds(start: int, end: int, /) -> list:
    """
    Returns a list of odd numbers
    Parameters:
    start (int): The start of the range
    end   (int): The end of the range
    """
    return list(range((start if start%2==1 else start+1), end+1, 2))

def evens(start: int, end: int, /) -> list:
    """
    Returns a list of even numbers
    Parameters:
    start (int): The start of the range
    end   (int): The end of the range
    """
    return list(range((start if start%2==0 else start+1), end+1, 2))
