import random
import time
from datetime import datetime


def log(message):
    print(f"{datetime.now()}: {message}")


def process_data(data):
    log("Processing data")
    result = data * 2
    log(f"Data processed. Result is {result}")
    return result


if __name__ == "__main__":
    while True:
        data = random.randint(0, 100)
        result = process_data(data)
        time.sleep(1)
        log(result)
