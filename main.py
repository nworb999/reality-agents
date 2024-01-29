from utils.constants import ASCII_INTRO, VALID_GAME_TYPES
from reality_agents.view.game_handlers import (
    play_horse_race_game,
    play_conversation_game,
)


def main():
    game_type = input("Please enter the game type: ").lower().strip() or "convo"

    if game_type in ["conversation", "convo"]:
        play_conversation_game()
    elif game_type == "horse race":
        play_horse_race_game()
    elif game_type not in VALID_GAME_TYPES:
        print("Unknown game type. Exiting.")


if __name__ == "__main__":
    print("\033[2J\033[H", end="")
    print(ASCII_INTRO)

    main()
