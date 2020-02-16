import click

from game import Game
from train import Trainer


@click.group()
def cli():
    pass


@cli.command()
def one_player():
    game = Game()
    game.one_player()


@cli.command()
def two_player():
    game = Game()
    game.two_player()


@cli.command()
@click.option('--epochs', default=10, help='Number of training epochs.', type=int)
@click.option('--exploration-rate', default=0.3, help='Exploration rate.', type=float)
def train(epochs, exploration_rate):
    trainer = Trainer(exploration_rate=exploration_rate)
    trainer.train(epochs=epochs)


if __name__ == '__main__':
    cli()
