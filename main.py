from contextlib import contextmanager
import traceback
from utils.constants import VALID_GAME_TYPES
from utils.ssh_tunnel import start_tunnel, stop_tunnel
from reality_agents.data.database import get_db, setup_db
from reality_agents.view.game_handler import (
    play_conversation_game,
)
from utils.ascii import intro_text, spin, clear_screen
import sys

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
    setup_main()
    start_tunnel(
        remote_server="imagination.mat.ucsb.edu",
        ssh_username="emma",
        ssh_pkey="~/.ssh/id_rsa",
        remote_port=11434,
        local_port=12345,
    )
    game_loop()
    stop_tunnel()


def setup_main():
    intro_text()
    spin()


def game_loop():
    while True:
        try:
            play_game()
        except ConnectionError:
            handle_connection_error()
        except KeyboardInterrupt:
            handle_keyboard_interrupt()
            break  # Exit the while loop on KeyboardInterrupt
        except Exception:
            handle_unexpected_error()


def play_game():
    with initialize_db_session() as db:
        play_conversation_game(db, SCENE_CACHE, CONFLICT_CACHE, CHARACTERS_CACHE)


def handle_connection_error():
    play_conversation_game(db, SCENE_CACHE, CONFLICT_CACHE, CHARACTERS_CACHE)


def handle_keyboard_interrupt():
    clear_screen()
    intro_text()
    print("\nGoodbye!\n")
    spin(2)


def handle_unexpected_error():
    print("Error! Sorry, it's an experiment after all! :)")
    spin(1)
    traceback_lines = traceback.format_exc().splitlines()
    # Print the last 3 lines of the traceback
    for line in traceback_lines[-3:]:
        print(f"Details: {line}")
    sys.exit(1)


if __name__ == "__main__":
    main()
