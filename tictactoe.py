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

    raise NotImplementedError

    for rows in board:
        for space in rows:
            if not space == EMPTY:
                pass
            else:
                # possible moves would have to include (row, space) then what the actual move would be I imagine
                possible_moves = (row, space)
                return


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


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
