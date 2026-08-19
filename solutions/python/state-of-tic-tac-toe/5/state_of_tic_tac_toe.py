""" This module review a tic-tac-toe game
"""

def gamestate(board):
    """This function evalutes a tic-tac-toe game and determinate the results.
        Parameter:
            Board(list): represents the game board
        Return:
            status(string): The final status of the game.
    """
    match = [
        # rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # cols
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    
    count = 0
    previus = ""
    for pos_1, pos_2, pos_3 in match:
        if pos_1 == pos_2 == pos_3 and pos_1 != " ":
            if previus == pos_1:
                count -= 1
            count += 1
            previus = pos_1
    if count == 1:
        return "win"
    if count > 1:
        raise ValueError("Impossible board: game should have ended after the game was won")
        
    white_spaces = any(" " in row for row in board)

    if not white_spaces:
        return "draw"

    for row in board:
        if "XX" in row:
            raise ValueError("Wrong turn order: X went twice")
        if "OO" in row:
            raise ValueError("Wrong turn order: O started")
    
    return "ongoing"