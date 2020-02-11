import numpy as np

from board import Board
from board_transforms import mirror_lr, mirror_ud, rotate_90


def test_mirror_lr():
    board = Board()
    board.state = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
    result = mirror_lr(board)

    expected = Board(np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
    assert result == expected


def test_mirror_ud():
    board = Board()
    board.state = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
    result = mirror_ud(board)

    expected = Board(np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]]))
    assert result == expected


def test_rotate_90():
    board = Board()
    board.state = np.array([[0, 0, 1], [0, -1, 0], [0, 0, 1]])
    result = rotate_90(board)

    expected = Board(np.array([[1, 0, 1], [0, -1, 0], [0, 0, 0]]))
    assert result == expected
