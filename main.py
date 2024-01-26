from utils.constants import ascii_intro_2
from reality_agents.view.game_handlers import play_horse_race_game


def main():
    game_type = input("Please enter the game type: ") or "horse race"
    num_players_input = input("Enter the number of players: ")
    if game_type.lower().strip() == "horse race":
        play_horse_race_game(num_players_input)
    else:
        print("Unknown game type. Exiting.")


if __name__ == "__main__":
    print("\033[2J\033[H", end="")
    print(ascii_intro_2)

    main()
