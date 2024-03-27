import os
import textwrap
from utils.string import parse_utterance
from reality_agents.view.utils import get_emoji_by_index

TERMINAL_WIDTH = os.get_terminal_size().columns
PADDING = 17

# TODO print out char by char


def justify_center(text, width):
    words = text.split()
    line = words[0]
    for word in words[1:]:
        if len(line) + len(word) + 1 <= width:
            line += " " + word
        else:
            spaces_to_add = width - len(line)
            spaces_between_words = line.count(" ")
            if spaces_between_words > 0:
                extra_space, remaining_space = divmod(
                    spaces_to_add, spaces_between_words
                )
                line = line.replace(" ", " " * (extra_space + 1), remaining_space)
                line = line.replace(" ", " " * extra_space)
            yield line
            line = word
    yield line


def center_text(text):
    effective_width = TERMINAL_WIDTH - 2 * PADDING
    wrapped_text = textwrap.fill(text, width=effective_width)
    justified_lines = [
        " ".join(justify_center(line, effective_width))
        for line in wrapped_text.split("\n")
    ]
    centered_lines = [line.center(effective_width, " ") for line in justified_lines]
    return "\n".join([" " * PADDING + line for line in centered_lines]) + "\n\n"


def center_name(name):
    return name.center(TERMINAL_WIDTH, " ")


def display_end():
    print(center_text("THE END"))
    print("\n\n")


def display_dialogue(char_index, character, dialogue):
    formatted_name = f"{character} {get_emoji_by_index(char_index)}"
    response = f"Sure, here's a response from {character}:"
    formatted_dialogue = f"{parse_utterance(dialogue, [character, response])}\n\n"

    print(center_name(formatted_name.upper()))
    print(center_text(formatted_dialogue))
