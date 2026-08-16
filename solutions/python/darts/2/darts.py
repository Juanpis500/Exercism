"""
    This module can calculate the score of the dart with a posicion given.
"""

def score(x, y):
    """Calculating the score

        Parameters:
            x(int): position at point x
            y(int): position at point y
        
        Returns:
            points(int): the total points of the posicion.
    """

    if x ** 2 + y ** 2 > 100:
        return 0
    if 25 < x ** 2 + y ** 2 <= 100:
        return 1
    if 1 < x ** 2 + y ** 2 <= 25:
        return 5
    if 0 <= x ** 2 + y ** 2 <= 1:
        return 10
    
    return None