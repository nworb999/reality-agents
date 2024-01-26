from reality_agents.domain.horse_race.game_logic import (
    HorseRaceLogic as GameLogic,
)


class HorseRaceService:
    def __init__(self, num_players):
        self.game = GameLogic(num_players)  # replace with gamestate?

    def start_game(self):
        self.game.reset_game()
        return f"New game started. Player 1 goes first."

    def play_round(self):
        winner = self.game.play_turn()  # i think i need this up there
        if winner:
            return {"message": f"Player {winner} wins!", "winner": winner}
        else:
            next_player = self.game.current_turn + 1
            return {"message": f"Player's turn completed. Player {next_player}'s turn."}

