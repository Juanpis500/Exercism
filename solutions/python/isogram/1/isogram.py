"""
    This module contains a function that analyse a word to determine if it's a isogram.
"""
import re

def is_isogram(phrase):  
    return not re.search(r"([a-zA-Z]).*\1", phrase, flags=re.IGNORECASE)