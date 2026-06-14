import json
import pandas as pd

import requests
import pandas as pd

PRICE_API_URL = "https://prices.runescape.wiki/api/v1/osrs/latest"
PRICE_API_USER_AGENT = "leagues-rewards-value"
PRICE_API_TIMEOUT = 30

def get_item_prices(item_id):
    """
    Returns (high_price, low_price, avg_price) for an OSRS item.
    """
    response = requests.get(
        PRICE_API_URL,
        params={"id": item_id},
        headers={"User-Agent": PRICE_API_USER_AGENT},
        timeout=PRICE_API_TIMEOUT,
    )
    response.raise_for_status()

    data = response.json()["data"]

    item_data = data.get(str(item_id))
    if item_data is None:
        return None, None, None

    high_price = item_data.get("high")
    low_price = item_data.get("low")

    if high_price is not None and low_price is not None:
        avg_price = (high_price + low_price) / 2
    else:
        avg_price = None

    return high_price, low_price, avg_price

# Load the CSV into a DataFrame
leagues_rewards = pd.read_csv("data/leagues-rewards.csv")

# Load the item mapping JSON
with open("data/item_mapping.json", "r", encoding="utf-8") as f:
    item_mapping = json.load(f)

# Create a lookup dictionary: item name -> id
name_to_id = {item["name"].lower(): item["id"] for item in item_mapping}

# Create the new id column by matching Item Name to name
leagues_rewards["id"] = leagues_rewards["Item Name"].str.lower().map(name_to_id)

# Optional: print any items that could not be matched
unmatched = leagues_rewards[leagues_rewards["id"].isna()]["Item Name"].unique()
if len(unmatched) > 0:
    print("Unmatched items:")
    for item in unmatched:
        print(f"  - {item}")

print(f"Matched {leagues_rewards['id'].notna().sum()} of {len(leagues_rewards)} items")

