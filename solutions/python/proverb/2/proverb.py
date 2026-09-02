""" Generate a proverb.
"""

def proverb(*data,qualifier=None):
    """ Generate a proverb based on the provided data and optional qualifier.

        Parameters:
            data(list/tuples): The elements for generate a proverb.
            qualifier(str): The optional qualifier.
        Return:
            complete_proverb(list): Proverb sliced by phrases.
    """
    if not data:
        return []
        
    quali = f'{qualifier} ' if qualifier else ''
    complete_proverb = [f"For want of a {first} the {second} was lost." for first, second in zip(data, data[1:])]

    first_item = data[0]
    complete_proverb.append(f"And all for the want of a {quali}{first_item}.")
        
    return complete_proverb