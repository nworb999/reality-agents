from reality_agents.services.game.game_service import (
    ConversationService as GameService,
)

# handles game logic
# return messages with status codes for when it's FINISHED


class GameController:
    def __init__(self, db, characters, conflict, scene, test_flag=False):
        self.game_service = GameService(
            db, characters, conflict, scene, test_flag=test_flag
        )

    def start_game(self):
        response = self.game_service.start_game()
        return {"message": response}

    def update(self):
        game_status = self.game_service.update()
        if game_status["status"] == "Game over: conversation ended":
            return {"message": "Game over: conversation ended"}
        if game_status["status"] == "Game over: cutoff reached":
            return {"message": "Game over: cutoff reached"}
        return {"message": game_status}
