import random
import time
from utils.constants import SCENE_DEFAULT, CONFLICT_DEFAULT, EMOJI_LIST, DEFAULT_PLAYERS
from utils.string import THEN_PRESS_ENTER
from utils.ascii import clear_screen, intro_text, spin


def game_setup_ascii():
    clear_screen()
    intro_text()
    spin()
    print("You are setting up a scene for a reality TV show.")
    spin(2)
    print("\nThere are two characters.\n")
    spin(3)


def get_game_setup(scene_cache, conflict_cache, characters_cache, test_flag=None):
    if test_flag:
        scene = SCENE_DEFAULT
        conflict = CONFLICT_DEFAULT
        characters = DEFAULT_PLAYERS
    else:
        scene = scene_cache or get_input_with_default(
            "Where do they work? e.g. auto shop", SCENE_DEFAULT
        )
        conflict = conflict_cache or get_input_with_default(
            "What is the conflict? e.g. money", CONFLICT_DEFAULT
        )
        characters = characters_cache or get_player_info(test_flag)
    return scene, conflict, characters


def get_input_with_default(prompt, default_value):
    return input(f"{prompt}{THEN_PRESS_ENTER}") or default_value


def start_conversation_game(conversation_game_controller):
    conversation_game_controller.start_game()
    clear_screen()
    intro_text()
    print("\n\n")


def slow_type(text, delay=0.1):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def create_player(name, personality=None, relationship_to_target=None):
    player = {"name": name}
    if personality:
        player["personality"] = personality
    if relationship_to_target:
        player["relationship_to_target"] = relationship_to_target
    return player


def set_relationships_between_players(players, test_flag=False):
    for i in range(len(players)):
        target = (i + 1) % len(players)
        relation = input(
            f"How does {players[i]['name']} feel about {players[target]['name']}?"
            + THEN_PRESS_ENTER
        ).strip()
        if not test_flag:
            spin(1)
        if not relation:
            relation = "They are just acquaintances."
        players[i]["relationship_to_target"] = relation
    return players


def collect_player_info(player_number):
    ordinal_dict = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth"}
    ordinal = ordinal_dict.get(player_number, str(player_number) + "th")

    name = input(
        f"What is the name of the {ordinal} character?" + THEN_PRESS_ENTER
    ).strip()
    spin(1)
    if name.lower() == "test":
        return None  # Signal to use default players
    personality = input(f"What is {name}'s personality?" + THEN_PRESS_ENTER).strip()
    spin(1)
    return create_player(name, personality)


def get_player_info(test_flag=False):
    players = []

    first_player = collect_player_info(1)
    if first_player is None:
        return DEFAULT_PLAYERS

    players.append(first_player)
    second_player = collect_player_info(2)
    players.append(second_player)

    players = set_relationships_between_players(players, test_flag)

    if all(
        player["name"] == ""
        and player["relationship_to_target"] == "They are just acquaintances."
        for player in players
    ):
        players = DEFAULT_PLAYERS

    return players


def get_emoji_by_index(index):
    return EMOJI_LIST[index % len(EMOJI_LIST)]
