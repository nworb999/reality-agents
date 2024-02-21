from utils.ascii import TERMINAL_WIDTH
from reality_agents.view.utils import get_emoji_by_index


# TODO print out char by char
def center_text(text):
    return text.center(TERMINAL_WIDTH, " ")


def display_end():
    print("\n\n")
    print(center_text("THE END"))
    print("\n\n")


def display_dialogue(char_index, character, dialogue):
    formatted_name = f"{character} {get_emoji_by_index(char_index)}"
    formatted_dialogue = f"{dialogue}\n\n"

    print(center_text(formatted_name))
    print(center_text(formatted_dialogue))
