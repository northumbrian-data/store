import os
import logging
import django
from uvicorn import Config, Server
from loguru import logger
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings.base")


class InterceptHandler(logging.Handler):
    """
    Intercept all default Python logging statements and send to loguru.
    """

    def emit(self, record):
        # get corresponding loguru level if it exists
        # if not, use the level number
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        # send loguru statement, making sure we raise an exception where we should
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logging():
    # intercept everything at the root logger at level as per the settings files
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(settings.LOG_LEVEL)
    # remove every other logger's handlers
    # and propagate them to the root logger
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True


if __name__ == "__main__":
    # set-up django, loads settings etc.
    django.setup()

    from server.asgi import get_application  # requires django to be set up

    # start the asynchronous web app server
    app = get_application()

    # initialise uvicorn server
    server = Server(
        Config(
            app=app,
            host=settings.HOST,
            log_level=settings.LOG_LEVEL.lower(),  # annoyingly uses lowercase log levels
        ),
    )

    # setup logging last, to make sure no library overwrites it
    # (they shouldn't, but it happens)
    setup_logging()

    # run the thing
    server.run()
