from reality_agents.api.horse_race.controller import (
    GameController as HorseGameController,
)
from reality_agents.view.horse_race.terminal_output import (
    display_progress,
    display_winners,
)
import time


def play_horse_race_game():
    num_players_input = input("Enter the number of players: ")
    num_players = int(num_players_input) if num_players_input else 2
    horse_race_controller = HorseGameController(num_players)

    print(horse_race_controller.start_game()["message"])

    round_counter = 0

    while True:
        for current_player in range(1, num_players + 1):
            _ = horse_race_controller.update()

            if current_player == num_players:
                round_completed = True
            else:
                round_completed = False
            if round_completed:
                winners = (
                    horse_race_controller.game_service.game.finish_game()
                )  # too many layers exposed here
                if winners:
                    display_progress(*progress)
                    display_winners(winners)
                    return

                progress = (
                    horse_race_controller.game_service.game.progress
                )  # put this on the controller instead of going all the way through the layers
                round_counter += 1
                display_progress(*progress)
                print("\n")

            time.sleep(1)
