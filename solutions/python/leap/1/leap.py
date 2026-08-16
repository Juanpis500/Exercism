"""
    This module coins the function about calculate if a given year is a leap.
"""

def leap_year(year):
    """
        This function calculates if a year is leap.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
