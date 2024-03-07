import random
import time
from utils.string import THEN_PRESS_ENTER
from utils.ascii import spin


def slow_type(text, delay=0.1):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def create_player(name, pronouns=None, personality=None, relationship_to_target=None):
    player = {"name": name}
    if pronouns:
        player["pronouns"] = pronouns
    if personality:
        player["personality"] = personality
    if relationship_to_target:
        player["relationship_to_target"] = relationship_to_target
    return player


def collect_player_info(player_number):
    name = input(
        f"What is the name of character {player_number}?" + THEN_PRESS_ENTER
    ).strip()
    spin(1)
    if name.lower() == "test":
        return None  # Signal to use default players
    pronouns = input(f"What are {name}'s pronouns?" + THEN_PRESS_ENTER).strip()
    spin(1)
    personality = input(f"What is {name}'s personality?" + THEN_PRESS_ENTER).strip()
    spin(1)
    return create_player(name, pronouns, personality)


def get_player_info():
    players = []
    default_players = [
        create_player(
            "Mark",
            "he/him",
            "a bit of a hothead, but passionate and kind",
            "He is Billy' son, and he thinks Billy is too old to make decisions and is losing his touch.  He calls Billy dad.",
        ),
        create_player(
            "Billy",
            "he/him",
            "cool, calm, and collected, but a schemer",
            "He is Mark's 70-year-old dad and the owner of the shop. He thinks Mark is too rash and emotionally unstable to make decisions.",
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
