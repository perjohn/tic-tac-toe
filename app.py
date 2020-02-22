import pickle

import click

from agent import Agent
from board import Board, PLAYER_X
from game import Game
from train import Trainer


@click.group()
def cli():
    pass


@cli.command()
def one_player():
    board = Board()
    agent = Agent(board, PLAYER_X, exploration_rate=0)
    agent.q_values = pickle.load(open("model/tic-tac-toe-agent-x-epochs-2000.pickle", "rb"))
    game = Game()
    game.one_player(board, agent)


@cli.command()
def two_player():
    game = Game()
    game.two_player()


@cli.command()
@click.option('--epochs', default=10, help='Number of training epochs.', type=int)
@click.option('--exploration-rate', default=0.3, help='Exploration rate.', type=float)
@click.option('--save-dir', help='Directory to save results.', type=click.Path(exists=True))
def train(epochs, exploration_rate, save_dir):
    trainer = Trainer(exploration_rate=exploration_rate, save_dir=save_dir)
    trainer.train(epochs=epochs)


if __name__ == '__main__':
    cli()
