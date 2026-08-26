""" This module has a function to count the occurrences of each word in a sentence.

"""
import re


def count_words(sentence):
    """ Count the occurrences of each word in a sentence.
        Parameter
            sentence(str): This is the sentence that will be count the occurrences.
        Return
            total_words(dict): It's a dictionary with all the occurrences separate for each word.
    """
    sentence = sentence.lower()
    words = re.findall(r"[^\W_]+(?:'[^\W_]+)*", sentence)
    
    total_words = {}

    for word in words:
        total_words[word] = total_words.get(word, 0) + 1
            
    return total_words