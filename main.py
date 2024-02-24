from contextlib import contextmanager
from utils.constants import VALID_GAME_TYPES
from utils.ssh_tunnel import start_tunnel, stop_tunnel
from reality_agents.data.database import get_db, setup_db
from reality_agents.data.repository import get_memory_entries
from reality_agents.view.conversation.game_handler import (
    play_conversation_game,
)
from utils.ascii import intro_text, spin


@contextmanager
def initialize_db_session():
    setup_db()
    db_session_gen = get_db()
    db = next(db_session_gen)
    try:
        yield db
    finally:
        next(db_session_gen, None)


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

    with initialize_db_session() as db:
        game_type = input("Please enter the game type: ").lower().strip() or "convo"
        if game_type in ["conversation", "convo"]:
            play_conversation_game(db)
        elif game_type not in VALID_GAME_TYPES:
            print("Unknown game type. Exiting.")

    stop_tunnel()


if __name__ == "__main__":
    main()
