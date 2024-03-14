# import pytest
# from unittest.mock import MagicMock

# from reality_agents.api.controller import GameController

# # Mock the GameService class
# class MockGameService:
#     def __init__(self, db, characters, conflict, scene):
#         pass

#     def start_game(self):
#         return "Game started"

#     def update(self):
#         return {"status": "Game in progress"}

# # Fixture to create a GameController instance with mocked dependencies
# @pytest.fixture
# def game_controller():
#     db = MagicMock()
#     characters = MagicMock()
#     conflict = MagicMock()
#     scene = MagicMock()
#     game_service = MockGameService(db, characters, conflict, scene)
#     return GameController(db, characters, conflict, scene)

# # Test the start_game method
# def test_start_game(game_controller):
#     response = game_controller.start_game()
#     assert response == {"message": "Game started"}

# # Test the update method when the game is in progress
# def test_update_game_in_progress(game_controller):
#     response = game_controller.update()
#     assert response == {"message": {"status": "Game in progress"}}

# # Test the update method when the game is over (conversation ended)
# def test_update_game_over_conversation_ended(game_controller):
#     game_controller.game_service.update = MagicMock(return_value={"status": "Game over: conversation ended"})
#     response = game_controller.update()
#     assert response == {"message": "Game over: conversation ended"}

# # Test the update method when the game is over (cutoff reached)
# def test_update_game_over_cutoff_reached(game_controller):
#     game_controller.game_service.update = MagicMock(return_value={"status": "Game over: cutoff reached"})
#     response = game_controller.update()
#     assert response == {"message": "Game over: cutoff reached"}
