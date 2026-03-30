import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]
DOWNLOAD_DIR = BASE_DIR / os.getenv("DOWNLOAD_DIR", "data/downloads")
LOG_DIR = BASE_DIR / "logs"

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com/login")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"

LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "")

DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

