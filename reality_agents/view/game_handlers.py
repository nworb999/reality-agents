from reality_agents.api.horse_race.controller import (
    GameController as HorseGameController,
)
from reality_agents.view.terminal_output import display_progress, display_winners
import time


def play_horse_race_game(num_players_input):
    num_players = int(num_players_input) if num_players_input else 2
    game_controller = HorseGameController(num_players)

    print(game_controller.start_game()["message"])

    round_counter = 0

    while True:
        for current_player in range(1, num_players + 1):
            _ = game_controller.update()

            if current_player == num_players:
                round_completed = True
            else:
                round_completed = False
            if round_completed:
                winners = game_controller.game_service.game.check_winners()
                if winners:
                    display_progress(*progress)
                    display_winners(winners)
                    return

                progress = game_controller.game_service.game.progress
                round_counter += 1
                display_progress(*progress)
                print("\n")

            time.sleep(1)
