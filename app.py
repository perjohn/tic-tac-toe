import click

from agent import Agent


@click.group()
def cli():
    pass


@cli.command()
def one_player():
    pass


@cli.command()
def two_player():
    agent = Agent()
    agent.two_player()


if __name__ == '__main__':
    cli()
