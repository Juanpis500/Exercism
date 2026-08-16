"""
    This module contains the code for cheking if a strign its a ISBN valid.
"""
import re


def is_valid(isbn):
    """ ISBN verifier
        
    """
    total = 0
    pos = 10
    isbn = isbn.replace("-", "")

    if not re.search (r"^\d{9}[\dX]$", isbn, flags=re.IGNORECASE):
        return False
    
    if not len(isbn) == 10:
        return False
    
    for number in isbn:
        if number == 'X':
            total = total + (10 * pos)
        else:
            total = total + (int(number) * pos)
        pos -= 1
        
    return total % 11 == 0