from reality_agents.api.controller import (
    GameController as ConversationGameController,
)
from reality_agents.view.utils import (
    get_player_info,
    setup_game,
    get_game_setup,
    start_conversation_game,
)
from reality_agents.view.terminal_output import (
    display_dialogue,
    display_end,
)
from utils.string import THEN_PRESS_ENTER
from utils.ascii import spin


def play_conversation_game(
    db, scene_cache=None, conflict_cache=None, characters_cache=None
):
    setup_game()
    scene, conflict, characters = get_game_setup(
        scene_cache, conflict_cache, characters_cache
    )
    if not characters:
        return

    conversation_game_controller = ConversationGameController(
        db, characters, conflict, scene
    )
    start_conversation_game(conversation_game_controller)
    game_loop(conversation_game_controller, characters)


def game_loop(conversation_game_controller, characters):
    round_counter = 0
    game_finished = False

    while not game_finished:
        for current_character in range(len(characters)):
            response = process_character_turn(
                conversation_game_controller, current_character, characters
            )
            if response in [
                "Game over: cutoff reached",
                "Game over: conversation ended",
            ]:
                game_finished = True
                break
            round_counter += 1


def process_character_turn(conversation_game_controller, current_character, characters):
    full_response = conversation_game_controller.update()
    response = full_response["message"]
    if response == "Game over: cutoff reached":
        print("GAME OVER: CUTOFF REACHED")
    elif response == "Game over: conversation ended":
        display_end()
    else:
        display_dialogue(
            current_character,
            characters[current_character]["name"],
            response["dialogue"],
        )
    spin(1)
    return response
