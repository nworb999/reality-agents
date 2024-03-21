import random
from colorama import Fore

ASCII_INTRO = """
█▀█ █░█ █▄▄ █░░ █ █▀▀   █▀▀ ▀▄▀ █▀█ █▀▀ █▀█ █ █▀▄▀█ █▀▀ █▄░█ ▀█▀   █ █
█▀▀ █▄█ █▄█ █▄▄ █ █▄▄   ██▄ █░█ █▀▀ ██▄ █▀▄ █ █░▀░█ ██▄ █░▀█ ░█░   █ █
"""

COLORS = [
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.WHITE,
]

SPINNER_SYMBOLS = [
    "⠋",
    "⠙",
    "⠹",
    "⠸",
    "⠼",
    "⠴",
    "⠦",
    "⠧",
    "⠇",
    "⠏",
]

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

SCENE_DEFAULT = "auto shop"
CONFLICT_DEFAULT = "money."

DEFAULT_PLAYERS = [
    {
        "name": "Mark",
        "personality": "hothead",
        "relationship_to_target": "He calls Billy dad. He thinks he's too old to run things.",
    },
    {
        "name": "Billy",
        "personality": "calm, but a schemer",
        "relationship_to_target": "He thinks Mark is too rash and emotionally unstable to make decisions.",
    },
]
