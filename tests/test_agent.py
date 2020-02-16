import numpy as np
from mock import patch

from agent import Agent
from board import Board, PLAYER_X


@patch('numpy.random.uniform')
@patch('random.choice')
def test_choose_move(mock_choice, mock_uniform):
    mock_uniform.return_value = 0.1
    mock_choice.return_value = (1, 1)
    agent = Agent(Board(), PLAYER_X, exploration_rate=0.2)
    result = agent.choose_move()
    assert result == (1, 1)
    assert len(agent.moves) == 1
    assert agent.moves[0] == (Board(), (1, 1))

# def test_initial_q_values():
#     agent = Agent(Board(), PLAYER_X)
#     result = agent.q_values
#     assert len(result[Board()]) == 9
#     move_q_values = result[Board()]
#     assert move_q_values[(1, 1)] == 0
#     assert len(result[Board(np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]]))]) == 7
