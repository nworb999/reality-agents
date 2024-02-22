import pytest
from reality_agents.api.conversation.controller import GameController
from reality_agents.services.game.conversation.game_service import ConversationService


@pytest.fixture
def game_controller(mocker):
    characters = [
        {"name": "Character1", "personality": "Personality1"},
        {"name": "Character2", "personality": "Personality2"},
    ]
    scene = "Scene1"
    mocker.patch(
        "reality_agents.services.game.conversation.game_service.ConversationService"
    )
    return GameController(characters, scene)


def test_start_game(game_controller, mocker):
    mocked_start_game = mocker.patch.object(
        ConversationService, "start_game", return_value="Game started"
    )
    response = game_controller.start_game()
    mocked_start_game.assert_called_once()
    assert response == {"message": "Game started"}


def test_update_finished(game_controller, mocker):
    mocked_update = mocker.patch.object(
        ConversationService, "update", return_value={"status": "FINISHED"}
    )
    response = game_controller.update()
    mocked_update.assert_called_once()
    assert response == {"message": "FINISHED"}


def test_update_ongoing(game_controller, mocker):
    game_status = {"status": "ONGOING", "details": "Game continues"}
    mocked_update = mocker.patch.object(
        ConversationService, "update", return_value=game_status
    )
    response = game_controller.update()
    mocked_update.assert_called_once()
    assert response == {"message": game_status}
