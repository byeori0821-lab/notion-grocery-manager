#!/usr/bin/env python3
"""
Import parsed receipt JSON into Notion inventory.

Usage:
  1. Send your receipt + prompt to ANY AI (ChatGPT/Claude/Gemini/Kimi/...)
  2. Copy the JSON output
  3. Run: python3 import_receipt.py receipt.json
     Or:  python3 import_receipt.py            (paste JSON interactively)

The AI only does the OCR/parsing. Everything else runs locally.
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from config import INVENTORY_DB, PURCHASE_DB
from notion_client import create_page
from receipt_parser import classify_item, guess_emoji


def import_from_json(data):
    store = data.get("store", "기타")
    date = data.get("date", "")
    items = data.get("items", [])

    if not items:
        print("No items found in JSON.")
        return 0

    print(f"Store: {store}")
    print(f"Date:  {date}")
    print(f"Items: {len(items)}")
    print("-" * 40)

    added = 0
    total = 0
    for item in items:
        name = item.get("name", "")
        price = item.get("price", 0)
        qty = str(item.get("qty", "1"))
        if not name:
            continue

        category = classify_item(name)
        emoji = guess_emoji(name)
        total += price

        create_page(INVENTORY_DB, {
            "이름 品名": {"title": [{"text": {"content": name}}]},
            "분류": {"select": {"name": category}},
            "가격 价格": {"number": price},
            "수량": {"rich_text": [{"text": {"content": qty}}]},
            "출처": {"select": {"name": store}},
            "구매일": {"date": {"start": date}},
            "상태": {"select": {"name": "✅ 충분"}},
        }, icon_emoji=emoji)

        create_page(PURCHASE_DB, {
            "이름 品名": {"title": [{"text": {"content": name}}]},
            "가격 价格": {"number": price},
            "출처": {"select": {"name": store}},
            "구매일": {"date": {"start": date}},
        }, icon_emoji=emoji)

        print(f"  {emoji} {name}  ¥{price}  [{category}]")
        added += 1

    print("-" * 40)
    print(f"✅ {added} items added | Total: ¥{total:.2f}")
    return added


def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        print("Paste the JSON from your AI, then press Enter twice:")
        print("(或粘贴AI输出的JSON，按两次回车)")
        print()
        lines = []
        empty_count = 0
        while True:
            try:
                line = input()
                if line.strip() == "":
                    empty_count += 1
                    if empty_count >= 2:
                        break
                else:
                    empty_count = 0
                lines.append(line)
            except EOFError:
                break

        text = "\n".join(lines).strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1]
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0]
        data = json.loads(text)

    import_from_json(data)


if __name__ == "__main__":
    main()
