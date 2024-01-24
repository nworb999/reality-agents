from reality_agents.services.progress_bar_race.game_service import ProgressBarRace as GameService

# handles game logic

class GameController:
    def __init__(self):
        self.game_service = GameService()

    def start_game(self):
        return {"message":  self.game_service.start_game()}

    def play_turn(self, player_number):
        winner = self.game_service.play_turn(player_number)
        if winner:
            return {"message": f"Player {winner} wins!"}
        else:
            return {"message": f"Player {player_number} has rolled. Next player's turn."}
