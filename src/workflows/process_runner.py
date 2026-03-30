from src.config import settings
from src.pages.login_page import LoginPage
from src.pages.report_page import ReportPage


class ProcessRunner:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def run(self) -> None:
        self.logger.info("Starting login workflow.")

        login_page = LoginPage(self.driver)
        login_page.open(settings.BASE_URL)
        self.logger.info("Login page opened: %s", settings.BASE_URL)

        login_page.login(settings.LOGIN_USERNAME, settings.LOGIN_PASSWORD)
        self.logger.info("Login form submitted.")

        login_page.verify_login_success()
        self.logger.info("Login successful.")

        report_page = ReportPage(self.driver)
        report_page.verify_page_loaded()
        self.logger.info("Secure/report page loaded successfully.")

        page_heading = report_page.get_page_heading()
        flash_message = report_page.get_flash_message()

        self.logger.info("Page heading: %s", page_heading)
        self.logger.info("Flash message: %s", flash_message)

        print("Page heading:", page_heading)
        print("Flash message:", flash_message)
