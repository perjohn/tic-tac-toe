from agent import Agent
from board import Board


def test_get_possible_moves():
    board = Board()
    agent = Agent(board)
    result = agent.get_possible_moves(1)
    assert len(result) == 9
