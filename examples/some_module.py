import logging


logger = logging.getLogger(__name__)


def do_work():
    logger.warning("Doing some work")
    logger.error("Something might go wrong")
    logger.warning("Finishing work")
