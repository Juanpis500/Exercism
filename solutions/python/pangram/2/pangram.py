"""
    This module contains the code for review if a serntence its a pangram.
"""

import string 

def is_pangram(sentence):
    """ Verify if the sentences it's a pangram.

        Parameter:
            sentence(string): this is the sentence that will be review.

        Return: 
            bool: True if its a pangram or False if not.
    """
    abc = string.ascii_lowercase
    sentence = sentence.lower()
    
    for letter in abc:
        if not letter in sentence:
            return False
            
    return True