from reality_agents.domain.game_state import GameState
import reality_agents.services.cli_services

class GameServer:
    def __init__(self):
        self.game_state = GameState()

    def start_game(self):
        self.game_state.start()
        self.run_game_loop()

    def run_game_loop(self):
        # Here you would have the loop that calls the game state update
        self.game_state.update(cli_services)

    def shutdown(self):
        # Perform any cleanup necessary for shutting down the server
        pass
