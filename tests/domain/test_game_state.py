import pytest
from unittest.mock import patch
from reality_agents.domain.conversation import ConversationManager
from reality_agents.domain.game_state import GameState, DEFAULT_ORDER_TYPE


@pytest.fixture
def characters():
    return [
        {"name": "Alice", "personality": "friendly"},
        {"name": "Bob", "personality": "grumpy"},
    ]


@pytest.fixture
def game_state(characters):
    return GameState(characters=characters)


def test_initialization(game_state, characters):
    assert game_state.characters == characters
    assert game_state.max_turns == 5
    assert isinstance(game_state.current_conversation, ConversationManager)
    assert game_state.current_character == 0
    assert game_state.current_turn == 0
    assert game_state.emotional_states == {
        character["name"]: "neutral" for character in characters
    }


def test_start_new_conversation(game_state):
    game_state.start_new_conversation()
    assert len(game_state.conversations) == 1
    assert isinstance(game_state.current_conversation, ConversationManager)
    assert game_state.current_turn == 1


def test_end_current_conversation(game_state):
    game_state.start_new_conversation()
    game_state.end_current_conversation()
    assert len(game_state.conversations) == 2
    assert game_state.current_conversation is None


@patch("reality_agents.domain.conversation.ConversationManager.next_line")
def test_continue_conversation(mock_next_line, game_state):
    mock_return_value = (0, "Alice", "Bob", "Hello, Bob!")
    mock_next_line.return_value = mock_return_value

    script = [{"dialogue": "Hello, Bob!", "speaker": "Alice", "target": "Bob"}]
    turn, speaker, target, utterance = game_state.continue_conversation(script)

    assert turn == 0
    assert speaker == "Alice"
    assert target == "Bob"
    assert utterance == "Hello, Bob!"
    mock_next_line.assert_called_once_with(script)


def test_update_emotional_state(game_state):
    game_state.update_emotional_state("Alice", "happy")
    assert game_state.emotional_states["Alice"] == "happy"


def test_is_game_over(game_state):
    assert not game_state.is_game_over()
    game_state.current_turn = 5
    assert game_state.is_game_over()


def test_get_emotional_state(game_state):
    assert game_state.get_emotional_state("Alice") == "neutral"
    assert game_state.get_emotional_state("Unknown") == "unknown"
