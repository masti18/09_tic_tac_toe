"""Simple random-move computer opponent for O."""

import random


def choose_move(board):
    empty_cells = [
        (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] is None
    ]
    return random.choice(empty_cells) if empty_cells else None
