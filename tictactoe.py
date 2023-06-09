"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # Initialize the counts for each player, Allowing for the game to start with the X player going first
    count_X = 0
    count_O = 0

    for rows in board:
        for space in rows:
            if space == X:
                count_X += 1
            elif space == O:
                count_O += 1

    # X will always go first, so if the counts are equal then theoretically it should be X's turn
    if count_X == count_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    # Iterate through the rows of the board (ex: if it's a standard ttt board it would have 3 rows)
    for row in range(len(board)):
        # Iterate through the spaces of any given row (ex: if it's a standard ttt board each row would have 3 spaces)
        for space in range(len(board[row])):
            # If the given space is EMPTY add the (row, space) {ex: (row)1, (space)2 == EMPTY} to the possible moves set
            if board[row][space] == EMPTY:
                possible_moves.add((row, space))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    while True:
        for row in range(len(board)):
            for space in range(len(board[row])):
                try:
                    if board[row][space] == EMPTY:
                        board[row][space] = action
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print(
                        f"Space: row {row} / position {space} is currently occupied, please choose another spot"
                    )

        return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if EMPTY in board:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
