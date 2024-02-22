import pytest
from reality_agents.domain.conversation.game_logic import (
    GameLogic,
)  # Adjust the import path according to your project structure


@pytest.fixture
def game_logic():
    characters = ["Alice", "Bob"]  # Example characters
    return GameLogic(characters)


def test_reset_game(game_logic):
    # Simulate some game activity
    for _ in range(3):
        game_logic.play_turn()
    game_logic.reset_game()

    # Assert reset state
    assert game_logic.current_turn == 0
    assert game_logic.current_round == 0
    assert all(turn == 0 for turn in game_logic.speaking_turns)


def test_play_turn(game_logic):
    # Play one turn
    current_turn, round_completed = game_logic.play_turn()

    # Assert correct turn and round not completed
    assert current_turn == 1
    assert not round_completed
    assert game_logic.speaking_turns == [1, 0]

    # Play another turn to complete a round
    current_turn, round_completed = game_logic.play_turn()

    # Assert round completed and turns updated
    assert current_turn == 0
    assert round_completed
    assert game_logic.speaking_turns == [1, 1]
    assert game_logic.current_round == 1


def test_is_game_over_not_over(game_logic):
    # Game should not be over immediately
    assert not game_logic.is_game_over()

    # Simulate playing until just before game over
    for _ in range(game_logic.max_rounds * len(game_logic.characters) - 1):
        game_logic.play_turn()

    # Game should still not be over
    assert not game_logic.is_game_over()


def test_is_game_over(game_logic):
    # Simulate playing through max rounds
    for _ in range(game_logic.max_rounds * len(game_logic.characters)):
        game_logic.play_turn()

    # Game should be over
    assert game_logic.is_game_over()
