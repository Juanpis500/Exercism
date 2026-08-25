""" This module include a pair of functions to generate a song.

"""


def create_verse(number_verse):
    """ In this method build a single verse.
        Parameters:
            number_verse(int): The posicion of the verse.
        Return:
            verse(string): The verse that was built in the function.
    """
    numeral=[
        "no",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten"
    ]
    verse = []
    bottle_str = "bottles" if number_verse > 1 else "bottle"
    verse.extend([numeral[number_verse].capitalize() + " green " + bottle_str + " hanging on the wall,"] * 2)
    verse.append("And if one green bottle should accidentally fall,")
    bottle_str = "bottle" if number_verse - 1 == 1 else "bottles"
    verse.append("There'll be "+ numeral[number_verse - 1] +" green " + bottle_str + " hanging on the wall.")
    return verse
    

def recite(start, take=1):
    """ Build the song
        Parameters
            star(int): The initial verse.
            take(int)(default = 1): the total of verse.
        Return    
            song(list): The song separate in a list.
    """
    song = []
    for number_verse in range(start, start - take, -1):
        song.extend(create_verse(number_verse))
        if number_verse != (start - take + 1):
            song.extend([""])
    return song