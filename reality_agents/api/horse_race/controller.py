from reality_agents.services.game.horse_race.game_service import (
    HorseRaceService as GameService,
)

# handles game logic at very high level


class GameController:
    def __init__(self, num_players):
        self.game_service = GameService(num_players)

    def start_game(self):
        return {"message": self.game_service.start_game()}

    def update(self):
        return self.game_service.update()
