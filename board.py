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

    def _count_plays_difference(self):
        result = 0
        for row in range(0, 2):
            for col in range(0, 2):
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
