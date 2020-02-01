import click

from board import Board


class Agent:
    def __init__(self):
        self.board = Board()

    def two_player(self):
        win = False
        player = 1
        while not win:
            value = click.prompt(f'Move for player {"X" if player == 1 else "O"}', type=str)
            move = (int(value.replace(' ', '').split(',')[0]), int(value.replace(' ', '').split(',')[1]))
            self.board.move(player=player, position=move)
            print(self.board)
            win = self.board.check_win()
            if win:
                print(f'Player {"X" if player == 1 else "O"} has won')
            player = -player
