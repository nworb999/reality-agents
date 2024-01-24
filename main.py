from reality_agents.api.progress_bar_race.controller import (
    GameController as ProgressBarGameController,
)
from reality_agents.view.terminal_output import display_progress, display_winner
import time
import sys


def main():
    game_type = input("Please enter the game type: ")

    if game_type.lower() == "progress bar":
        game_controller = ProgressBarGameController()

        print(game_controller.start_game()["message"])

        current_player = 1

        while True:
            response = game_controller.play_turn(current_player)
            print(response["message"])

            # Display progress here
            # You need to add a method in your game logic to retrieve current progress
            progress1, progress2 = (
                game_controller.game_service.game.progress1,
                game_controller.game_service.game.progress2,
            )
            display_progress(progress1, progress2)

            if "wins" in response["message"]:
                display_winner(response["winner"])
                break

            # Switch player
            current_player = 1 if current_player == 2 else 2

            # Delay for readability
            time.sleep(1)

    else:
        print("Unknown game type. Exiting.")


if __name__ == "__main__":
    main()
