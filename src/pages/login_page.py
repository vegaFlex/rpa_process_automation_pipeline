from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.exceptions import LoginError


class LoginPage:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_BANNER = (By.ID, "flash")
    SECURE_AREA = (By.CSS_SELECTOR, "h2")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def login(self, username: str, password: str) -> None:
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )

        username_input.clear()
        username_input.send_keys(username)

        password_input.clear()
        password_input.send_keys(password)

        login_button.click()

    def verify_login_success(self) -> bool:
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_BANNER))
        secure_area = self.wait.until(
            EC.visibility_of_element_located(self.SECURE_AREA)
        )
        banner = self.driver.find_element(*self.SUCCESS_BANNER)

        banner_text = banner.text.lower()
        page_text = secure_area.text.lower()

        if "you logged into a secure area!" in banner_text and "secure area" in page_text:
            return True

        raise LoginError("Login was submitted, but success confirmation was not found.")
