import logging
import logging.config
import random
import time


logging_logger = logging.getLogger("helpers.logger")


def init_logger():
    config = {
        "version": 1,
        # Disables all normal logging until some rouge library
        # (dramatiq ...) turns it back on accidentally.
        "disable_existing_loggers": True,
        "formatters": {
            # "standard": {
            #     "format": log_settings.console_format,
            #     "datefmt": log_settings.console_datefmt,
            # },
            "json": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "fmt": "%(levelname)s %(name)s %(message)s",
                "timestamp": True,
                "rename_fields": {"levelname": "level"},
            }
        },
        "handlers": {
            "console": {
                "level": "INFO",
                "formatter": "json",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
        },
        "loggers": {
            "api": {"propagate": True},
            "helpers": {"propagate": True},
            "instances": {"propagate": True},
            "models": {"propagate": True},
            "services": {"propagate": True},
            "dramatiq": {"propagate": False},
            "opensearch": {"propagate": False},
            "sentry": {"propagate": False},
            "uvicorn": {"propagate": False},
            "trafilatura": {"propagate": False},
            "pymorphy2": {"propagate": False},
            "sentence_transformers": {"propagate": False},
            "matplotlib": {"propagate": False},
            "easyocr": {"propagate": False},
            "opentelemetry": {"propagate": True},
            # if __name__ == "__main__"
            "__main__": {
                "level": "DEBUG",
                "propagate": True,
            },
        },
        "root": {  # root logger
            "handlers": ["console"],
            "level": "INFO",
        },
    }

    logging.config.dictConfig(config)
    logging_logger.info("Logging configuration has been set")


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    init_logger()

    logger.info("Hello, world!")

    time.sleep(10)

    while True:
        time.sleep(1)
        logger.info("Processing data")
        data = random.randint(0, 100)
        result = data * 2
        logger.info(f"Data processed. Result is {result}")
