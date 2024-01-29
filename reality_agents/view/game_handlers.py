from reality_agents.api.horse_race.controller import (
    GameController as HorseGameController,
)
from reality_agents.api.conversation.controller import (
    GameController as ConversationGameController,
)
from reality_agents.view.utils import assign_characters_to_sides, get_player_info
from reality_agents.view.terminal_output import (
    display_progress,
    display_winners,
    display_dialogue,
)
import time


# conversation game
def play_conversation_game():
    scene = input("Enter a setting: ") or "auto shop"
    characters = get_player_info()
    if not characters:
        return

    num_characters = len(characters)
    character_positions = assign_characters_to_sides(num_characters)
    conversation_game_controller = ConversationGameController(characters, scene)
    print(conversation_game_controller.start_game()["message"])

    round_counter = 0

    while True:
        for current_character in range(1, len(characters) + 1):
            response = conversation_game_controller.update()["message"]

            if current_character == num_characters:  # keep round logic just in case
                round_completed = True
            else:
                round_completed = False
            if "FINISHED" in response:
                # winners = conversation_game_controller.game_service.game.finish_game() # too many layers exposed here!
                round_counter += 1
                print("\nTHE END\n")
                return
            else:
                display_dialogue(
                    current_character,
                    response,
                    character_positions[current_character - 1],
                )

            time.sleep(1)


# horse race game
# TODO fix for more than 2


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
