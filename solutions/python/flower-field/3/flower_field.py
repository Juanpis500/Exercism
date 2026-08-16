"""
    This module contains a pair of functions that calculate how many neighbors flower are in a garden.
"""

def get_neighbors(garden, row, col):
    """ Calculates the total of neighbors flower in a exact position.
        Parameters:
            garden(list): the field with flowers
            row(int): the row that will check their neighbors.
            col(int): the col that will check their neighbors.
        Return:
            total_neigbors(string): the total of neighbors flower in the specific position.
    """
    rows = len(garden)
    cols = len(garden[0])
    neighbors = []
    total_neigbors = ''
    positions = [
        (-1, -1), (-1, 0), (-1, 1),  
        ( 0, -1),          ( 0, 1),  
        ( 1, -1), ( 1, 0), ( 1, 1)   
    ]
    
    for posr, posc in positions:
        new_pos_r = posr + row
        new_pos_c = posc + col
        if 0 <= new_pos_r < rows and 0 <= new_pos_c < cols:
            neighbors.append(garden[new_pos_r][new_pos_c])

    if neighbors.count('*') == 0:
        total_neigbors = ' '
    else:
        total_neigbors = str(neighbors.count('*'))
        
    return total_neigbors
    

def annotate(garden):
    """ This function changes the flower field and put the number of the neighbors.
        Parameters:
            garden(list): The flower field
        Return:
            garden(list): The flower field modified
    """
    # Function body starts here
    if not all(char in {' ', '*'} for item in garden for char in item):
        raise ValueError('The board is invalid with current input.')
    if not any('*' in item for item in garden):
        return garden
    if any(len(item) != len(garden[0]) for item in garden):
        raise ValueError('The board is invalid with current input.')
        
    garden = [item.replace(' ','.') for item in garden]
    temp = ''
    for index_r in range(len(garden)):
        temp = ''
        for index_c in range(len(garden[index_r])):
            if garden[index_r][index_c] == '*':
                temp += '*'
                continue
            temp += get_neighbors(garden, index_r,index_c)
        garden[index_r] = temp

    return garden