""" This module splits the input data into a output different format.

"""

def transform(legacy_data):
    """ Split the legacy data into a original data. (This means, separate each letter individual letter with its score in a one-to-            one)
        Parameter
            legacy_data(dict): the legacy data -> ({1: ["A", "E", "I", "O", "U"]})
        Return
            original_data(dict): the original data -> ({"a": 1, "e": 1, "i": 1, "o": 1, "u": 1})
    """
    original_data = {}
    for key, value in legacy_data.items():
        for letter in value:
            original_data[letter.lower()] = key
    
    return original_data