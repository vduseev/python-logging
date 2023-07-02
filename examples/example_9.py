import logging
import random
import time
import sys

from opensearch_logger import OpenSearchHandler


handler = OpenSearchHandler(
    index_name="my-logs",
    hosts=["https://localhost:9200"],
    http_auth=("admin", "admin"),
    http_compress=True,
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.addHandler(logging.StreamHandler(sys.stdout))


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
