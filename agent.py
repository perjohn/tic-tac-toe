import random

import numpy as np

from board import Board


class Agent:
    def __init__(self, board: Board, player: int, exploration_rate: float = 0.3, learning_rate: float = 0.2):
        self.board = board
        self.player = player
        self.exploration_rate = exploration_rate
        self.learning_rate = learning_rate
        self.decay_gamma = 0.9
        self.q_values = {}
        self.moves = []

    def choose_move(self) -> tuple:
        if self.board not in self.q_values:
            self.q_values[Board(state=self.board.state)] = self._get_initial_q_values_for_board(self.board)
        if np.random.uniform(0, 1) < self.exploration_rate:
            move = random.choice(self.board.get_possible_moves(self.player))
        else:
            move = self._get_move_with_highest_value()
        self.moves.append((Board(state=self.board.state), move))
        return move

    def update_q_values(self, reward: int):
        for move in self.board.get_possible_moves(self.player):
            self.q_values[self.board] = (move, reward)
        for board, move in reversed(self.moves):
            current_q_value = self.q_values[board][move]
            reward = current_q_value + self.learning_rate * (self.decay_gamma * reward - current_q_value)
            self.q_values[board][move] = round(reward, 3)

    def reset(self, board: Board):
        self.board = board
        self.moves = []

    def _get_move_with_highest_value(self):
        highest_value = 0
        highest_value_move = None
        for move, q_value in self.q_values[self.board].items():
            if q_value >= highest_value:
                highest_value = q_value
                highest_value_move = move
        return highest_value_move

    # def _get_initial_q_values(self) -> dict:
    #     result = {}
    #     for board in self._get_initial_boards():
    #         result[board] = self._get_initial_q_values_for_board(board)
    #     return result

    def _get_initial_q_values_for_board(self, board: Board):
        moves = board.get_possible_moves(self.player)
        return {move: 0 for move in moves}

    @staticmethod
    def _get_initial_boards() -> list:
        return [
            Board(np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])),
            Board(np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]])),
        ]
