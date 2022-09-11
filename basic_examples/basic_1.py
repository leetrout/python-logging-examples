"""The minimum amount of code to log something.

However, not everything will show up in the output...
"""
import logging

print("basic_1.py starting")
logger = logging.getLogger()

logger.info("an info message")
logger.error("an error message")

print("basic_1.py complete")
