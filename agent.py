import numpy as np

from board import Board


class Agent:
    def __init__(self, board: Board):
        self.board = board

    def choose_move(self, exploration_rate: float):
        if np.random.uniform(0, 1) <= exploration_rate:
            pass

    def get_possible_moves(self, player: int) -> list:
        result = []
        for row in range(3):
            for column in range(3):
                if self.board.is_valid_move(player, (row, column)):
                    result.append((row, column))
        return result
