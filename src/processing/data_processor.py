import json
from pathlib import Path


def save_raw_data(payload: dict, output_path: Path) -> None:
    output_path.write_text(
        json.dumps(payload, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )
