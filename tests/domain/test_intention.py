# import pytest
# from unittest.mock import patch

# from reality_agents.domain.intention import Intention, check_response

# # Mock external dependencies
# @pytest.fixture(autouse=True)
# def mock_external_dependencies():
#     with patch("reality_agents.services.llm.get_response", return_value="Some response"):
#         yield

# # Fixture to create an Intention instance
# @pytest.fixture
# def intention():
#     persona = "Assertive"
#     return Intention(persona)

# # Test the initialize_objective method
# def test_initialize_objective(intention):
#     intention.initialize_objective("Happy", "Disagreement", "Friend")
#     assert intention.objective == "Some response"

# # Test the update_objective method
# def test_update_objective(intention):
#     intention.objective = "Objective"
#     intention.update_objective("Disagreement", "Happy", ["Previous dialogue"])
#     assert intention.objective == "Some response"

# # Test the initialize_intention method
# def test_initialize_intention(intention):
#     intention.initialize_intention("Disagreement", "Happy")
#     assert intention.intention == "Some response"

# # Test the update_intention method
# def test_update_intention(intention):
#     intention.objective = "Objective"
#     intention.update_intention("Disagreement", "Happy", ["Previous dialogue"])
#     assert intention.intention == "Some response"

# # Test the is_ending_conversation method
# def test_is_ending_conversation(intention):
#     intention.intention = "END CONVERSATION"
#     assert intention.is_ending_conversation()

# # Test the check_response function
# @pytest.mark.parametrize("input_string, expected_output", [
#     ("yes", "Yes"),
#     ("no", "No"),
#     ("maybe", "The sentence does not start with Yes or No."),
# ])
# def test_check_response(input_string, expected_output):
#     assert check_response(input_string) == expected_output
