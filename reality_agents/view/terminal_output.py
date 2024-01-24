from colorama import Fore, Style


# progress bar race
def display_progress(progress1, progress2):
    print(
        Fore.RED
        + f"Player 1: [{'=' * progress1}{' ' * (100 - progress1)}]"
        + Style.RESET_ALL
    )
    print(
        Fore.BLUE
        + f"Player 2: [{'=' * progress2}{' ' * (100 - progress2)}]"
        + Style.RESET_ALL
    )


def display_winner(winner):
    if winner:
        color = Fore.RED if winner == 1 else Fore.BLUE
        print(color + f"\nPlayer {winner} wins the game!" + Style.RESET_ALL)
