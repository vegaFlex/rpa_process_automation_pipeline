from src.processing.data_processor import transform_session_data


def test_transform_session_data_returns_expected_columns():
    payload = {
        "execution_timestamp": "2026-03-30T16:00:00",
        "page_heading": "Secure Area",
        "flash_message": "You logged into a secure area! ×",
        "current_url": "https://the-internet.herokuapp.com/secure",
    }

    dataframe = transform_session_data(payload)

    assert dataframe.loc[0, "page_heading"] == "Secure Area"
    assert bool(dataframe.loc[0, "login_success"]) is True
    assert dataframe.loc[0, "page_category"] == "secure_area"
    assert "×" not in dataframe.loc[0, "flash_message"]
