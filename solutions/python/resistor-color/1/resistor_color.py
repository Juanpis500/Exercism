""" This module contains a pair of function to determine the code of a color on a color list.
"""

def color_code(color):
    """ Code  of the color
        Parameters:
            color(stirng): it's a color.
        Return: 
            number(int): the code based in the position of the color list.        
    """
    return colors().index(color)


def colors():
    """ List of colors

        Return:
            color_list(list): Its a list of color in order of the resistance bands.
    """
    color_list = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white']
    return color_list