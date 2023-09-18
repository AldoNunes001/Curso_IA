"""
Tic Tac Toe Player
"""

import math
import copy
import numpy as np

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_O = 0
    count_X = 0
    for row in board:
        count_O += row.count('O')
        count_X += row.count('X')
    
    if count_X > count_O:
        return 'O'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square is None:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    if action not in possible_actions:
        raise Exception('Not a valid action.')

    current_player = player(board)
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board_x = []
    board_o = []
    for i, row in enumerate(board):
        row_x = []
        row_o = []
        for j, square in enumerate(row):
            if square == 'X':
                row_x.append(1)
            else:
                row_x.append(0)
            if square == 'O':
                row_o.append(1)
            else:
                row_o.append(0)

        board_x.append(row_x)
        board_o.append(row_o)

    board_x = np.asarray(board_x)
    board_o = np.asarray(board_o)

    sums_rows_x = board_x.sum(axis=1)
    sums_cols_x = board_x.sum(axis=0)
    sums_principal_diagonal_x = np.trace(board_x)
    board_x = np.fliplr(board_x)
    sums_anti_diagonal_x = np.trace(board_x)

    sums_rows_o = board_o.sum(axis=1)
    sums_cols_o = board_o.sum(axis=0)
    sums_principal_diagonal_o = np.trace(board_o)
    board_o = np.fliplr(board_o)
    sums_anti_diagonal_o = np.trace(board_o)

    if (3 in sums_rows_x) or (3 in sums_cols_x) or (sums_principal_diagonal_x == 3) or (sums_anti_diagonal_x == 3):
        return 'X'
    elif (3 in sums_rows_o) or (3 in sums_cols_o) or (sums_principal_diagonal_o == 3) or (sums_anti_diagonal_o == 3):
        return 'O'

    return


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if None in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_ = winner(board)
    if winner_ == 'X':
        return 1
    elif winner_ == 'O':
        return -1
    else:
        return 0


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    play = player(board)

    if play == 'X':
        if board == initial_state():
            return (1, 0)

        moves = []

        for action in actions(board):
            moves.append( (min_value(result(board, action)), action) )

        moves.sort()
        moves.reverse()

        return moves[0][1]

    elif play == 'O':
        moves = []

        for action in actions(board):
            moves.append( (max_value(result(board, action)), action) )

        moves.sort()

        return moves[0][1]
