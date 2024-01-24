from reality_agents.api.progress_bar_race.controller import GameController as ProgressBarGameController
import sys

def main():
    game_type = input("Please enter the game type: ")

    if game_type.lower() == "progress bar":

        game_controller = ProgressBarGameController()

        print(game_controller.start_game()['message'])

        while True:
            player_input = input("Enter player number to roll (1 or 2), or 'quit' to exit: ")
            
            if player_input.lower() == 'quit':
                print("Game ended.")
                break
            
            try:
                player_number = int(player_input)

                response = game_controller.play_turn(player_number)
                print(response['message'])

                if 'wins' in response['message']:
                    break
                
            except ValueError:
                print("Please enter a valid player number (1 or 2) or 'quit' to exit.")
    else:
        print("Unknown game type. Exiting.")

if __name__ == "__main__":
    main()
