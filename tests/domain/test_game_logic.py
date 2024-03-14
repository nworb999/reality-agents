# import pytest
# from reality_agents.domain.game_logic import GameLogic, GameState

# # Fixture to create a GameLogic instance
# @pytest.fixture
# def game_logic():
#     characters = [{"name": "Alice"}, {"name": "Bob"}]
#     conflict = "Disagreement"
#     scene = "Park"
#     return GameLogic(characters, conflict, scene)

# # Test the reset_game method
# def test_reset_game(game_logic):
#     game_logic.reset_game()
#     assert game_logic.game_state.conversation_index == 1
#     assert game_logic.game_state.turn == 0

# # Test the update_game method
# def test_update_game(game_logic):
#     script = [{"character": "Alice", "dialogue": "Hello, Bob!"}]
#     current_turn, current_character, target, utterance, round_completed = game_logic.update_game(script)
#     assert current_turn == 1
#     assert current_character["name"] == "Bob"
#     assert target["name"] == "Alice"
#     assert utterance is None
#     assert not round_completed

# # Test the is_game_over method
# def test_is_game_over(game_logic):
#     assert not game_logic.is_game_over()
#     game_logic.game_state.max_turns = 0  # Force game over
#     assert game_logic.is_game_over()
