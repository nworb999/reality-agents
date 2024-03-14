from reality_agents.api.controller import (
    GameController as ConversationGameController,
)
from reality_agents.view.utils import get_player_info
from reality_agents.view.terminal_output import (
    display_dialogue,
    display_end,
)
from utils.string import THEN_PRESS_ENTER
from utils.ascii import clear_screen, intro_text, spin
import time

# from main import SCENE_CACHE, CONFLICT_CACHE, CHARACTERS_CACHE


def play_conversation_game(db):
    clear_screen()
    intro_text()
    spin()
    print("You are setting up a scene for a reality TV show.")
    spin(2)
    print()
    print("There are two characters.")
    print()
    spin(3)
    scene = (
        input("[1/10] What is the setting? e.g. auto shop" + THEN_PRESS_ENTER)
        or "auto shop"
    )
    # SCENE_CACHE = scene
    spin(1)
    conflict = (
        input("[2/10] What is the conflict? e.g. money" + THEN_PRESS_ENTER)
        or """Money."""
    )
    # CONFLICT_CACHE = conflict
    spin(1)
    characters = get_player_info()
    if not characters:
        return
    # CHARACTERS_CACHE = characters
    conversation_game_controller = ConversationGameController(
        db, characters, conflict, scene
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
            if response == "Game over: cutoff reached":
                print("GAME OVER: CUTOFF REACHED")
                game_finished = True
                break
            if response == "Game over: conversation ended":
                display_end()
                game_finished = True
                break
            display_dialogue(
                current_character,
                characters[current_character]["name"],
                response["dialogue"],
            )
            round_counter += 1
            spin(1)
