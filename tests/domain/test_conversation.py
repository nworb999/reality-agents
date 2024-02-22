import pytest
from reality_agents.domain.conversation.conversation import (
    ConversationLogic,
    SpeakingOrderLogic,
)  # Adjust the import path according to your project structure


class MockCharacter:
    def __init__(self, name):
        self.name = name


@pytest.fixture
def conversation_logic():
    characters = [MockCharacter("Alice"), MockCharacter("Bob")]
    return ConversationLogic(characters, order_type="sequential")


def test_speaking_order_initialization(conversation_logic):
    assert conversation_logic.speaking_order_logic.order == [0, 1]


def test_play_turn_sequential(conversation_logic):
    utterance, round_completed = conversation_logic.play_turn()

    # Check utterance
    assert utterance == "Alice spoke"
    assert not round_completed

    # Second call to play_turn
    utterance, round_completed = conversation_logic.play_turn()
    assert utterance == "Bob spoke"
    assert round_completed


def test_reset_game(conversation_logic):
    # Simulate a few turns
    conversation_logic.play_turn()
    conversation_logic.play_turn()

    conversation_logic.reset_game()

    # Check if the game is reset properly
    assert conversation_logic.speaking_turns == [0, 0]
    assert conversation_logic.speaking_order_logic.current_turn == 0
    assert conversation_logic.speaking_order_logic.order == [0, 1]


@pytest.fixture
def conversation_logic_random():
    characters = [MockCharacter("Alice"), MockCharacter("Bob")]
    return ConversationLogic(characters, order_type="random")


def test_speaking_order_random(conversation_logic_random):
    first_speaker = conversation_logic_random.speaking_order_logic.next_speaker()
    assert first_speaker in [0, 1]

    second_speaker = conversation_logic_random.speaking_order_logic.next_speaker()
    # In random mode, the same speaker could be selected again
    assert second_speaker in [0, 1]
