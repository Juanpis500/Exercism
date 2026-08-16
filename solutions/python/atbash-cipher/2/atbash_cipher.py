"""
    This module contains the functions to apply the Atbash Cipher.
"""
import re

PLAIN = 'abcdefghijklmnopqrstuvwxyz'
CIPHER = 'zyxwvutsrqponmlkjihgfedcba'

def encode(plain_text):
    """ Encode fuction

        Parameters:
            plain_text(string): The text that will be cipher.
        Return:
            cipher_text(string): The text after been cipher. 
    """
    plain_text = plain_text.lower()
    plain_text = re.sub(r'[^a-zA-Z0-9]', '', plain_text)
    cipher_text = ''
    pos = 0
    for letter in plain_text:
        if not letter in PLAIN:
            cipher_text += letter
        else:
            cipher_text += CIPHER[PLAIN.find(letter)]
        pos += 1
        if pos == 5:
            pos = 0
            cipher_text += ' '
    cipher_text = cipher_text.strip()
    return cipher_text

def decode(ciphered_text):
    """ Decode function
        
        Parameters:
            ciphered_text(string): The code that will be decode.
        Return:
            text_clean(string): The text after been decoded. 
    """
    ciphered_text = ciphered_text.replace(' ','')
    text_clean = ''
    for letter in ciphered_text:
        if not letter in PLAIN:
            text_clean += letter
        else:
            text_clean += PLAIN[CIPHER.find(letter)]
    return text_clean