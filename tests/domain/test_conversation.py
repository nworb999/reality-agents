import pytest
from reality_agents.domain.conversation.conversation import (
    ConversationLogic,
    SpeakingOrderLogic,
)  # Adjust the import path according to your project structure


class MockCharacter:
    def __init__(self, name, conversation):
        self.name = name
        self.conversation = conversation


@pytest.fixture
def characters():
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]


@pytest.fixture
def script():
    return [
        {"dialogue": "Hello, how are you?"},
        {"dialogue": "I'm good, thanks!"},
        {"dialogue": "That's great to hear."},
    ]


@pytest.fixture
def conversation_logic(characters):
    return ConversationLogic(characters=characters)


def test_conversation_logic_initialization(conversation_logic, characters):
    assert conversation_logic.characters == characters
    assert conversation_logic.turn == 0
    assert conversation_logic.speaking_turns == [0] * len(characters)
    assert conversation_logic.speaking_order_logic.characters == characters
    assert conversation_logic.speaking_order_logic.order_type == "sequential"


def test_reset_game(conversation_logic):
    conversation_logic.turn = 5
    conversation_logic.speaking_turns = [1, 2, 2]
    conversation_logic.reset_game()
    assert conversation_logic.turn == 0
    assert conversation_logic.speaking_turns == [0, 0, 0]


def test_next_line(conversation_logic, script):
    turn, current_speaker, target, utterance = conversation_logic.next_line(script)
    assert turn == 1
    assert current_speaker == conversation_logic.characters[0]
    assert target == conversation_logic.characters[1]
    assert isinstance(utterance, str)
