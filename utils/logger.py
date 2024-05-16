import asyncio
from colorama import Fore, init
import logging
import random
from datetime import datetime
from fastapi.logger import logger as fastapi_logger

init(autoreset=True)


class PrintCaptureHandler(logging.Handler):
    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.logs = []
        self.colors = [Fore.GREEN, Fore.MAGENTA, Fore.CYAN]

    def emit(self, record):
        try:
            # Choose a random color from the list
            color = random.choice(self.colors)
            # Format the message with a timestamp and apply the color
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msg = self.format(record)
            colored_msg = f"{color}{timestamp} - {msg}{Fore.RESET}"  # Explicit reset after each message
            self.logs.append(colored_msg)
            self.loop.call_soon_threadsafe(print, colored_msg)
        except Exception:
            self.handleError(record)


logger = logging.getLogger(__name__)

# https://chatgpt.com/c/7e180cb6-f31b-416f-8f87-728c7a5d2c8d

formatter = logging.Formatter("%(levelname)s - %(message)s")
main_event_loop = asyncio.get_event_loop()
print_capture_handler = PrintCaptureHandler(main_event_loop)
print_capture_handler.setFormatter(formatter)
logger.addHandler(print_capture_handler)

try:
    from fastapi.logger import logger as fastapi_logger

    gunicorn_logger = logging.getLogger("gunicorn.error")
    if gunicorn_logger.handlers:
        fastapi_logger.handlers = gunicorn_logger.handlers
        fastapi_logger.setLevel(gunicorn_logger.level)
    else:
        raise ValueError("No Gunicorn handlers found")
except (ValueError, ImportError) as e:
    # Fallback to basic configuration when not running under Gunicorn
    logger.setLevel(logging.INFO)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


logger.setLevel(logging.INFO)

logger.info("Logger setup complete")
print("Logger setup complete")
