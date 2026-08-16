"""
    This module contain a function to solve the exercise of raindrop.
"""


def convert(number):
    """ Convert number to a sounds

        Parameter:
            number(int): number to convert a sound

        Return: 
            text(string): result from the conversion 
    """
    sounds = ''
    
    if number % 3 == 0:
        sounds = sounds + 'Pling'
    if number % 5 == 0:
        sounds = sounds + 'Plang'
    if number % 7 == 0:
        sounds = sounds + 'Plong'
    if not number % 7 == 0 and not number % 5 == 0 and not number % 3 == 0:
        sounds = str(number)

    return sounds