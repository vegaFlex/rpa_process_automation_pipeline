import logging
from datetime import datetime
from pathlib import Path


def setup_logger(log_dir: Path, log_level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("rpa_pipeline")
    logger.setLevel(log_level)

    if logger.handlers:
        return logger

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    latest_log_file = log_dir / "automation.log"
    run_log_file = log_dir / f"automation_{timestamp}.log"

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    latest_file_handler = logging.FileHandler(latest_log_file, encoding="utf-8")
    latest_file_handler.setFormatter(formatter)

    run_file_handler = logging.FileHandler(run_log_file, encoding="utf-8")
    run_file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(latest_file_handler)
    logger.addHandler(run_file_handler)
    logger.addHandler(stream_handler)

    return logger
