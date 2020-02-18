import numpy as np

from board import Board


def test_move():
    board = Board()
    assert board.state[0][0] == 0

    board.move(player=1, position=(1, 1))
    assert board.state[1][1] == 1

    board.move(player=-1, position=(0, 0))
    assert board.state[0][0] == -1


def test_is_valid_move():
    board = Board()

    assert board.is_valid_move(1, (1, 1))
    board.move(player=1, position=(1, 1))

    assert board.is_valid_move(-1, (0, 0))


def test_is_valid_move_outside_board():
    board = Board()
    assert not board.is_valid_move(1, (3, 3))
    assert not board.is_valid_move(1, (0, 3))
    assert not board.is_valid_move(1, (-1, 2))


def test_is_valid_move_unknown_player():
    board = Board()
    assert not board.is_valid_move(2, (1, 1))


def test_is_valid_cell_occupied():
    board = Board()
    board.move(1, (1, 1))
    assert not board.is_valid_move(1, (1, 1))


def test_is_valid_illegal_state():
    board = Board()
    board.move(1, (1, 1))
    assert not board.is_valid_move(1, (0, 1))

    board = Board()
    assert not board.is_valid_move(0, (1, 1))


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


def test_check_win_diagonal():
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


def test_check_win_diagonal_other():
    board = Board()
    board.move(1, (1, 1))
    board.move(-1, (0, 1))
    board.move(1, (0, 2))
    result = board.check_win()
    assert not result
    board.move(-1, (0, 0))
    board.move(1, (2, 0))
    result = board.check_win()
    assert result


def test_check_draw():
    board = Board(np.array([[-1, 1, -1], [1, 1, -1], [1, -1, 1]]))
    result = board.check_draw()
    assert result

    board = Board(np.array([[0, 1, -1], [1, 1, -1], [1, -1, 1]]))
    result = board.check_draw()
    assert not result


def test_get_possible_moves_empty_board():
    board = Board()
    result = board.get_possible_moves(1)
    assert len(result) == 9


def test_get_possible_moves_one_space_left():
    board = Board(np.array([[1, -1, 1], [-1, 1, -1], [1, -1, 0]]))
    result = board.get_possible_moves(1)
    assert len(result) == 1
    assert result[0] == (2, 2)


def test_equality():
    board1 = Board()
    board2 = Board()
    assert board1 == board2

    board1.move(1, (1, 1))
    assert board1 != board2

    board2.move(1, (1, 1))
    assert board1 == board2


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
