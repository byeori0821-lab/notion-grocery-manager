"""Daily inventory check: expiration warnings + auto-restock."""

from datetime import datetime, timedelta
from config import INVENTORY_DB, SHOPPING_DB
from notion_client import query_database, create_page, update_page


def check_expiration(today=None):
    today = today or datetime.now()
    items = query_database(INVENTORY_DB)
    updated = 0

    for page in items["results"]:
        props = page["properties"]
        name = "".join(t["plain_text"] for t in props["이름 品名"]["title"])
        status = (props.get("상태", {}).get("select") or {}).get("name", "")
        cat = (props.get("분류", {}).get("select") or {}).get("name", "")
        purchase = props.get("구매일", {}).get("date")

        if status in ("❌ 다 씀", "🔄 보충필요") or "냉동" in status or "약품" in cat:
            continue
        if not purchase or not purchase.get("start"):
            continue

        days = (today - datetime.strptime(purchase["start"], "%Y-%m-%d")).days
        new_status = _classify(cat, days)

        if new_status and new_status != status:
            update_page(page["id"], {"상태": {"select": {"name": new_status}}})
            print(f"  {name}: {status} → {new_status} ({days}일)")
            updated += 1

    return updated


def auto_restock():
    restock_items = query_database(
        INVENTORY_DB,
        {"property": "상태", "select": {"equals": "🔄 보충필요"}},
    )

    existing = query_database(SHOPPING_DB)
    existing_names = set()
    for p in existing["results"]:
        for v in p["properties"].values():
            if v["type"] == "title":
                existing_names.add("".join(t["plain_text"] for t in v.get("title", [])))

    added = 0
    for page in restock_items["results"]:
        props = page["properties"]
        name = "".join(t["plain_text"] for t in props["이름 品名"]["title"])
        if name in existing_names:
            continue

        source = (props.get("출처", {}).get("select") or {}).get("name")
        icon = page.get("icon", {})

        shop_props = {
            "품목 品名": {"title": [{"text": {"content": name}}]},
            "긴급도": {"select": {"name": "🔴 지금 당장"}},
            "산다 买了": {"checkbox": False},
            "비고": {"rich_text": [{"text": {"content": "보충필요 → 자동 추가됨"}}]},
        }
        if source:
            shop_props["어디서 去哪买"] = {"select": {"name": source}}

        create_page(
            SHOPPING_DB, shop_props,
            icon.get("emoji") if icon.get("type") == "emoji" else None,
        )
        update_page(page["id"], {"상태": {"select": {"name": "❌ 다 씀"}}})
        print(f"  ✓ {name} → 补货清单")
        added += 1

    return added


def _classify(category, days):
    if "채소" in category or "과일" in category:
        if days >= 5: return "⚠️ 빨리 먹어!"
        if days >= 3: return "📌 이번 주에 쓰자"
    elif "유제품" in category:
        if days >= 10: return "⚠️ 빨리 먹어!"
        if days >= 7: return "📌 이번 주에 쓰자"
    elif "냉장" in category:
        if days >= 5: return "⚠️ 빨리 먹어!"
        if days >= 3: return "📌 이번 주에 쓰자"
    return None
