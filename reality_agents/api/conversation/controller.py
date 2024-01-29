from reality_agents.services.conversation.game_service import (
    ConversationService as GameService,
)

# handles game logic

# return messages with status codes for when it's FINISHED


class GameController:
    def __init__(self, characters, scene):
        self.game_service = GameService(characters, scene)

    def start_game(self):
        return {"message": self.game_service.start_game()}

    def update(self):
        game_status = self.game_service.update()
        if game_status["status"] == "FINISHED":
            return {"message": "FINISHED"}
        return {"message": game_status}