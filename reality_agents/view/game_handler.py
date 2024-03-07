from reality_agents.api.controller import (
    GameController as ConversationGameController,
)
from reality_agents.view.utils import get_player_info
from reality_agents.view.terminal_output import (
    display_dialogue,
    display_end,
)
from utils.ascii import clear_screen, intro_text
import time


def play_conversation_game(db):
    scene = input("Enter a setting: ") or "auto shop"
    situation = (
        input("Enter a situation: ")
        or """The characters work in an auto shop. They are discussing a tough fix on a customer's classic car."""
    )
    characters = get_player_info()
    if not characters:
        return

    conversation_game_controller = ConversationGameController(
        db, characters, situation, scene
    )
    conversation_game_controller.start_game()

    round_counter = 0
    clear_screen()
    intro_text()
    print("\n\n")

    game_finished = False

    while not game_finished:
        for current_character in range(len(characters)):
            full_response = conversation_game_controller.update()

            response = full_response["message"]
            if response == "FINISHED":
                display_end()
                game_finished = True
                break
            display_dialogue(
                current_character,
                characters[current_character]["name"],
                response["dialogue"],
            )
            round_counter += 1
            time.sleep(1)
