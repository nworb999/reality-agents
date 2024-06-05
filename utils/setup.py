import sys
import traceback
from utils.ascii import intro_text, spin, clear_screen
from reality_agents.view.game_handler import play_conversation_game


SCENE_CACHE = {}
CONFLICT_CACHE = {}
CHARACTERS_CACHE = {}


def setup_main_ascii(test_flag=False):
    intro_text()
    if not test_flag:
        spin()


def game_loop(test_flag=False, cuttlefish_flag=False):
    while True:
        try:
            play_game(test_flag, cuttlefish_flag)
        except ConnectionError:  # just replay (with cache)
            play_game(test_flag, cuttlefish_flag)
        except KeyboardInterrupt:
            handle_keyboard_interrupt(test_flag)
            break  # Exit the while loop on KeyboardInterrupt
        except Exception:
            handle_unexpected_error(test_flag)
        break


# this should be happening in back end
def play_game(test_flag, cuttlefish_flag):
    play_conversation_game(
        SCENE_CACHE, CONFLICT_CACHE, CHARACTERS_CACHE, test_flag, cuttlefish_flag
    )


def handle_keyboard_interrupt(test_flag):
    clear_screen()
    intro_text()
    print("\nGoodbye!\n")
    if not test_flag:
        spin(2)


def handle_unexpected_error(test_flag):
    print("Error! Sorry, it's an experiment after all! :)")
    if not test_flag:
        spin(1)
    traceback_lines = traceback.format_exc().splitlines()
    # Print the last 3 lines of the traceback
    for line in traceback_lines[-10:]:
        print(f"Details: {line}")
    sys.exit(1)
