"""
    This module contains a function for calculate a armstrong number.
"""

def is_armstrong_number(number):
    """
        Input
            number: The number that will be analize
        
        Return
            True or False: Only if its a amstrong number
            
        This function calculates if one number is an armstrong number.
    """
    txt = str(number)
    total = 0
    for num in txt:
        total += int(num) ** len(txt)

    if total == number: 
        return True 
    
    return False
