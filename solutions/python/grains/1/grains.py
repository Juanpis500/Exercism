import math

def square(number):
    if (number <= 0 or number > 64):
        raise ValueError("square must be between 1 and 64")
        
    return 2 ** (number - 1)


def total():
    total = 0
    number = 64
    while number > 0:
        total += 2 ** (number - 1) 
        number -= 1

    return total