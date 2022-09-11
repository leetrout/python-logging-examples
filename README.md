# Python & Django Logging Examples

Simple katas to explore logging in Python & Django.

## Output buffering

👉 Reminder to set `PYTHONUNBUFFERED=1` or run `python -u` to ensure all
output is flushed immediately.

✅ Basic example 1 should output:

```
basic_1.py starting
an error message
basic_1.py complete
```

❌ You will see messages out of order if output is buffered:

```
an error message
basic_1.py starting
basic_1.py complete
```

## Basic examples

There are several examples in the `basic_examples` directory. Execute them with
Python and examine their behavior using the notes below.

### Basic 1

The `basic_1.py` file contains the bare minimum to use Python logging.

- Why does the info message not show up?
  - Because the default minimum log level is higher than the `INFO` level.
  - Because there is no handler for `INFO` messages
- What logger is being used?
  - The root logger because we did not provider a logger namespace when calling
    `getLogger`.

### Basic 2

The `basic_2.py` file starts to incorporate best practices for setting up
logging.

## Django example
