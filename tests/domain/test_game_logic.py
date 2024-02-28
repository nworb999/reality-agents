import pytest
from unittest.mock import patch
from reality_agents.domain.game_logic import GameLogic
from reality_agents.domain.game_state import GameState


@pytest.fixture
def characters():
    return [
        {"name": "Alice", "personality": "friendly"},
        {"name": "Bob", "personality": "grumpy"},
    ]


@pytest.fixture
def game_logic(characters):
    return GameLogic(characters=characters)


def test_initialization(game_logic, characters):
    assert game_logic.characters == characters
    assert isinstance(game_logic.game_state, GameState)
    assert game_logic.max_turns == 5


def test_reset_game(game_logic):
    game_logic.reset_game()
    assert game_logic.game_state.current_turn == 1
    assert game_logic.game_state.current_conversation is not None


@patch("reality_agents.domain.game_state.GameState.continue_conversation")
def test_update_game(mock_continue_conversation, game_logic):
    mock_return_value = (0, "Alice", "Bob", "Hello, Bob!")
    mock_continue_conversation.return_value = mock_return_value

    script = [{"dialogue": "Hello, Bob!", "speaker": "Alice", "target": "Bob"}]
    turn, character, target, utterance, round_completed = game_logic.update_game(script)

    assert turn == 0
    assert character == "Alice"
    assert target == "Bob"
    assert utterance == "Hello, Bob!"
    assert not round_completed
    mock_continue_conversation.assert_called_once_with(script)


def test_is_game_over(game_logic):
    assert not game_logic.is_game_over()
    game_logic.game_state.current_turn = 5
    assert game_logic.is_game_over()
