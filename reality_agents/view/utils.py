import random


# conversation game
def get_player_info():
    players = []
    while True:
        if len(players) < 2:
            player_name = input("What is the player's name? ")
        else:
            player_name = input(
                f"What is the player's name? (or enter to continue with {len(players)} players) "
            )

        if not player_name:
            if len(players) < 2:
                print("Not enough players to start the game. Exiting.")
                return None
            else:
                break

        personality = input("What is their personality like? ")

        players.append({"name": player_name, "personality": personality})

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

EMOJI_LIST = list(ANIMAL_EMOJIS.values())
random.shuffle(EMOJI_LIST)


def get_emoji_by_index(index):
    return EMOJI_LIST[index % len(EMOJI_LIST)]


def assign_characters_to_sides(num_characters):
    character_indices = list(range(num_characters))

    random.shuffle(character_indices)

    half_size = len(character_indices) // 2
    left_side_indices = character_indices[:half_size]
    right_side_indices = character_indices[half_size:]

    character_sides = dict((index, "left") for index in left_side_indices)
    character_sides.update(dict((index, "right") for index in right_side_indices))

    return character_sides
