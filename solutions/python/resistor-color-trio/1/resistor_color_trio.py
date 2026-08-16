""" This module contains a pair of functions that calculates the value of a resistance band.
    
"""

def get_value(colors):
    """ Calculate the value of the resistance.
    
        Parameter:
            colors(list): It's a list of color to calculate the resistance value.
        Return:
            value(string): Return the value of the resistance after been calculated.
    """
    colors_field=[
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
    value = str(colors_field.index(colors[0])) + str(colors_field.index(colors[1])) + '0'*colors_field.index(colors[2])
    return value


def label(colors):
    """ Design the field of the value of the resistance with ohm metrix.

        Parameters:
            colors(list): It's a list of colors.
        Return: 
            resistance_value(int): It's the final result.
    """
    metric_prefix=[
        "ohms",
        "kiloohms",
        "megaohms",
        "gigaohms"
    ]
    value = get_value(colors)
    fragment = [value[max(i - 3, 0):i] for i in range(len(value), 0, -3)][::-1]
    
    resistance_value = fragment[0] + ' ' + metric_prefix[len(fragment) - 1]

    if(resistance_value[0] == '0'):
        resistance_value = resistance_value[1:]
    
    return  resistance_value
