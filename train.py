from agent import Agent
from board import Board, PLAYER_X, PLAYER_O

WIN_REWARD = 1
LOSE_REWARD = -1


class Trainer:
    def __init__(self, exploration_rate: float):
        self.exploration_rate = exploration_rate
        self.board = Board()
        self.agent_x = Agent(self.board, PLAYER_X, self.exploration_rate)
        self.agent_o = Agent(self.board, PLAYER_O, self.exploration_rate)

    def train(self, epochs: int):
        for epoch in range(epochs):
            print(f'Epoch {epoch}')
            done = False
            while not done:
                move_x = self.agent_x.choose_move()
                self.board.move(PLAYER_X, move_x)
                done = self.board.check_win()
                if done:
                    self.agent_x.update_q_values(WIN_REWARD)
                    self.agent_o.update_q_values(LOSE_REWARD)
                    continue

                move_o = self.agent_o.choose_move()
                self.board.move(PLAYER_O, move_o)
                done = self.board.check_win()
                if done:
                    self.agent_x.update_q_values(LOSE_REWARD)
                    self.agent_o.update_q_values(WIN_REWARD)
                    continue

    def reset(self):
        self.board = Board()
        self.agent_x.reset(self.board)
        self.agent_o.reset(self.board)
