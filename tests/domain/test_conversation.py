# import pytest
# from unittest.mock import MagicMock, patch

# from reality_agents.domain.conversation import ConversationManager, check_yes_or_no

# # Mock the get_response function
# @pytest.fixture
# def mock_get_response():
#     with patch("reality_agents.services.llm.ollama_handler.get_response") as mock:
#         yield mock

# # Fixture to create a ConversationManager instance
# @pytest.fixture
# def conversation_manager():
#     characters = [{"name": "Alice", "personality": "Assertive"}, {"name": "Bob", "personality": "Calm"}]
#     scene = "Park"
#     conflict = "Disagreement"
#     return ConversationManager(characters, scene, conflict)

# # Test the next_line method
# def test_next_line(conversation_manager, mock_get_response):
#     mock_get_response.return_value = "Hello, Bob!"
#     turn, current_speaker, target, utterance = conversation_manager.next_line([])

#     assert turn == 1
#     assert current_speaker["name"] == "Alice"
#     assert target["name"] == "Bob"
#     assert utterance == "Hello, Bob!"

# # Test the check_yes_or_no function
# @pytest.mark.parametrize("input_string, expected_output", [
#     ("yes", True),
#     ("no", False),
#     ("not", False),
#     ("maybe", None),
# ])
# def test_check_yes_or_no(input_string, expected_output):
#     assert check_yes_or_no(input_string) == expected_output
