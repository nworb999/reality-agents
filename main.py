from contextlib import contextmanager
from utils.ssh_tunnel import start_tunnel, stop_tunnel
from reality_agents.data.database import get_db, setup_db
from reality_agents.view.game_handler import (
    play_conversation_game,
)
from utils.ascii import intro_text, spin, clear_screen
import time
import traceback


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
        spin(2)
    except Exception as e:
        print("Error! Sorry, it's an experiment after all! :)")
        spin(1)
        traceback_lines = traceback.format_exc().splitlines()
        # Print the last 3 lines of the traceback
        for line in traceback_lines[-3:]:
            print(f"Details: {line}")


if __name__ == "__main__":
    main()
