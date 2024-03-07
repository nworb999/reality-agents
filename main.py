from contextlib import contextmanager
from utils.ssh_tunnel import start_tunnel, stop_tunnel
from reality_agents.data.database import get_db, setup_db
from reality_agents.view.game_handler import (
    play_conversation_game,
)
from utils.ascii import intro_text, spin, clear_screen
import time


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
    try:
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
            play_conversation_game(db)

        stop_tunnel()
    except KeyboardInterrupt:
        clear_screen()
        intro_text()
        print()
        print("Goodbye!")
        print()
        time.sleep(2)


if __name__ == "__main__":
    main()
