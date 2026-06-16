# 🛒 Notion Grocery & Inventory Manager

> ADHD-friendly smart grocery management system powered by Notion API

一个基于 Notion API 的智能库存管理系统，专为 ADHD 用户设计。通过发票自动解析、过期预警、药品余量追踪、跨平台提醒推送，让"买了什么、还剩什么、该买什么"变得零负担。

## ✨ Features

### 📦 Smart Inventory Tracking
- PDF receipt/invoice auto-parsing → categorized inventory entry
- Auto-classification into 10+ categories (beverages, produce, frozen, dairy, etc.)
- Expiration-based status updates (✅ OK → 📌 eat this week → ⚠️ eat now!)
- Frozen item tracking (🧊 separate slow-consume timeline)

### 💊 Medicine Inventory
- Daily remaining dose calculation
- **7-day advance restock alert** — medications cannot run out
- Multi-brand consolidation (e.g., same drug, different brands → unified tracking)

### 🛒 Auto Restock Workflow
- Mark "🔄 needs restock" → auto-added to shopping list
- Mark "❌ used up" → archived, NOT auto-added (prevents impulse repurchase)
- Duplicate detection before adding to shopping list

### 📊 Spending Analysis
- Category breakdown with text-based progress bars (no paid Notion plan needed)
- Per-store comparison (Hema vs Xiaoxiang)
- Monthly/weekly spending summaries

### 🥗 Nutrition Reminders
- Alerts when produce ratio drops below threshold
- Vitamin C fruit tracking
- **Anxiety-aware**: never suggests eliminating sugar/sweet beverages entirely

### 🔔 Cross-Platform Notifications
- **macOS Reminders** — native reminder creation via AppleScript
- **Google Calendar** — medication restock events (syncs to Android)
- **Claude Push Notifications** — daily routine summary

## 🏗 Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  PDF Receipt │────▶│  receipt_parser   │────▶│   Notion API    │
│  (盒马/小象)  │     │  auto-classify    │     │  Inventory DB   │
└─────────────┘     └──────────────────┘     │  Shopping DB    │
                                              │  Purchase DB    │
┌─────────────┐     ┌──────────────────┐     └────────┬────────┘
│  Daily Cron  │────▶│ inventory_check   │             │
│  (routine)   │     │ medicine_tracker  │◀────────────┘
└─────────────┘     └──────┬───────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
     ┌──────────────┐ ┌────────┐ ┌──────────────┐
     │macOS Reminders│ │ Claude │ │Google Calendar│
     │  (AppleScript)│ │ Push   │ │  (URL scheme) │
     └──────────────┘ └────────┘ └──────────────┘
```

## 📁 Project Structure

```
notion-grocery-manager/
├── src/
│   ├── config.py            # Environment variables & Notion IDs
│   ├── notion_client.py     # Lightweight Notion API client (stdlib only)
│   ├── inventory_check.py   # Expiration check + auto-restock logic
│   ├── medicine_tracker.py  # Medicine dose calculation & alerts
│   ├── receipt_parser.py    # PDF invoice → Notion auto-entry
│   └── notifications.py     # macOS Reminders + Google Calendar
├── .env.example             # Template for environment variables
├── .gitignore
└── README.md
```

## 🚀 Setup

1. Clone this repo
2. Copy `.env.example` to `.env` and fill in your Notion API credentials
3. [Create a Notion integration](https://www.notion.so/my-integrations) and share your databases with it
4. Run any module directly:

```bash
export $(cat .env | xargs)
cd src
python3 inventory_check.py
```

## 🧠 Design Philosophy: ADHD-Friendly

This system is designed with ADHD users in mind:

- **Zero manual data entry** — upload a receipt screenshot, everything auto-populates
- **No guilt design** — "used up" ≠ "you need to buy more". Only restock what you actively choose
- **Visual differentiation** — every item has a category emoji, color-coded statuses
- **Low decision fatigue** — automated suggestions, not overwhelming options
- **Gentle reminders** — Korean casual tone, no motivational slogans
- **One-tap actions** — change status with a single click in Notion

## 🛠 Tech Stack

- **Python 3** (stdlib only — no pip dependencies)
- **Notion API** (2022-06-28)
- **AppleScript** (macOS Reminders integration)
- **Google Calendar URL Scheme** (cross-platform calendar events)

## 📄 License

MIT
