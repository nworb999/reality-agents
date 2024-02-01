from colorama import Fore, Style
import os
from utils.constants import RACE_HORSE, CAROUSEL_HORSE
from reality_agents.view.utils import get_emoji_by_index

COLORS = [
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.WHITE,
]

TERMINAL_WIDTH = os.get_terminal_size().columns


# conversation game
# TODO center it more so it looks like a screenplay
# also prints out char by char
def display_dialogue(character, input, position):
    if position == "left":
        line = f"{get_emoji_by_index(character)} :: {input['dialogue']}"
    else:
        line = f"{input['dialogue']} :: {get_emoji_by_index(character)}".rjust(
            TERMINAL_WIDTH - 1
        )
    print(line)


# horse race
def display_progress(*progress):
    for i, player_progress in enumerate(progress):
        horse = CAROUSEL_HORSE if i % 2 == 0 else RACE_HORSE
        color = COLORS[i % len(COLORS)]

        print(
            color
            + f"Player {i + 1}: [{' ' * (100 - player_progress)}{horse + ' '}{'=' * player_progress}]"
            + Style.RESET_ALL
        )


def display_winners(winners):
    if not winners:
        print("No winners yet.")
        return

    if len(winners) == 1:
        print(f"Player {winners[0]} wins the race!")
    else:
        winners_str = ", ".join(str(winner) for winner in winners)
        print(f"Players: {winners_str} tied the race.")
