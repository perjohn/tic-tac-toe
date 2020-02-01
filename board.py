class Board:

    def __init__(self):
        self._state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def move(self, player: int, position: tuple):
        assert player == -1 or player == 1
        assert 0 <= position[0] <= 2
        assert 0 <= position[1] <= 2
        assert self._state[position[0]][position[1]] == 0
        new_plays_difference = self._count_plays_difference() + player
        assert new_plays_difference == 0 or new_plays_difference == 1
        self._state[position[0]][position[1]] = player

    def check_win(self) -> bool:
        rows_win = self._check_rows_win()
        if rows_win:
            return True
        columns_win = self._check_columns_win()
        if columns_win:
            return True
        return self._check_diagonal_win()

    def _check_rows_win(self) -> bool:
        result = False
        for row in self._state:
            row_sum = sum([cell for cell in row])
            if row_sum == 3 or row_sum == -3:
                return True
        return result

    def _check_columns_win(self) -> bool:
        result = False
        for column_index in range(0, 3):
            column_sum = 0
            for row_index in range(0, 3):
                column_sum += self._state[row_index][column_index]
            if column_sum == 3 or column_sum == -3:
                return True
        return result

    def _check_diagonal_win(self) -> bool:
        result = False
        diagonal_sum = 0
        for index in range(0, 3):
            diagonal_sum += self._state[index][index]
            if diagonal_sum == 3 or diagonal_sum == -3:
                return True
        diagonal_sum = 0
        for index in range(0, 3):
            diagonal_sum += self._state[index][2 - index]
            if diagonal_sum == 3 or diagonal_sum == -3:
                return True
        return result

    def _count_plays_difference(self):
        result = 0
        for row in range(0, 3):
            for col in range(0, 3):
                result += self._state[row][col]
        return result

    def __str__(self):
        def format_cell(cell):
            return "X" if cell == 1 else "O" if cell == -1 else " "

        result = '\n-------------\n'
        for row in self._state:
            result += f'| {format_cell(row[0])} | {format_cell(row[1])} | {format_cell(row[2])} |\n'
        result += '-------------\n'
        return result
