import logging
import random
import time


logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")


def process_data(data):
    logging.info("Processing data")
    result = data * 2
    logging.info(f"Data processed. Result is {result}")
    return result


if __name__ == "__main__":
    while True:
        data = random.randint(0, 100)
        result = process_data(data)
        time.sleep(1)
        logging.info(result)
