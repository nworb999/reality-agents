from colorama import Style
from utils.constants import RACE_HORSE, CAROUSEL_HORSE
from utils.ascii import COLORS


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
