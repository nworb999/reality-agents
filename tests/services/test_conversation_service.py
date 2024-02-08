import pytest
from reality_agents.domain.conversation.game_logic import (
    GameLogic,
)
from reality_agents.domain.conversation.character import Character
from reality_agents.domain.conversation.scene import Scene
from reality_agents.services.game.conversation.game_service import ConversationService


@pytest.fixture
def conversation_service(mocker):
    characters = [
        {"name": "Alice", "personality": "Curious"},
        {"name": "Bob", "personality": "Calm"},
    ]
    scene = "A quiet garden"

    # Mock dependencies
    mocker.patch("reality_agents.domain.conversation.game_logic.GameLogic")
    mocker.patch("reality_agents.domain.conversation.character.Character")
    mocker.patch("reality_agents.domain.conversation.scene.Scene")

    # Use real instances for simplicity, but could be further mocked if necessary
    Character.side_effect = lambda name, personality: mocker.Mock(
        name=name, personality=personality
    )
    Scene.return_value = mocker.Mock(description=scene)

    return ConversationService(characters, scene)


def test_start_game(conversation_service, mocker):
    mocked_reset_game = mocker.patch.object(GameLogic, "reset_game")
    response = conversation_service.start_game()
    mocked_reset_game.assert_called_once()
    assert "New game started. Alice goes first." in response


def test_update_game_ongoing(conversation_service, mocker):
    # Assuming play_turn returns current_turn index and round_completed boolean
    mocked_play_turn = mocker.patch.object(
        GameLogic, "play_turn", return_value=(0, False)
    )
    mocked_is_game_over = mocker.patch.object(
        GameLogic, "is_game_over", return_value=False
    )

    response = conversation_service.update()

    assert response["status"] == "ONGOING"
    assert response["name"] == "Alice"
    assert response["dialogue"] == "spoke"
    assert not response["round_completed"]
    mocked_play_turn.assert_called_once()
    mocked_is_game_over.assert_called_once()


def test_update_game_finished(conversation_service, mocker):
    mocker.patch.object(GameLogic, "is_game_over", return_value=True)

    response = conversation_service.update()

    assert response == {"status": "FINISHED"}
