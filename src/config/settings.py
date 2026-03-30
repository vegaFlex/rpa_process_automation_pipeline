import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
DOWNLOAD_DIR = BASE_DIR / os.getenv("DOWNLOAD_DIR", "data/downloads")
OUTPUT_DIR = DATA_DIR / "output"
LOG_DIR = BASE_DIR / "logs"

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com/login")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"

LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "")

EMAIL_ENABLED = os.getenv("EMAIL_ENABLED", "False").lower() == "true"
EMAIL_TO = os.getenv("EMAIL_TO", "")
EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT", "RPA Automation Report")

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
