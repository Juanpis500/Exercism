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
    match len(colors):
        case 5:
            value = str(colors_field.index(colors[0])) + str(colors_field.index(colors[1])) + str(colors_field.index(colors[2]))                 +'0'*colors_field.index(colors[3])
        case 4:
            value = str(colors_field.index(colors[0])) + str(colors_field.index(colors[1])) + '0'*colors_field.index(colors[2])
        case 2:
            value = str(colors_field.index(colors[0])) + str(colors_field.index(colors[1]))
        case 1:
            value = str(colors_field.index(colors[0]))
    
    return value

def resistor_label(colors):
    """ Design the field of the value of the resistance with ohm metrix and tolerance.

        Parameters:
            colors(list): It's a list of colors with the resistances band.
        Return: 
            resistance_value(int): It's the final result.
    """
    metric_prefix = [
        'ohms',
        'kiloohms',
        'megaohms',
        'gigaohms']

    tolerance_band = {
        'grey':'0.05',
        'violet':'0.1',
        'blue':'0.25',
        'green':'0.5',
        'brown':'1',
        'red':'2',
        'gold':'5',
        'silver':'10'
    }
    #We get the value and separate in fragments
    value = get_value(colors)
    fragment = [value[max(i - 3, 0):i] for i in range(len(value), 0, -3)][::-1]
    
    decimal = ''
    tolerance_field = ''

    #Then, we get the 2 other digits for add as a decimal number, just in case to be necessary.
    if len(fragment) > 1 and fragment[1]:
        sub = fragment[1]
        if len(sub) >= 2 and sub[1] in '123456789':
            decimal = sub[0] + sub[1]
        elif len(sub) >= 1 and sub[0] in '123456789':
            decimal = sub[0]
    if len(decimal) > 0:
        decimal = '.' + decimal
    
    if len(colors)> 3:
        tolerance_field = f" ±{tolerance_band[colors[-1]]}%"
    
    resistance_value = fragment[0] + decimal + ' ' + metric_prefix[len(fragment) - 1] + tolerance_field
    
    return  resistance_value