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
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

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

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid Action")

    player_turn = player(board)
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player_turn
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Return a result for horizontal wins
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Return a result for vertical wins
    for col in range(3):
        if board[0][col] == X and board[1][col] == X and board[2][col] == X:
            return X
        if board[0][col] == O and board[1][col] == O and board[2][col] == O:
            return O

    # Return a winner for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # Return None if there is a Tie
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or all(
        all(space is not None for space in row) for row in board
    ):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    player_turn = player(board)

    if terminal(board):
        return None

    if player_turn == X:
        max_value = -math.inf
        optimal_action = None

        for action in actions(board):
            new_board = result(board, action)
            value = min_value_helper(new_board)

            if value > max_value:
                max_value = value
                optimal_action = action

        return optimal_action

    elif player_turn == O:
        min_value = math.inf
        optimal_action = None

        for action in actions(board):
            new_board = result(board, action)
            value = max_value_helper(new_board)

            if value < min_value:
                min_value = value
                optimal_action = action

        return optimal_action


def min_value_helper(board):
    """Helper function for returning the min value of possible actions"""
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value_helper(result(board, action)))

    return v


def max_value_helper(board):
    """Helper function for returning the max value of possible actions"""
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value_helper(result(board, action)))

    return v
