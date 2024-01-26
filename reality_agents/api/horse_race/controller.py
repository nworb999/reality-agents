from reality_agents.services.horse_race.game_service import (
    HorseRaceService as GameService,
)

# handles game logic


class GameController:
    def __init__(self, num_players=2):
        self.game_service = GameService(num_players)

    def start_game(self):
        return {"message": self.game_service.start_game()}

    def play_round(self):
        return self.game_service.play_round()
