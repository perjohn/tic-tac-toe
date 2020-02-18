import pickle
import os

from agent import Agent
from board import Board, PLAYER_X, PLAYER_O

WIN_REWARD = 1
LOSE_REWARD = -1
DRAW_REWARD = 0


class Trainer:
    def __init__(self, exploration_rate: float, save_dir: str):
        self.exploration_rate = exploration_rate
        self.save_dir = save_dir

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
                if self.board.check_win():
                    self.set_rewards(WIN_REWARD, LOSE_REWARD)
                    done = True
                    continue
                elif self.board.check_draw():
                    self.set_rewards(DRAW_REWARD, DRAW_REWARD)
                    done = True
                    continue

                move_o = self.agent_o.choose_move()
                self.board.move(PLAYER_O, move_o)
                if self.board.check_win():
                    self.set_rewards(LOSE_REWARD, WIN_REWARD)
                    done = True
                    continue
                elif self.board.check_draw():
                    self.set_rewards(DRAW_REWARD, DRAW_REWARD)
                    done = True
                    continue

        self.save(epochs)

    def set_rewards(self, agent_x_reward: int, agent_o_reward: int):
        self.agent_x.update_q_values(agent_x_reward)
        self.agent_o.update_q_values(agent_o_reward)
        self.reset()

    def reset(self):
        self.board = Board()
        self.agent_x.reset(self.board)
        self.agent_o.reset(self.board)

    def save(self, epochs: int):
        if self.save_dir:
            file_name = os.path.join(self.save_dir, f'tic-tac-toe-agent-x-epochs-{epochs}.pickle')
            with open(file_name, 'wb') as x_handle:
                pickle.dump(self.agent_x.q_values, x_handle)
