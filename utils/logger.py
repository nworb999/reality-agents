from fastapi.logger import logger as fastapi_logger
import logging


gunicorn_logger = logging.getLogger("gunicorn.error")
fastapi_logger.handlers = gunicorn_logger.handlers
if __name__ != "main":
    fastapi_logger.setLevel(gunicorn_logger.level)
else:
    fastapi_logger.setLevel(logging.DEBUG)


class PrintCaptureHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.latest_message = ""

    def emit(self, record):
        try:
            msg = self.format(record)
            self.latest_message = msg
            print(msg)  # Or you can log to a file or other destination
        except Exception:
            self.handleError(record)


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create and add the custom handler
print_capture_handler = PrintCaptureHandler()
logger.addHandler(print_capture_handler)

# Optional: Add a formatter to the handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
print_capture_handler.setFormatter(formatter)
