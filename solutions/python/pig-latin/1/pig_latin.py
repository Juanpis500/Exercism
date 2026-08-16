"""
This module conteins the fuction for traslate Engils a Pig latin.
"""
import re

def translate(text):
    """ Engish to Pig Latin
    
        Paremeter:
            text(string): It's the text that will be translate to Pig latin. 
        Return:
            traslation(string): It's the text that already been translated.
    """
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    text = text.strip()
    words = text.split()
    text = ''
    for w in words:
        #Rule 3
        pattern_3 = r'^([^aeiouAEIOU]*qu)(.*)'
        
        match = re.match(pattern_3, w, re.IGNORECASE)
        if match:
            text = text + ' ' + match.group(2) + match.group(1) + 'ay'
            continue
            
        #Rule 4
        pattern_4 = r'^([^aeiouAEIOU]+)(y.*)'
        match = re.match(pattern_4, w, re.IGNORECASE)
        if match:
            text = text + ' ' + match.group(2) + match.group(1) + 'ay'
            continue
        
        #Rule 1
        if w.startswith(('xr', 'yt')) or w[0].lower() in vowels:
            w = w + 'ay'
            text = text + ' ' + w
            continue
            
        #Rule 2
        pattern_2 = r'^([^aeiouAEIOU]+)(.*)'
        
        match = re.match(pattern_2, w, re.IGNORECASE)
        if match:
            text = text + ' ' + match.group(2) + match.group(1) + 'ay'
            continue

    return text.strip()