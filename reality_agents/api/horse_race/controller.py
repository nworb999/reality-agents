from reality_agents.services.horse_race.game_service import (
    HorseRaceService as GameService,
)

# handles game logic at very high level


class GameController:
    def __init__(self, characters):
        self.game_service = GameService(characters)

    def start_game(self):
        return {"message": self.game_service.start_game()}

    def update(self):
        return self.game_service.update()
