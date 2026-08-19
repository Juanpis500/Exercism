""" This module contains a function to count the number of 1 bits in the binary representation of a number.
    
"""

def egg_count(display_value):
    """ This function converts a number in to a binary, then count the number 1.

        Parameter:
            display_value(int): the number base.
        Return: 
            total_ eggs(int): total of 1 bits.
    """
    total_eggs = 0
    result = ''
    
    if display_value == 0:
        return 0
        
    #Transform the number to binary
    number = display_value 
    while number > 0:
        res = number % 2
        result = str(res) + result
        number = number // 2
    
    #Then, count all the digit 1 in the number base 2
    for digit in result:
        if digit == '1':
            total_eggs += 1

    return total_eggs