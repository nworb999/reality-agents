from contextlib import contextmanager
import traceback
from utils.constants import VALID_GAME_TYPES
from utils.ssh_tunnel import start_tunnel, stop_tunnel
from reality_agents.data.database import get_db, setup_db
from reality_agents.view.game_handler import (
    play_conversation_game,
)
from utils.ascii import intro_text, spin, clear_screen

SCENE_CACHE = {}
CONFLICT_CACHE = {}
CHARACTERS_CACHE = {}


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
    while True:
        try:
            with initialize_db_session() as db:
                play_conversation_game(
                    db, SCENE_CACHE, CONFLICT_CACHE, CHARACTERS_CACHE
                )
        except ConnectionError:
            play_conversation_game(db, SCENE_CACHE, CONFLICT_CACHE, CHARACTERS_CACHE)
        except KeyboardInterrupt:
            clear_screen()
            intro_text()
            print()
            print("Goodbye!")
            print()
            spin(2)
            break  # Exit the while loop on KeyboardInterrupt
        except Exception as e:
            print("Error! Sorry, it's an experiment after all! :)")
            spin(1)
            traceback_lines = traceback.format_exc().splitlines()
            # Print the last 3 lines of the traceback
            for line in traceback_lines[-3:]:
                print(f"Details: {line}")
    stop_tunnel()


if __name__ == "__main__":
    main()
