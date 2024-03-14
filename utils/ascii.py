import os
import sys
import time
from colorama import Fore
from utils.constants import ASCII_INTRO

COLORS = [
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.WHITE,
]

spinner_symbols = [
    "⠋",
    "⠙",
    "⠹",
    "⠸",
    "⠼",
    "⠴",
    "⠦",
    "⠧",
    "⠇",
    "⠏",
]


def clear_line():
    # Move the cursor to the beginning of the line
    print("\033[1G", end="")
    # Clear the line from the cursor position to the end of the line
    print("\033[0K", end="")


def clear_screen():
    # (used to use print("\033[2J\033[H", end=""))
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def spin(duration=3):
    # Hide cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    start_time = time.time()
    while True:
        for symbol in spinner_symbols:
            if time.time() - start_time >= duration:
                clear_line()
                # Show cursor
                sys.stdout.write("\033[?25h")
                sys.stdout.flush()
                return
            sys.stdout.write("\r" + symbol)
            sys.stdout.flush()
            time.sleep(0.1)


def intro_text():
    clear_screen()
    print(ASCII_INTRO)
