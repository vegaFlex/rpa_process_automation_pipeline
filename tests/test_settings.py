from src.config import settings


def test_base_url_is_configured():
    assert settings.BASE_URL.startswith("http")


def test_download_dir_exists():
    assert settings.DOWNLOAD_DIR.exists()


def test_log_dir_exists():
    assert settings.LOG_DIR.exists()
