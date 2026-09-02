""" Given an input text output it transposed.
"""

def transpose(text):
    """ Given an input text output it transposed.
        
    """
    if not text:
        return ''
    
    lines = text.splitlines()

    padded_lines = []
    for i, line in enumerate(lines):
        max_future_len = max((len(l) for l in lines[i:]), default=0)
        padded_lines.append(line.ljust(max_future_len, ' '))

    
    max_len = max(len(line) for line in lines)
    full_lines = [line.ljust(max_len, '\0') for line in padded_lines]

    trasposed_lines = zip(*full_lines)

    transposed_rows = ["".join(row).rstrip('\0') for row in trasposed_lines]
    
    return "\n".join(transposed_rows)