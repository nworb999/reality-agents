import pytest
from reality_agents.api.horse_race.controller import GameController
from reality_agents.services.game.horse_race.game_service import HorseRaceService


@pytest.fixture
def game_controller(mocker):
    mocker.patch(
        "reality_agents.services.game.horse_race.game_service.HorseRaceService"
    )
    return GameController(num_players=2)


def test_start_game(game_controller, mocker):
    mocked_start_game = mocker.patch.object(
        HorseRaceService, "start_game", return_value="Game started"
    )
    response = game_controller.start_game()
    mocked_start_game.assert_called_once()
    assert response == {"message": "Game started"}


def test_update(game_controller, mocker):
    mocked_update = mocker.patch.object(
        HorseRaceService, "update", return_value="Round played"
    )
    response = game_controller.update()
    mocked_update.assert_called_once()
    assert response == "Round played"
