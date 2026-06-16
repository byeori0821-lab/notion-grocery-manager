"""Track medicine inventory and alert before running out."""

from datetime import datetime, timedelta
from config import INVENTORY_DB
from notion_client import query_database, update_page


# Initial stock recorded on 2026-06-16
INITIAL_DATE = datetime(2026, 6, 16)
MEDICINES = {
    "舍曲林": {
        "initial": {"左洛复50mg": 5, "快五优25mg": 84},
        "daily_dose": {"左洛复50mg": 1, "快五优25mg": 2},
        "order": ["左洛复50mg", "快五优25mg"],
    },
    "异维A酸": {
        "initial_count": 17,
        "interval_days": 2,
    },
}
RESTOCK_LEAD_DAYS = 7


def check_medicines(today=None):
    today = today or datetime.now()
    days_passed = (today - INITIAL_DATE).days

    med_items = query_database(
        INVENTORY_DB,
        {"property": "분류", "select": {"equals": "💊 약품"}},
    )

    results = []
    for page in med_items["results"]:
        name = "".join(t["plain_text"] for t in page["properties"]["이름 品名"]["title"])

        if "舍曲林" in name:
            info = _calc_sertraline(days_passed)
        elif "异维" in name:
            info = _calc_isotretinoin(days_passed)
        else:
            continue

        update_page(page["id"], {
            "수량": {"rich_text": [{"text": {"content": info["qty_text"]}}]},
            "비고 备注": {"rich_text": [{"text": {"content": info["note"]}}]},
            "상태": {"select": {"name": info["status"]}},
        })
        print(f"  💊 {name}: {info['qty_text']} · {info['days_left']}일분 · {info['status']}")
        results.append({"name": name, **info})

    return results


def _calc_sertraline(days_passed):
    zuo_left = max(0, 5 - days_passed)
    if zuo_left > 0:
        kuai_left = 84
        total_days = zuo_left + kuai_left // 2
        qty = f"左洛复{zuo_left}粒 + 快五优{kuai_left}粒"
    else:
        kuai_used = (days_passed - 5) * 2
        kuai_left = max(0, 84 - kuai_used)
        total_days = kuai_left // 2
        qty = f"左洛复已用完 · 快五优{kuai_left}粒"

    end = INITIAL_DATE + timedelta(days=days_passed + total_days)
    restock = end - timedelta(days=RESTOCK_LEAD_DAYS)
    status = _status_by_days(total_days)
    note = f"약{total_days}일분 · 预计{end:%m/%d}用完 · {restock:%m/%d}前补货"
    return {"qty_text": qty, "days_left": total_days, "status": status, "note": note, "end_date": end}


def _calc_isotretinoin(days_passed):
    used = days_passed // 2
    left = max(0, 17 - used)
    days_left = left * 2
    end = INITIAL_DATE + timedelta(days=days_passed + days_left)
    restock = end - timedelta(days=RESTOCK_LEAD_DAYS)
    status = _status_by_days(days_left)
    note = f"隔1~2天1粒 · 预计{end:%m/%d}用完 · {restock:%m/%d}前补货"
    return {"qty_text": f"{left}粒", "days_left": days_left, "status": status, "note": note, "end_date": end}


def _status_by_days(days_left):
    if days_left <= 7:
        return "🔄 보충필요"
    if days_left <= 14:
        return "📌 이번 주에 쓰자"
    return "✅ 충분"
