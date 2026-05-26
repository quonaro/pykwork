"""
Logger configuration for Kwork API library
"""

import logging


def get_logger(name: str, level: int = logging.WARNING) -> logging.Logger:
    """
    Get or create a logger with specified level.

    Args:
        name: Logger name
        level: Logging level (default: WARNING)

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(level)
    return logger
