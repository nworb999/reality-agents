import pytest
from unittest.mock import patch
from reality_agents.domain.game_logic import GameLogic, ConversationManager


@pytest.fixture
def game_logic():
    characters = [
        {"name": "Alice", "personality": "Friendly"},
        {"name": "Bob", "personality": "Serious"},
    ]
    return GameLogic(characters, max_rounds=5)


def test_reset_game(game_logic):
    game_logic.reset_game()
    assert game_logic.current_character == 0
    assert game_logic.current_round == 0


@patch.object(
    ConversationManager,
    "next_line",
    return_value=(1, {"name": "Alice"}, {"name": "Bob"}, "Hello, Bob!"),
)
def test_play_turn(mock_next_line, game_logic):
    script = [{"dialogue": "Hi, Alice!"}]
    turn, current_character, target, utterance, round_completed = game_logic.play_turn(
        script
    )
    assert turn == 1
    assert current_character == {"name": "Alice"}
    assert target == {"name": "Bob"}
    assert utterance == "Hello, Bob!"
    assert not round_completed
    mock_next_line.assert_called_once_with(script)


def test_is_game_over(game_logic):
    game_logic.current_round = 5
    assert game_logic.is_game_over()
    game_logic.current_round = 4
    assert not game_logic.is_game_over()
