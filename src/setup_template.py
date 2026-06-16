#!/usr/bin/env python3
"""
Set up Notion Template: add formula columns for auto-calculation.
Run once to upgrade databases with self-updating formulas.

After running this, the template works WITHOUT any Python scripts:
- 경과일 auto-calculates days since purchase
- 신선도 auto-shows freshness alerts based on category
- Users just paste items into the table and everything updates
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from config import INVENTORY_DB, PURCHASE_DB
from notion_client import api

FRESHNESS_FORMULA = (
    'if(empty(prop("구매일")), "", '
    'if(contains(prop("분류"), "냉동"), "🧊 냉동보관중", '
    'if(or(contains(prop("분류"), "채소"), contains(prop("분류"), "과일")), '
    'if(dateBetween(now(), prop("구매일"), "days") >= 5, "⚠️ 빨리 먹어!", '
    'if(dateBetween(now(), prop("구매일"), "days") >= 3, "📌 이번 주에 쓰자", "✅ 신선")), '
    'if(contains(prop("분류"), "유제품"), '
    'if(dateBetween(now(), prop("구매일"), "days") >= 10, "⚠️ 빨리 먹어!", '
    'if(dateBetween(now(), prop("구매일"), "days") >= 7, "📌 이번 주에 쓰자", "✅ 신선")), '
    'if(contains(prop("분류"), "냉장"), '
    'if(dateBetween(now(), prop("구매일"), "days") >= 5, "⚠️ 빨리 먹어!", '
    'if(dateBetween(now(), prop("구매일"), "days") >= 3, "📌 이번 주에 쓰자", "✅ 신선")), '
    '"✅ OK")))))'
)

DAYS_FORMULA = (
    'if(empty(prop("구매일")), 0, '
    'dateBetween(now(), prop("구매일"), "days"))'
)


def setup_inventory_formulas():
    print("📦 Adding formula columns to inventory database...")
    api("PATCH", f"/databases/{INVENTORY_DB}", {
        "properties": {
            "경과일": {
                "formula": {"expression": DAYS_FORMULA}
            },
            "신선도": {
                "formula": {"expression": FRESHNESS_FORMULA}
            },
        }
    })
    print("  ✅ 경과일 (days elapsed) — auto-calculates")
    print("  ✅ 신선도 (freshness alert) — auto-updates by category")


def setup_purchase_month():
    print("\n💰 Adding month formula to purchase history...")
    api("PATCH", f"/databases/{PURCHASE_DB}", {
        "properties": {
            "월 Month": {
                "formula": {
                    "expression": 'if(empty(prop("구매일")), "", formatDate(prop("구매일"), "YYYY-MM"))'
                }
            },
        }
    })
    print("  ✅ 월 Month — auto-groups purchases by month")


def main():
    print("🔧 Setting up Notion Template formulas...\n")
    setup_inventory_formulas()
    setup_purchase_month()
    print("\n" + "=" * 50)
    print("✅ Done! Your databases now auto-calculate:")
    print("   📦 Inventory → 경과일 + 신선도 (no scripts needed)")
    print("   💰 Purchases → 월 Month (for monthly grouping)")
    print("\n💡 Tip: In Notion, group the inventory view by 신선도")
    print("   to see items that need attention at the top!")


if __name__ == "__main__":
    main()
