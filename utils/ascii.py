import os
import sys
import time
from colorama import Fore
from utils.constants import ASCII_INTRO

TERMINAL_WIDTH = os.get_terminal_size().columns

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


def clear_screen():
    # (used to use print("\033[2J\033[H", end=""))
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def spin(duration=3):
    start_time = time.time()
    while True:
        for symbol in spinner_symbols:
            if time.time() - start_time >= duration:
                sys.stdout.write("\r" + " " * len(symbol))
                sys.stdout.write("\r")
                sys.stdout.flush()
                return
            sys.stdout.write("\r" + symbol)
            sys.stdout.flush()
            time.sleep(0.1)


def intro_text():
    clear_screen()
    print(ASCII_INTRO)
