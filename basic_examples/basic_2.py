"""It's best to ensure you are setting the correct level.

And to see all the output you should ensure you have a handler
configured that supports all levels.
"""
import logging
import sys

print("basic_2.py starting")

logger = logging.getLogger("basic_2")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

logger.info("an info message")
logger.error("an error message")

print("basic_2.py complete")
