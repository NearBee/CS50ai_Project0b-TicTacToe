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
            # If the given space is EMPTY add the (row, space) to possible_moves set {ex: (row)1, (space)2 == EMPTY} to the possible moves set
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
    for row in board:
        # Return a result for vertical wins
        if row[0] == X and row[1] == X and row[2] == X:
            return X
        if row[0] == O and row[1] == O and row[2] == O:
            return O

    # Return a result for horizontal wins
    for i in range(3):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        if board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O

    # Return a winner for diagonal wins
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    # Return None if there is a Tie
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or not any(EMPTY in spaces for spaces in board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
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

            if value > min_value:
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
