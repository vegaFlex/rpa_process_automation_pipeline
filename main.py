import argparse

from src.browser.driver_factory import create_driver
from src.config import settings
from src.utils.logger import setup_logger
from src.workflows.process_runner import ProcessRunner


def parse_args():
    parser = argparse.ArgumentParser(
        description="RPA Process Automation Pipeline"
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run browser in headless mode",
    )
    parser.add_argument(
        "--demo-email",
        action="store_true",
        help="Enable demo email payload generation",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    logger = setup_logger(settings.LOG_DIR, settings.LOG_LEVEL)
    logger.info("Starting RPA process.")

    driver = None

    try:
        headless_mode = args.headless or settings.HEADLESS
        email_enabled = args.demo_email or settings.EMAIL_ENABLED

        driver = create_driver(headless=headless_mode)
        logger.info("Browser started successfully.")

        runner = ProcessRunner(driver, logger, email_enabled=email_enabled)
        runner.run()

    except Exception as exc:
        logger.exception("Process execution failed: %s", exc)
        raise

    finally:
        if driver:
            driver.quit()
            logger.info("Browser closed successfully.")


if __name__ == "__main__":
    main()
