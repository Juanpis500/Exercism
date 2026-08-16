"""
    This module include a function to determine if a list of words can be anagram from a especific word.
"""

def find_anagrams(word, candidates):
    """ Review every word to determine if it's a possible anagram and exclude others.
        Parameters:
            word (string): It;s the word that we compare.
            candidates(list): List of posible anagrams.
        Return:
            anagrams(list): Includes the list of anagrams.  
    """
    temp =[]
    anagrams = []
    for candi in candidates:
        temp = list(word.lower())
        temp_word = candi.lower()
        if candi.lower() == word.lower():
            continue
        if len(word) == len(candi):
            band = True
            for char in temp:
                if not char in temp_word or word.lower().count(char) != temp_word.count(char):
                    band = False
                    break
            if band:
                anagrams.append(candi)

    return anagrams
