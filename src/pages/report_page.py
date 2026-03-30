from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.exceptions import NavigationError


class ReportPage:
    PAGE_HEADING = (By.CSS_SELECTOR, "h2")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def verify_page_loaded(self) -> None:
        heading = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_HEADING)
        )
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))

        if "secure area" not in heading.text.lower():
            raise NavigationError("Secure page loaded, but heading was not as expected.")

    def get_page_heading(self) -> str:
        heading = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_HEADING)
        )
        return heading.text.strip()

    def get_flash_message(self) -> str:
        flash_message = self.wait.until(
            EC.visibility_of_element_located(self.FLASH_MESSAGE)
        )
        return flash_message.text.replace("\n", " ").strip()

    def get_current_url(self) -> str:
        return self.driver.current_url
