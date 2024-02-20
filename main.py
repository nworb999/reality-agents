from utils.constants import VALID_GAME_TYPES
from utils.ssh_tunnel import start_tunnel, stop_tunnel
from reality_agents.data.database import get_db, setup_db
from reality_agents.data.repository import get_memory_entries
from reality_agents.view.conversation.game_handler import (
    play_conversation_game,
)
from reality_agents.view.horse_race.game_handler import play_horse_race_game
from utils.ascii import intro_text, spin


def main():
    intro_text()
    spin()
    start_tunnel(
        remote_server="imagination.mat.ucsb.edu",
        ssh_username="emma",
        ssh_pkey="~/.ssh/id_rsa",
        remote_port=11434,
        local_port=12345,
    )

    setup_db()

    # retrieve_data()

    game_type = input("Please enter the game type: ").lower().strip() or "convo"
    if game_type in ["conversation", "convo"]:
        play_conversation_game()
    elif game_type == "horse race":
        play_horse_race_game()
    elif game_type not in VALID_GAME_TYPES:
        print("Unknown game type. Exiting.")

    stop_tunnel()


if __name__ == "__main__":
    main()
