import asyncio
import logging
import os
from datetime import datetime
from fastapi.logger import logger as fastapi_logger


def is_running_under_gunicorn():
    if "GUNICORN_CMD_ARGS" in os.environ:
        return True
    # Optionally check for other Gunicorn-specific or related environment variables
    if (
        "SERVER_SOFTWARE" in os.environ
        and "gunicorn" in os.environ["SERVER_SOFTWARE"].lower()
    ):
        return True
    return False


class PrintCaptureHandler(logging.Handler):
    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.logs = []

    def emit(self, record):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msg = self.format(record)
            msg = f"{timestamp} - {msg}"  # Explicit reset after each message
            self.logs.append(msg)
            self.loop.call_soon_threadsafe(print, msg)
        except Exception:
            self.handleError(record)

    def clear_logs(self):
        self.logs.clear()


if is_running_under_gunicorn():
    gunicorn_logger = logging.getLogger("gunicorn.error")
    fastapi_logger.handlers = gunicorn_logger.handlers
    if __name__ != "main":
        fastapi_logger.setLevel(gunicorn_logger.level)
    else:
        fastapi_logger.setLevel(logging.DEBUG)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    main_event_loop = asyncio.get_event_loop()
    print_capture_handler = PrintCaptureHandler(main_event_loop)

    logger.addHandler(print_capture_handler)

    logger.info("Logger setup complete")
else:
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
