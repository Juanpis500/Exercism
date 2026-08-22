""" This module include a function that converts images of text into machine-readable text. (numbers in this case).

"""
def convert(input_grid):
    """ Transform image number into machine-readable text.
    
        Parameter:
            input_grid(list): This is a list of image number separete into 3x4.
        Reutrn:
            final_number(str): It's the machine-readable text number.
    """
    patterns = {
        (" _ ", "| |", "|_|", "   "): "0",
        ("   ", "  |", "  |", "   "): "1",
        (" _ ", " _|", "|_ ", "   "): "2",
        (" _ ", " _|", " _|", "   "): "3",
        ("   ", "|_|", "  |", "   "): "4",
        (" _ ", "|_ ", " _|", "   "): "5",
        (" _ ", "|_ ", "|_|", "   "): "6",
        (" _ ", "  |", "  |", "   "): "7",
        (" _ ", "|_|", "|_|", "   "): "8",
        (" _ ", "|_|", " _|", "   "): "9",
    }

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(number) % 3 != 0 for number in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    numbers = []
    for r in range(0, len(input_grid), 4):
        for i in range(0, len(input_grid[0]), 3):
            one_number = (
                input_grid[0 + r][i : i + 3],
                input_grid[1 + r][i : i + 3],
                input_grid[2 + r][i : i + 3],
                input_grid[3 + r][i : i + 3],
            )
            numbers.append(one_number)
        if len(input_grid) > 4 and r != len(input_grid)-4:    
            numbers.append(',')
            
    final_number = ''
    for num in numbers:
        if patterns.get(num) != None:
            final_number += patterns.get(num)
        elif num == ',':
            final_number += ','
        else:
            final_number += '?'
    
    return final_number