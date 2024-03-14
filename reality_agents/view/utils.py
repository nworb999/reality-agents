import random
import time
from utils.string import THEN_PRESS_ENTER
from utils.ascii import clear_screen, intro_text, spin


def setup_game():
    clear_screen()
    intro_text()
    spin()
    print("You are setting up a scene for a reality TV show.")
    spin(2)
    print("\nThere are two characters.\n")
    spin(3)


def get_game_setup(scene_cache, conflict_cache, characters_cache):
    scene = scene_cache or get_input_with_default(
        "Where do they work? e.g. auto shop", "auto shop"
    )
    conflict = conflict_cache or get_input_with_default(
        "What is the conflict? e.g. money", "money."
    )
    characters = characters_cache or get_player_info()
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


def get_player_info():
    players = []
    default_players = [
        create_player(
            "Mark",
            "hothead",
            "He calls Billy dad. He thinks he's too old to run things.",
        ),
        create_player(
            "Billy",
            "calm, but a schemer",
            "He thinks Mark is too rash and emotionally unstable to make decisions.",
        ),
    ]

    first_player = collect_player_info(1)
    if first_player is None:
        return default_players

    players.append(first_player)
    second_player = collect_player_info(2)
    players.append(second_player)

    for i in range(2):
        target = (i + 1) % 2
        relation = input(
            f"How does {players[i]['name']} feel about {players[target]['name']}?"
            + THEN_PRESS_ENTER
        ).strip()
        spin(1)
        if not relation:
            relation = "They are just acquaintances."
        players[i]["relationship_to_target"] = relation

    if all(
        player["name"] == ""
        and player["relationship_to_target"] == "They are just acquaintances."
        for player in players
    ):
        players = default_players

    return players


ANIMAL_EMOJIS = {
    "dog": "🐶",
    "cat": "🐱",
    "mouse": "🐭",
    "fox": "🦊",
    "bear": "🐻",
    "panda": "🐼",
    "lion": "🦁",
    "tiger": "🐯",
    "wolf": "🐺",
    "frog": "🐸",
    "cow": "🐮",
    "rabbit": "🐰",
    "pig": "🐷",
    "chicken": "🐔",
    "penguin": "🐧",
    "koala": "🐨",
}

EMOJI_LIST = random.sample(list(ANIMAL_EMOJIS.values()), k=len(ANIMAL_EMOJIS))


def get_emoji_by_index(index):
    return EMOJI_LIST[index % len(EMOJI_LIST)]


def assign_characters_to_sides(num_characters):
    character_indices = list(range(num_characters))
    random.shuffle(character_indices)

    half_size = len(character_indices) // 2
    left_side_indices = character_indices[:half_size]
    right_side_indices = character_indices[half_size:]

    character_sides = {index: "left" for index in left_side_indices}
    character_sides.update({index: "right" for index in right_side_indices})

    return character_sides
