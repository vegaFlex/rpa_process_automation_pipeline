import json
from pathlib import Path

import pandas as pd


def save_raw_data(payload: dict, output_path: Path) -> None:
    output_path.write_text(
        json.dumps(payload, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )


def load_raw_data(input_path: Path) -> dict:
    return json.loads(input_path.read_text(encoding="utf-8"))


def transform_session_data(payload: dict) -> pd.DataFrame:
    cleaned_flash_message = payload.get("flash_message", "").replace("×", "").strip()
    current_url = payload.get("current_url", "")

    processed_record = {
        "execution_timestamp": payload.get("execution_timestamp", ""),
        "page_heading": payload.get("page_heading", ""),
        "flash_message": cleaned_flash_message,
        "current_url": current_url,
        "login_success": "secure" in current_url.lower(),
        "message_length": len(cleaned_flash_message),
        "page_category": "secure_area" if "secure" in current_url.lower() else "unknown",
    }

    return pd.DataFrame([processed_record])


def save_processed_data(dataframe: pd.DataFrame, output_path: Path) -> None:
    dataframe.to_csv(output_path, index=False)
