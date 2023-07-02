import logging
import random
import time


logger = logging.getLogger(__name__)
logger.add("logfile_{time}.log", rotation="1 day")


def process_data(data):
    logger.info("Processing data")
    result = data * 2
    logger.info(f"Data processed. Result is {result}")
    return result


if __name__ == "__main__":
    while True:
        data = random.randint(0, 100)
        result = process_data(data)
        time.sleep(1)
        logger.info(result)
