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
GENERIC_SIMS_STATEMENTS = [
    "Fluffing the clouds...",
    "Adjusting the ambiance...",
    "Ensuring the microphones are hidden...",
    "Infusing the air with aroma...",
    "Charging the crystals...",
    "Tidying up the place...",
    "Testing the lighting...",
    "Arranging the scenery...",
    "Adjusting the camera angles...",
    "Infusing the set with suspense...",
    "Tidying up the plot twists...",
    "Polishing the on-screen chemistry...",
    "Setting the temperature...",
    "Aligning the stars...",
    "Cueing the background music...",
    "Ensuring the Wi-Fi is strong...",
    "Polishing the atmosphere...",
    "Balancing the energy levels...",
    "Harmonizing the surroundings...",
    "Refreshing the ambiance...",
    "Fine-tuning the vibes...",
    "Saturating the colors...",
    "Smoothing the edges...",
    "Summoning the spirits...",
    "Synchronizing the elements...",
    "Recharging the atmosphere...",
    "Chewing the scenery...",
]
