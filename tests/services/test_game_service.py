# import pytest
# from unittest.mock import patch, MagicMock

# from reality_agents.services.game.game_service import ConversationService

# # Mock external dependencies
# @pytest.fixture(autouse=True)
# def mock_external_dependencies():
#     with patch("reality_agents.db.repository.create_memory_entry"):
#         yield

# # Fixture to create a ConversationService instance
# @pytest.fixture
# def conversation_service():
#     db = MagicMock()
#     characters = [
#         {"name": "Alice", "personality": "Assertive", "relationship_to_target": "Friend"},
#         {"name": "Bob", "personality": "Calm", "relationship_to_target": "Stranger"},
#     ]
#     conflict = "Disagreement"
#     scene = "Park"
#     return ConversationService(db, characters, conflict, scene)

# # Test the start_game method
# def test_start_game(conversation_service):
#     message = conversation_service.start_game()
#     assert message == "New game started. Alice goes first."

# # Test the update method
# def test_update(conversation_service):
#     conversation_service.game.is_game_over = MagicMock(return_value=False)
#     turn_data = conversation_service.update()
#     assert turn_data["name"] == "Alice"
#     assert turn_data["turn"] == 1
#     assert turn_data["status"] == "ONGOING"

# # Test the store_data method
# @patch("your_module.create_memory_entry")
# def test_store_data(mock_create_memory_entry, conversation_service):
#     conversation_service.store_data(1, "Alice", "Bob", "Hello, Bob!")
#     mock_create_memory_entry.assert_called_once_with(
#         conversation_service.db,
#         "game 1",
#         "convo 1",
#         "round 1",
#         1,
#         "Alice",
#         "Bob",
#         "Hello, Bob!",
#     )
