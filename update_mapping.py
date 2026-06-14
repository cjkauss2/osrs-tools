import os
import json
import requests
from pathlib import Path

API_URL = "https://prices.runescape.wiki/api/v1/osrs/mapping"
OUTPUT_FILE = Path("data/item_mapping.json")


def main():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    # Overwrite the file if it already exists
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Saved item mapping to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()