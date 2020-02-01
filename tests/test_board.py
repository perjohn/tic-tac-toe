import pytest

from board import Board


def test_move():
    board = Board()
    assert board._state[0][0] == 0

    board.move(player=1, position=(1, 1))
    assert board._state[1][1] == 1

    board.move(player=-1, position=(0, 0))
    assert board._state[0][0] == -1


def test_illegal_move_outside_board():
    board = Board()
    with pytest.raises(AssertionError):
        board.move(1, (3, 3))

    with pytest.raises(AssertionError):
        board.move(1, (-1, 2))


def test_illegal_move_unknown_player():
    board = Board()
    with pytest.raises(AssertionError):
        board.move(2, (1, 1))


def test_illegal_move_cell_occupied():
    board = Board()
    board.move(1, (1, 1))
    with pytest.raises(AssertionError):
        board.move(0, (1, 1))


def test_illegal_move_illegal_state():
    board = Board()
    board.move(1, (1, 1))
    with pytest.raises(AssertionError):
        board.move(1, (0, 1))

    board = Board()
    with pytest.raises(AssertionError):
        board.move(0, (1, 1))


def test_check_win_empty():
    board = Board()
    result = board.check_win()
    assert not result


def test_check_win_column():
    board = Board()
    board.move(1, (1, 1))
    board.move(-1, (0, 0))
    board.move(1, (0, 1))
    board.move(-1, (2, 2))
    board.move(1, (2, 1))
    result = board.check_win()
    assert result


def test_check_win_row():
    board = Board()
    board.move(1, (1, 1))
    board.move(-1, (0, 0))
    board.move(1, (2, 2))
    board.move(-1, (0, 1))
    board.move(1, (2, 1))
    board.move(-1, (0, 2))
    result = board.check_win()
    assert result


def test_check_diagonal():
    board = Board()
    board.move(1, (1, 1))
    board.move(-1, (0, 1))
    board.move(1, (0, 0))
    result = board.check_win()
    assert not result
    board.move(-1, (0, 2))
    board.move(1, (2, 2))
    result = board.check_win()
    assert result


def test_to_string_empty_board():
    board = Board()
    result = board.__str__()
    assert result == '''
-------------
|   |   |   |
|   |   |   |
|   |   |   |
-------------
'''


def test_to_string_moves():
    board = Board()
    board.move(1, (1, 1))
    board.move(-1, (0, 0))
    result = board.__str__()
    assert result == '''
-------------
| O |   |   |
|   | X |   |
|   |   |   |
-------------
'''
