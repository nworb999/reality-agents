# import pytest
# from unittest.mock import patch

# from reality_agents.domain.game_state import GameState, ConversationManager

# # Mock external dependencies
# @pytest.fixture(autouse=True)
# def mock_external_dependencies():
#     with patch("utils.ascii.clear_screen"), patch("utils.ascii.intro_text"):
#         yield

# # Fixture to create a GameState instance
# @pytest.fixture
# def game_state():
#     characters = [{"name": "Alice"}, {"name": "Bob"}]
#     conflict = "Disagreement"
#     scene = "Park"
#     max_turns = 10
#     return GameState(characters, conflict, scene, max_turns)

# # Test the start_new_conversation method
# def test_start_new_conversation(game_state):
#     game_state.start_new_conversation()
#     assert isinstance(game_state.current_conversation, ConversationManager)
#     assert len(game_state.conversations) == 1
#     assert game_state.current_turn == 1

# # Test the end_current_conversation method
# def test_end_current_conversation(game_state):
#     game_state.end_current_conversation()
#     assert len(game_state.conversations) == 1
#     assert game_state.current_conversation is None

# # Test the continue_conversation method
# def test_continue_conversation(game_state):
#     script = [{"character": "Alice", "dialogue": "Hello, Bob!"}]
#     current_turn, current_character, target, utterance = game_state.continue_conversation(script)
#     assert current_turn == 1
#     assert current_character["name"] == "Bob"
#     assert target["name"] == "Alice"
#     assert utterance is not None

# # Test the is_game_over method
# def test_is_game_over(game_state):
#     assert not game_state.is_game_over()
#     game_state.current_conversation.game_over = True
#     assert game_state.is_game_over() == "Game over: conversation ended"
#     game_state.current_conversation.game_over = False
#     game_state.current_turn = game_state.max_turns
#     assert game_state.is_game_over() == "Game over: cutoff reached"
