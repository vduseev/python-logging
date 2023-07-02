import time
import random


def process_data(data):
    print("Processing data")
    result = data * 2 
    print(f"Data processed. Result is {result}")
    return result


if __name__ == "__main__":
    while True:
        data = random.randint(0, 100)
        result = process_data(data)
        time.sleep(1)
        print(result)
