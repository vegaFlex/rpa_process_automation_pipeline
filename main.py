from src.browser.driver_factory import create_driver
from src.config import settings
from src.utils.logger import setup_logger
from src.workflows.process_runner import ProcessRunner


def main():
    logger = setup_logger(settings.LOG_DIR, settings.LOG_LEVEL)
    logger.info("Starting RPA process.")

    driver = None

    try:
        driver = create_driver()
        logger.info("Browser started successfully.")

        runner = ProcessRunner(driver, logger)
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
