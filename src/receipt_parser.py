"""Parse PDF invoices/receipts and auto-populate Notion inventory."""

import json
import re
import subprocess
from config import INVENTORY_DB, PURCHASE_DB
from notion_client import create_page, query_database


CATEGORY_RULES = {
    "🥤 음료": ["水", "茶", "咖啡", "奶", "饮", "汽水", "气泡", "可可", "juice", "OATLY"],
    "🥬 채소/과일": ["蔬", "菜", "果", "番茄", "黄瓜", "生菜", "菌", "海带", "净菜", "根茎"],
    "🧊 냉동": ["冷冻", "速冻", "冻品", "水饺", "汤圆"],
    "🧊 냉장": ["冷藏", "鲜", "溏心蛋", "茶叶蛋", "卤"],
    "🥛 유제품": ["酸奶", "牛奶", "乳", "yogurt"],
    "🥫 저장식품": ["方便面", "干脆面", "零食", "薯片", "饼干", "坚果", "麦片", "Calbee", "Gemez"],
    "🧁 베이킹": ["面包", "蛋糕", "蛋挞", "贝果", "发糕", "糯米"],
}

EMOJI_MAP = {
    "음료": {"水": "💧", "茶": "🍵", "咖啡": "☕", "气泡": "🫧", "奶": "🥛"},
    "채소": "🥬", "과일": "🍎", "냉동": "🧊", "유제품": "🥛",
    "저장": "🥫", "베이킹": "🥐",
}


def classify_item(name):
    for category, keywords in CATEGORY_RULES.items():
        if any(kw.lower() in name.lower() for kw in keywords):
            return category
    return "🥫 저장식품"


def guess_emoji(name):
    for keyword, emoji in [
        ("水", "💧"), ("茶", "🍵"), ("咖啡", "☕"), ("气泡", "🫧"),
        ("奶", "🥛"), ("果", "🍎"), ("菜", "🥬"), ("菌", "🍄"),
        ("蛋", "🥚"), ("面", "🍜"), ("饼", "🍪"), ("糕", "🧁"),
        ("冰", "🧊"), ("酱", "🫙"), ("肉", "🥩"), ("鱼", "🐟"),
    ]:
        if keyword in name:
            return emoji
    return "📦"


def parse_and_insert(items, source, purchase_date):
    """Insert parsed receipt items into Notion inventory and purchase history.

    Args:
        items: list of {"name": str, "qty": str, "price": float}
        source: store name, e.g. "盒马", "小象超市"
        purchase_date: "YYYY-MM-DD"
    """
    added = 0
    for item in items:
        name = item["name"]
        price = item.get("price", 0)
        qty = item.get("qty", "1")
        category = classify_item(name)
        emoji = guess_emoji(name)

        create_page(INVENTORY_DB, {
            "이름 品名": {"title": [{"text": {"content": name}}]},
            "분류": {"select": {"name": category}},
            "가격 价格": {"number": price},
            "수량": {"rich_text": [{"text": {"content": str(qty)}}]},
            "출처": {"select": {"name": source}},
            "구매일": {"date": {"start": purchase_date}},
            "상태": {"select": {"name": "✅ 충분"}},
        }, icon_emoji=emoji)

        create_page(PURCHASE_DB, {
            "이름 品名": {"title": [{"text": {"content": name}}]},
            "가격 价格": {"number": price},
            "출처": {"select": {"name": source}},
            "구매일": {"date": {"start": purchase_date}},
        }, icon_emoji=emoji)

        added += 1

    return added
