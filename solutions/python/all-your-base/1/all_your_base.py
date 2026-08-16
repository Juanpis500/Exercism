"""
    This module contains a function to convert any number to a other base.
"""

def rebase(input_base, digits, output_base):
    """ Converter the number of input_base to a number in output_base.
        
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if any(number < 0 or number >= input_base for number in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    output_digit = []
    number_base_10 = 0

    #convert any number to base 10
    for number in digits:
        number_base_10 = number_base_10 * input_base + number

    if number_base_10 == 0:
        return [0]
        
    #Convert the number in base 10 to the number in output_base
    while number_base_10 > 0:
        output_digit.append(number_base_10 % output_base)
        number_base_10 = number_base_10 // output_base

    output_digit.reverse()

    return output_digit