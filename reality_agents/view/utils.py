import random
import time


def slow_type(text, delay=0.1):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


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
                return [
                    {
                        "name": "Mark",
                        "personality": "a bit of a hothead, but passionate and kind",
                    },
                    {
                        "name": "Billy",
                        "personality": "cool calm and collected, but a schemer",
                    },
                ]
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
