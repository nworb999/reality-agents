import pytest
from reality_agents.domain.horse_race.game_logic import HorseRaceLogic


@pytest.fixture
def game_logic():
    return HorseRaceLogic(num_players=2)


def test_initial_progress(game_logic):
    assert game_logic.progress == [0, 0]


def test_reset_game(game_logic):
    game_logic.progress = [10, 20]
    game_logic.current_turn = 1
    game_logic.round_values = [15, 15]

    game_logic.reset_game()

    assert game_logic.progress == [0, 0]
    assert game_logic.current_turn == 0
    assert game_logic.round_values == [0, 0]


def test_play_turn(game_logic):
    # Store the current player before playing the turn
    current_player_before_turn = game_logic.current_turn

    _, round_completed = game_logic.play_turn()

    # Check if the round value for the player who just played is updated correctly
    assert game_logic.round_values[current_player_before_turn] in range(5, 15)

    # Check round completion status
    if current_player_before_turn == game_logic.num_players - 1:
        assert round_completed
    else:
        assert not round_completed


def test_update_progress(game_logic):
    # Set up initial conditions
    game_logic.round_values = [15, 15]
    game_logic.update_progress()

    # Check if the progress is updated correctly
    assert game_logic.progress == [15, 15]


def test_finish_game_no_winner(game_logic):
    # Expect an empty list or None when there are no winners
    assert game_logic.finish_game() in [None, []]


def test_finish_game_with_single_winner(game_logic):
    # Set up the game state so that only one player has won
    game_logic.progress = [100, 50]
    winners = game_logic.finish_game()

    # Expect a list with a single winner
    assert winners == [1]


def test_finish_game_with_multiple_winners(game_logic):
    # Set up the game state so that multiple players have won
    game_logic.progress = [100, 100, 50]
    winners = game_logic.finish_game()

    # Expect a list with multiple winners
    assert winners == [1, 2]
