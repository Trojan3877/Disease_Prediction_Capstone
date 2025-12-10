import logging
from rich.logging import RichHandler

def get_logger(name: str) -> logging.Logger:
    """
    Returns a formatted logger using Rich for beautiful terminal output.
    """
    FORMAT = "%(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=FORMAT,
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )

    logger = logging.getLogger(name)
    return logger
