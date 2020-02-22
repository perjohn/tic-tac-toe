import click

from agent import Agent
from board import Board, PLAYER_X, PLAYER_O


class Game:

    @staticmethod
    def one_player(board: Board, agent: Agent):
        win = False
        while not win:
            board.move(player=PLAYER_X, position=agent.choose_move())
            print(board)
            win = board.check_win()
            if win:
                print(f'You have lost')
                continue
            elif board.check_draw():
                print(f'Draw')
                continue
            value = click.prompt(f'Move for player O', type=str)
            move = (int(value.replace(' ', '').split(',')[0]), int(value.replace(' ', '').split(',')[1]))
            board.move(player=PLAYER_O, position=move)
            print(board)
            win = board.check_win()
            if win:
                print(f'You have won')
            elif board.check_draw():
                print(f'Draw')

    @staticmethod
    def two_player(board: Board):
        win = False
        player = 1
        while not win:
            value = click.prompt(f'Move for player {"X" if player == 1 else "O"}', type=str)
            move = (int(value.replace(' ', '').split(',')[0]), int(value.replace(' ', '').split(',')[1]))
            board.move(player=player, position=move)
            print(board)
            win = board.check_win()
            if win:
                print(f'Player {"X" if player == 1 else "O"} has won')
            player = -player
