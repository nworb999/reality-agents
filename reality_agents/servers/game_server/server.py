from reality_agents.domain.game_state import GameState
from reality_agents.services import cli_service

class GameServer:
    def __init__(self):
        self.game_state = GameState()

    def start_game(self):
        self.game_state.start()
        self.run_game_loop()

    def run_game_loop(self):
        # Here you would have the loop that calls the game state update
        self.game_state.update()

    def shutdown(self):
        # Perform any cleanup necessary for shutting down the server
        pass
