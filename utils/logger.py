import asyncio
import logging
from fastapi.logger import logger as fastapi_logger


class PrintCaptureHandler(logging.Handler):
    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.logs = []

    def emit(self, record):
        try:
            msg = self.format(record)
            self.logs.append(msg)
        except Exception:
            self.handleError(record)


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
