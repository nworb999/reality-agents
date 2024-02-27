import pytest
import requests_mock
from unittest.mock import patch
from reality_agents.domain.conversation import SpeakingOrder, ConversationManager


# Test SpeakingOrder class
def test_speaking_order_sequential():
    order = SpeakingOrder(num_characters=3, order_type="sequential")
    assert order.next_speaker_index() == 0
    assert order.next_speaker_index() == 1
    assert order.next_speaker_index() == 2
    assert order.next_speaker_index() == 0  # Loop back to the first speaker


# Test ConversationManager class
@pytest.fixture
def conversation_manager():
    characters = [
        {"name": "Alice", "personality": "Friendly"},
        {"name": "Bob", "personality": "Serious"},
    ]
    return ConversationManager(characters, order_type="sequential")


def test_reset(conversation_manager):
    conversation_manager.reset()
    assert conversation_manager.turn == 0
    assert conversation_manager.speaking_turns == [0, 0]


@patch.object(ConversationManager, "_get_prompt", return_value="Prompt for Alice")
def test_next_line(mock_get_prompt, conversation_manager):
    with requests_mock.Mocker() as m:
        # Mock the POST request
        m.post(
            "http://localhost:12345/api/chat",
            json={"message": {"content": "Hello, Bob!"}},
        )
        script = [{"dialogue": "Hi, Alice!"}]
        turn, current_speaker, target, utterance = conversation_manager.next_line(
            script
        )
        assert turn == 1
        assert current_speaker["name"] == "Alice"
        assert target["name"] == "Bob"
        assert utterance == "Hello, Bob!"
        mock_get_prompt.assert_called_once_with(
            current_speaker,  # Changed from 'character' to match the actual parameter name
            target,  # Changed from 'target' to match the actual parameter name
            "Hi, Alice!",  # Changed from 'prev_statement' to match the actual value
            "start",  # Changed from 'convo_state' to match the actual value
        )
