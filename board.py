class Board:

    def __init__(self):
        self.state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def move(self, player: int, position: tuple):
        assert player == -1 or player == 1
        assert 0 <= position[0] <= 2
        assert 0 <= position[1] <= 2
        assert self.state[position[0]][position[1]] == 0
        new_plays_difference = self._count_plays_difference() + player
        assert new_plays_difference == 0 or new_plays_difference == 1
        self.state[position[0]][position[1]] = player

    def _count_plays_difference(self):
        result = 0
        for row in range(0, 2):
            for col in range(0, 2):
                result += self.state[row][col]
        return result
