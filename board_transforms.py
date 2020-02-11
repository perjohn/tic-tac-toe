import numpy as np

from board import Board


def mirror_lr(board: Board) -> Board:
    new_state = np.fliplr(board.state)
    return Board(new_state)


def mirror_ud(board: Board) -> Board:
    new_state = np.flipud(board.state)
    return Board(new_state)


def rotate_90(board: Board) -> Board:
    new_state = np.rot90(board.state)
    return Board(new_state)
