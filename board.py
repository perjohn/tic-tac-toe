import numpy as np

PLAYER_X = 1
PLAYER_O = -1


class Board:

    def __init__(self, state: np.ndarray = None):
        if state is not None:
            self.state = state.copy()
        else:
            self.state = np.zeros((3, 3))

    def move(self, player: int, position: tuple):
        assert self.is_valid_move(player, position)
        self.state[position[0]][position[1]] = player

    def is_valid_move(self, player, position: tuple) -> bool:
        if player != PLAYER_X and player != PLAYER_O:
            return False
        if position[0] < 0 or position[0] > 2:
            return False
        if position[1] < 0 or position[1] > 2:
            return False
        if self.state[position[0]][position[1]] != 0:
            return False
        new_plays_difference = self._count_plays_difference() + player
        if new_plays_difference != 0 and new_plays_difference != 1:
            return False
        return True

    def check_win(self) -> bool:
        rows_win = self._check_rows_win()
        if rows_win:
            return True
        columns_win = self._check_columns_win()
        if columns_win:
            return True
        return self._check_diagonal_win()

    def _check_rows_win(self) -> bool:
        return np.any(np.sum(self.state, axis=0) == 3) or np.any(np.sum(self.state, axis=0) == -3)

    def _check_columns_win(self) -> bool:
        return np.any(np.sum(self.state, axis=1) == 3) or np.any(np.sum(self.state, axis=1) == -3)

    def _check_diagonal_win(self) -> bool:
        return np.trace(self.state) == 3 or np.trace(self.state) == -3 \
               or np.trace(np.fliplr(self.state)) == 3 or np.trace(np.fliplr(self.state)) == -3

    def _count_plays_difference(self):
        result = 0
        for row in range(0, 3):
            for col in range(0, 3):
                result += self.state[row][col]
        return result

    def get_possible_moves(self, player: int) -> list:
        result = []
        for row in range(3):
            for column in range(3):
                if self.is_valid_move(player, (row, column)):
                    result.append((row, column))
        return result

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return np.array_equal(self.state, other.state)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.state[0, 0], self.state[0, 1], self.state[0, 2],
                     self.state[1, 0], self.state[1, 1], self.state[1, 2],
                     self.state[2, 0], self.state[2, 1], self.state[2, 2]))

    def __str__(self):
        def format_cell(cell):
            return "X" if cell == 1 else "O" if cell == -1 else " "

        result = '\n-------------\n'
        for row in self.state:
            result += f'| {format_cell(row[0])} | {format_cell(row[1])} | {format_cell(row[2])} |\n'
        result += '-------------\n'
        return result
