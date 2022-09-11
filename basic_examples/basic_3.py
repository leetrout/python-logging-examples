"""Of course the basics can be covered with the convenient built-in.

But is everything going where we want it to go?
"""
import logging

print("basic_3.py starting")

logging.basicConfig()
logger = logging.getLogger("basic_3")
logger.setLevel(logging.INFO)

logger.info("an info message")
logger.error("an error message")

print("basic_3.py complete")
