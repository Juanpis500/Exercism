""" 
    This module contains a functions that return a code of a resistance band.
"""

def color_position(color):
    """ Stores a list of colors.
    
        Parameter:
            color(string): this is a color.
        Return:
            position(int): return the position of the color into the list.
    """
    colors=[
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]
    return colors.index(color)

    
def value(colors):
    """ Returns the code color that is required.

        Parameters:
            colors(list): It's a list of colors.
        Return: 
            color_code(int): code of a resistance band.
    """
    color_code = ''
    for index in range(2):
        color_code += str(color_position(colors[index]))
        
    return int(color_code)