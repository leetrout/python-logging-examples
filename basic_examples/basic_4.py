"""Let's send errors to stderr and everything else to stdout..."""
import logging
import sys

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.addFilter(lambda r: r.levelno < logging.WARNING)

stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.WARNING)
stderr_handler.addFilter(lambda r: r.levelno >= logging.WARNING)


print("basic_3.py starting")

logger = logging.getLogger("basic_3")

logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

logger.setLevel(logging.INFO)

logger.info("an info message")
logger.error("an error message")

print("basic_3.py complete")
