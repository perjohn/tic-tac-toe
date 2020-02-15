import random

import numpy as np

from board import Board


class Agent:
    def __init__(self, board: Board, player: int, exploration_rate: float = 0.3):
        self.board = board
        self.player = player
        self.exploration_rate = exploration_rate
        self.q_values = self._get_initial_q_values()
        self.moves = []

    def choose_move(self) -> tuple:
        if np.random.uniform(0, 1) < self.exploration_rate:
            move = random.choice(self.board.get_possible_moves(self.player))
        else:
            move = self._get_move_with_highest_value()
        self.moves.append((Board(state=self.board.state), move))
        return move

    def update_q_values(self, reward: int):
        for move in self.board.get_possible_moves(self.player):
            self.q_values[self.board] = (move, reward)
        # current_q_value = self.q_values[state[0]][state[1]]
        # reward = current_q_value + self.learning_rate * (self.decay_gamma * reward - current_q_value)
        # self.q_values[state[0]][state[1]] = round(reward, 3)

    def _get_move_with_highest_value(self):
        highest_value = 0
        highest_value_move = None
        for move, q_value in self.q_values[self.board]:
            if q_value > highest_value:
                highest_value = q_value
                highest_value_move = move
        return highest_value_move

    def _get_initial_q_values(self) -> dict:
        result = {}
        for board in self._get_initial_boards():
            moves = board.get_possible_moves(self.player)
            result[board] = [(move, 0) for move in moves]
        return result

    @staticmethod
    def _get_initial_boards() -> list:
        return [
            Board(np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])),
            Board(np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]])),
        ]
