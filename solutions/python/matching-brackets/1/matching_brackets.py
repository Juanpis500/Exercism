"""
    This module contains a function to calculate equality.
"""


def is_paired(input_string):
    """ This function determine if a string contains an equal Characters.
    
        Parameters:
            input_string(string): this string that will analise.
        Return:
            bool: True or False if the string match with the conditions.
    """
    stack = []
    pattern = {')': '(', ']': '[', '}': '{'}
    for item in input_string: 
        if item in pattern.values():
            stack.append(item)
        elif item in pattern:
            if not stack or stack[-1] != pattern[item]:
                return False
            stack.pop()
            
    return len(stack) == 0