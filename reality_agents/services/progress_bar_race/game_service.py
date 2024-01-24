from reality_agents.domain.progress_bar_race.game_logic import ProgressBarRaceLogic as GameLogic

class ProgressBarRaceService:
    def __init__(self):
        self.game = None # replace with gamestate?

    def start_game(self):
        self.game = GameLogic()

        self.game.reset_game()
        return "New game started. Player 1 goes first."

    def play_turn(self, player_number):
        self.game.update_progress(player_number)
        return self.game.check_winner()