from reality_agents.api.controller import (
    GameController as ConversationGameController,
)
from reality_agents.services.llm.cuttlefish_mode import generate_cuttlefish_scenario
from reality_agents.view.utils import (
    get_player_info,
    game_setup_ascii,
    get_game_setup,
    start_conversation_game,
)
from reality_agents.view.terminal_output import (
    display_dialogue,
    display_end,
)
from utils.ascii import spin


def play_conversation_game(
    scene_cache=None,
    conflict_cache=None,
    characters_cache=None,
    test_flag=False,
    cuttlefish_flag=False,
):
    if not test_flag:
        game_setup_ascii()
    if not cuttlefish_flag:
        scene, conflict, characters = get_game_setup(
            scene_cache, conflict_cache, characters_cache, test_flag
        )
        if not characters:
            return
        conversation_game_controller = ConversationGameController(
            characters, conflict, scene, test_flag
        )
        start_conversation_game(conversation_game_controller)
        game_loop(conversation_game_controller, characters)
    else:
        infinite_game_loop(cuttlefish_flag)


def infinite_game_loop(cuttlefish_flag):
    game_count = 0
    scene, conflict, characters = generate_cuttlefish_scenario()
    conversation_game_controller = ConversationGameController(
        characters, conflict, scene, test_flag=True
    )
    while cuttlefish_flag:
        game_count += 1
        if game_count > 1:
            (
                scene,
                conflict,
                characters,
            ) = (
                generate_cuttlefish_scenario()
            )  # Refresh the scenario for each new game iteration
            conversation_game_controller.reset(
                scene, conflict, characters
            )  # Method to reset the game controller with new settings
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
                    print("Game status:", response)
                    game_finished = True
                    break


def game_loop(conversation_game_controller, characters, cuttlefish_flag):
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
                print("game status", response)
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
