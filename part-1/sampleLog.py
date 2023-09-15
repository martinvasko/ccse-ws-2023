import logging

logging.basicConfig(
    filename="sample.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.debug("Sample debug message")
