import click

from game import Game


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


if __name__ == '__main__':
    cli()
