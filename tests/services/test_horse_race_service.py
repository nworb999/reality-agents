import pytest
from reality_agents.domain.horse_race.game_logic import HorseRaceLogic
from reality_agents.services.horse_race.game_service import HorseRaceService


@pytest.fixture
def horse_race_service(mocker):
    mocker.patch("reality_agents.domain.horse_race.game_logic.HorseRaceLogic")
    return HorseRaceService(num_players=2)


def test_start_game(horse_race_service, mocker):
    mocked_reset_game = mocker.patch.object(HorseRaceLogic, "reset_game")
    horse_race_service.start_game()
    mocked_reset_game.assert_called_once()


def test_update_no_winner(horse_race_service, mocker):
    mocker.patch.object(HorseRaceLogic, "play_turn", return_value=(None, False))
    response = horse_race_service.update()
    assert "Player's turn completed" in response["message"]


def test_update_with_winner(horse_race_service, mocker):
    mocker.patch.object(HorseRaceLogic, "play_turn", return_value=(1, True))
    response = horse_race_service.update()
    assert "Player 1 wins" in response["message"]
