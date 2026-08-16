"""    This module contains a function that returns a specific code depending on the binary code in parameters.

"""


def commands(binary_str):
    """ Transform binary number into handshake code.
            Parameter:
                binary_str(string): includes the binary code.
            Return:
                handshake(list): Hanshake code in order.
    """
    actions = [
        'wink',
        'double blink',
        'close your eyes',
        'jump'
    ]
    handshake = []
    binary_reverse = binary_str[::-1]

    for index, bin in enumerate(binary_reverse):
        if bin == '1' and index < 4:
            handshake.append(actions[index])
        if bin == '1' and index == 4:
            handshake.reverse()

    return handshake