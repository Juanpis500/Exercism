"""
    This module integrates a function to cipher a text.
"""

def rotate(text, key):
    """Rotational cipher fuction
        Parameters:
            text(string): text to cipher.
            key(int): the rotation of the plain.
        Return:
            text_output(string): text already cipher.
    """
    text_output = ''
    
    plain = 'abcdefghijklmnopqrstuvwxyz'
    if key == 0 : 
        cipher = 'abcdefghijklmnopqrstuvwxyz'
    else: 
        cipher = plain[-key:] + plain[:len(plain) - key]
    
    for letter in text:
        if not letter.isalpha():
            text_output += letter
            continue
        if letter.isupper():
            letter = letter.lower()
            text_output += plain[cipher.find(letter)].upper()
            continue
        
        text_output += plain[cipher.find(letter)] 

    return text_output