"""
    This module contains the functions to apply the Atbash Cipher.
"""
import re

Plain = 'abcdefghijklmnopqrstuvwxyz'
Cipher = 'zyxwvutsrqponmlkjihgfedcba'

def encode(plain_text):
    """ Encode fuction
    
    """
    plain_text = plain_text.lower()
    plain_text = re.sub(r'[^a-zA-Z0-9]', '', plain_text)
    cipher_text = ''
    pos = 1
    for letter in plain_text:
        if not letter in Plain:
            cipher_text += letter
        else:
            cipher_text += Cipher[Plain.find(letter)]
        pos += 1
        if pos == 6:
            pos = 1
            cipher_text += ' '
    cipher_text = cipher_text.strip()
    return cipher_text

def decode(ciphered_text):
    """ Decode function
    
    """
    ciphered_text = ciphered_text.replace(' ','')
    text_clean = ''
    for letter in ciphered_text:
        if not letter in Plain:
            text_clean += letter
        else:
            text_clean += Plain[Cipher.find(letter)]
    return text_clean