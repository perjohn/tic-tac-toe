import numpy as np

from board import Board


class Trainer:
    def __init__(self, exploration_rate: float):
        self.exploration_rate = exploration_rate

    def train(self, epochs: int):
        for epoch in range(epochs):
            board = Board()
 