def proverb(*data,qualifier=None):
    """ Generate a proverb based on the provided data and optional qualifier.

        Parameters:
            data(list/tuples): The elements for generate a proverb.
            qualifier(str): The optional qualifier.
        Return:
            proverb(list): Proverb sliced by phrases.
    """
    if not data:
        return []
        
    quali = f'{qualifier} ' if qualifier else ''
    proverb = [f"For want of a {first} the {second} was lost." for first, second in zip(data, data[1:])]

    first_item, *_ = data
    proverb.append(f"And all for the want of a {quali}{first_item}.")
        
    return proverb