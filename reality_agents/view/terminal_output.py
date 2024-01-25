from colorama import Fore, Style
from utils.constants import race_horse, carousel_horse


# horse race
def display_progress(progress1, progress2):
    print(
        Fore.MAGENTA
        + f"Player 1: [{' ' * (100 - progress1)}{carousel_horse + ' '}{'=' * progress1}]\n"
        + Style.RESET_ALL
    )
    print(
        Fore.CYAN
        + f"Player 2: [{ ' ' * (100 - progress2)}{race_horse + ' '}{'=' * progress2}]\n\n"
        + Style.RESET_ALL
    )


def display_winner(winner):
    if winner:
        color = Fore.MAGENTA if winner == 1 else Fore.CYAN
        print(color + f"\nPlayer {winner}" + Style.RESET_ALL + " wins the game!")
