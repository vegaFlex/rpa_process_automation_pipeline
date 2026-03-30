from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.config import settings


def create_driver(headless: bool = False):
    if settings.BROWSER.lower() != "chrome":
        raise ValueError("Currently only Chrome is supported.")

    chrome_options = Options()

    prefs = {
        "download.default_directory": str(settings.DOWNLOAD_DIR.resolve()),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    if headless:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    return driver
