import logging
import random
import time

import some_module
from loguru import logger


# logging.getLogger("some_module").disabled = True


def process_data(data):
    some_module.do_work()
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
