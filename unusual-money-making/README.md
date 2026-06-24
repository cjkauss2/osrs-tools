## Unusual Money Making
Realtime Old School Runescape money making calculator

For niche money making methods where protitability depends on flucuating grand exchange prices. Especially useful for low volume items or highly volatile items.

## How to Run

Update [money_makers.json](data/money_makers.json) with the methods you would like to check.

Run `python calculate_value.py`

The script will summarize the data

## When new items come out

[item_mapping.json](data/item_mapping.json) contains information on all items in OSRS (from the wiki real time prices API). If new items are released and you would like to check the profitability, run `python update_mapping.py` or copy them from [here](https://prices.runescape.wiki/api/v1/osrs/mapping).
