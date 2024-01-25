from reality_agents.domain.horse_race.game_logic import (
    HorseRaceLogic as GameLogic,
)


class HorseRaceService:
    def __init__(self):
        self.game = None  # replace with gamestate?

    def start_game(self):
        self.game = GameLogic()
        self.game.reset_game()
        return "New game started. Player 1 goes first."

    def play_round(self):
        return self.game.play_round()

    def play_turn(self, player_number):
        self.game.update_progress(player_number)  # i think i need this up there
        return self.game.check_winner()
