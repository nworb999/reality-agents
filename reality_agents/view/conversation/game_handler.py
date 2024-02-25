from reality_agents.api.conversation.controller import (
    GameController as ConversationGameController,
)
from reality_agents.view.utils import get_player_info
from reality_agents.view.conversation.terminal_output import (
    display_dialogue,
    display_end,
)
from utils.ascii import clear_screen, intro_text, spin
import time


def play_conversation_game(db):
    scene = input("Enter a setting: ") or "auto shop"
    characters = get_player_info()
    if not characters:
        return

    conversation_game_controller = ConversationGameController(db, characters, scene)

    round_counter = 0
    clear_screen()
    intro_text()
    print("\n\n")

    while round_counter < 10:
        for current_character in range(len(characters)):
            full_response = conversation_game_controller.update()
            response = full_response["message"]

            display_dialogue(
                current_character,
                characters[current_character]["name"],
                response["dialogue"],
            )
            round_counter += 1
            time.sleep(1)

    display_end()
