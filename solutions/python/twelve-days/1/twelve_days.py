""" This module contains a function to create the lyric of The Twelve Days of Christmas.

"""

def create_verse (number_verse):
    """    Creates a verse of the song "The Twelve Days of Christmas" based on the given number_verse.
        Parameter:
            number_verse(int): The number of verse.
        Return:
            verse(string): The verse in string format.
    """
    gifts = [
        ('first', 'a Partridge in a Pear Tree',),
        ('second', 'two Turtle Doves'),
        ('third', 'three French Hens'),
        ('fourth', 'four Calling Birds'),
        ('fifth','five Gold Rings'),
        ('sixth', 'six Geese-a-Laying'),
        ('seventh', 'seven Swans-a-Swimming'),
        ('eighth', 'eight Maids-a-Milking'),
        ('ninth', 'nine Ladies Dancing'),
        ('tenth', 'ten Lords-a-Leaping'),
        ('eleventh', 'eleven Pipers Piping'),
        ('twelfth', 'twelve Drummers Drumming')
    ]
    verse = 'On the ' + gifts[number_verse -1][0] +' day of Christmas my true love gave to me: '
    if number_verse == 1:
        verse += gifts[number_verse - 1][1] + '.'
        return verse
    
    for index in range(number_verse, 0, -1):
        if index - 1 == 0:
            verse += 'and ' + gifts[index - 1][1] + '.'
        else:
            verse += gifts[index - 1][1] + ', '
    return verse

def recite(start_verse, end_verse):
    """Recites the verses of the song "The Twelve Days of Christmas" from start_verse to end_verse.
        Parameters:
            start_verse(int): represents the firts verse
            end_verse(int): represents the last verse
        Return:
            result(list): Returns the verse of the song separate in a list.
    """
    result = []
    for index in range(start_verse, end_verse + 1):
        result.append(create_verse(index))
    
    return result