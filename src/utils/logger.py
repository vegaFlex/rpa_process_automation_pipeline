import logging
from pathlib import Path


def setup_logger(log_dir: Path, log_level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("rpa_pipeline")
    logger.setLevel(log_level)

    if logger.handlers:
        return logger

    log_file = log_dir / "automation.log"

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
