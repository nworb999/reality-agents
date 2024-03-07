import random
import time


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
    name = input(f"What is the name of character {player_number}?: ").strip()
    if name.lower() == "test":
        return None  # Signal to use default players
    pronouns = input(f"What are {name}'s pronouns?: ").strip()
    personality = input(f"What is {name}'s personality?: ").strip()
    return create_player(name, pronouns, personality)


def get_player_info():
    players = []
    default_players = [
        create_player(
            "Mark",
            "he/him",
            "a bit of a hothead, but passionate and kind",
            "Mark is Billy's 40-year-old son. He thinks Billy can be patronizing. He also thinks Billy is too old to make decisions and is losing his touch.",
        ),
        create_player(
            "Billy",
            "he/him",
            "cool, calm, and collected, but a schemer",
            "Billy is Mark's 70-year-old father and the owner of the shop. He thinks Mark is too rash and emotionally unstable to make decisions.",
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
            f"What is the relationship of {players[i]['name']} to {players[target]['name']}?: "
        ).strip()
        if not relation:
            relation = "Is an acquaintance of the other character."
        players[i]["relationship_to_target"] = relation

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
