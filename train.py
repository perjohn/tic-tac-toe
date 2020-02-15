from agent import Agent
from board import Board, PLAYER_X, PLAYER_O

WIN_REWARD = 1
LOSE_REWARD = -1


class Trainer:
    def __init__(self, exploration_rate: float):
        self.exploration_rate = exploration_rate

    def train(self, epochs: int):
        for epoch in range(epochs):
            done = False
            while not done:
                board = Board()
                agent_x = Agent(board, PLAYER_X, self.exploration_rate)
                agent_o = Agent(board, PLAYER_O, self.exploration_rate)
                move_x = agent_x.choose_move()
                board.move(PLAYER_X, move_x)
                done = board.check_win()
                if done:
                    agent_x.update_q_values(WIN_REWARD)

                move_o = agent_o.choose_move()
                board.move(PLAYER_O, move_o)
                done = board.check_win()
