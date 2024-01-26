from colorama import Fore, Style
from utils.constants import race_horse, carousel_horse, ascii_intro_2

COLORS = [
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.WHITE,
]

# horse race
def display_progress(*progress):
    for i, player_progress in enumerate(progress):
        horse = carousel_horse if i % 2 == 0 else race_horse
        color = COLORS[i % len(COLORS)]

        print(
            color
            + f"Player {i + 1}: [{' ' * (100 - player_progress)}{horse + ' '}{'=' * player_progress}]"
            + Style.RESET_ALL
        )


def display_winner(winner):
    winner_int = int(winner)

    color_index = (winner_int - 1) % len(COLORS)
    color = COLORS[color_index]
    print(
        "Congratulations! Player "
        + color
        + str(winner)
        + Style.RESET_ALL
        + " wins the race!"
    )
