"""
    This module contains a function to convert arabic numerals to roman.
"""

def roman(number):
    """ Takes an arabic numeral and transforms to roman numeral.
        Parameters:
            number(int): arabic numeral. 
        Return:
            roman_str(string): roman numeral.
    """
    units = [
        ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
        ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
        ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
        ("", "M", "MM", "MMM")
    ]
    roman_str = ""
    for index, digit in enumerate(str(number)[::-1]):
        roman_str = units[index][int(digit)] + roman_str
    
    return roman_str