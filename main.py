from src.browser.driver_factory import create_driver
from src.config import settings
from src.utils.logger import setup_logger


def main():
    logger = setup_logger(settings.LOG_DIR, settings.LOG_LEVEL)
    logger.info("Starting Selenium smoke test.")

    driver = None

    try:
        driver = create_driver()
        logger.info("Browser started successfully.")

        driver.get(settings.BASE_URL)
        logger.info("Opened URL: %s", settings.BASE_URL)

        print("Page title:", driver.title)
        logger.info("Page title captured successfully.")

    except Exception as exc:
        logger.exception("Smoke test failed: %s", exc)
        raise

    finally:
        if driver:
            driver.quit()
            logger.info("Browser closed successfully.")


if __name__ == "__main__":
    main()
