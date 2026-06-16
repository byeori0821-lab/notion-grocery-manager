# 🛒 Notion Grocery Manager — Zero-Input Smart Inventory System

### 🇺🇸 [English](#english) · 🇨🇳 [中文](#中文) · 🇰🇷 [한국어](#한국어)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Notion API](https://img.shields.io/badge/Notion-API-000?logo=notion&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Android%20%7C%20iOS-lightgrey)

> **Upload a receipt. Everything else is automatic.**

```
📸 Receipt photo → 🤖 Auto-parse → 📦 Categorized inventory
                                   → 📊 Spending analysis
                                   → ⏰ Expiration alerts
                                   → 💊 Medicine tracking
                                   → 🔔 Cross-platform reminders
```

---

## 🏗 Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  PDF Receipt │────▶│  receipt_parser   │────▶│   Notion API    │
│  盒马/小象/山姆 │     │  auto-classify    │     │  ┣ Inventory DB │
└─────────────┘     └──────────────────┘     │  ┣ Shopping DB  │
                                              │  ┗ Purchase DB  │
┌─────────────┐     ┌──────────────────┐     └────────┬────────┘
│  Daily Cron  │────▶│ inventory_check   │             │
│  (scheduled) │     │ medicine_tracker  │◀────────────┘
└─────────────┘     └──────┬───────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
     ┌──────────────┐ ┌────────┐ ┌──────────────┐
     │macOS Reminders│ │ Push   │ │Google Calendar│
     │  (AppleScript)│ │Notify  │ │  (URL scheme) │
     └──────────────┘ └────────┘ └──────────────┘
```

## 📁 Structure

```
src/
├── config.py              # Environment variables
├── notion_client.py       # Notion API client (zero dependencies)
├── inventory_check.py     # Expiration + auto-restock
├── medicine_tracker.py    # Dose calculation + alerts
├── receipt_parser.py      # PDF invoice → auto-entry
└── notifications.py       # macOS Reminders + Google Calendar
```

---

<a id="english"></a>
## 🇺🇸 English

### The Problem

You buy groceries worth ¥500. Three days later you can't remember what's in your fridge. Vegetables rot. You buy duplicates. Medicine runs out because you forgot to refill. Sound familiar?

Traditional inventory apps fail because they demand **manual input for every item** — nobody keeps that up.

### The Solution

**Upload a receipt screenshot. That's it.** This system does the rest:

- **Auto-parse & categorize** — PDF invoices from Hema (盒马), Xiaoxiang (小象超市), Sam's Club get parsed and sorted into 10+ categories with emoji icons
- **Expiration intelligence** — knows that cut fruit lasts 1 day, bread lasts 5 days, frozen food lasts months. Updates status automatically every day
- **Smart restock flow** — "used up" ≠ "buy again". Items only enter the shopping list when you explicitly mark them for restock. Prevents impulse repurchasing
- **Medicine tracking** — calculates remaining doses daily, alerts 7 days before you run out. Medications cannot be allowed to lapse
- **Spending analysis** — category breakdown, store comparison, monthly trends. All rendered in Notion with text-based charts (no paid plan needed)
- **Nutrition nudges** — flags when your produce ratio drops too low, or when you haven't bought vitamin C-rich fruit in 2 weeks
- **Cross-platform alerts** — macOS Reminders (AppleScript), Google Calendar (syncs to Android/iOS), push notifications

### Design Principles

This isn't just an inventory tracker — it's designed for people who've tried every productivity app and quit them all:

| Principle | Implementation |
|---|---|
| **Zero manual entry** | Receipt upload → everything auto-populates |
| **No guilt** | "Used up" is archived, not added to buy-again. You choose what to restock |
| **Visual-first** | Every item has a category emoji. Color-coded statuses at a glance |
| **Low friction** | Change status with a single click. No forms, no fields to fill |
| **Gentle tone** | Casual reminders, not productivity guilt trips |
| **Works offline** | Notion mobile app works at the supermarket |

### Quick Start

```bash
git clone https://github.com/byeori0821-lab/notion-grocery-manager.git
cd notion-grocery-manager
cp .env.example .env
# Fill in your Notion API token and database IDs in .env
export $(cat .env | xargs)
cd src && python3 inventory_check.py
```

### Requirements

- Python 3.9+ (stdlib only — zero pip dependencies)
- A [Notion integration](https://www.notion.so/my-integrations) with read/write access
- macOS (for Reminders integration; optional)

---

<a id="中文"></a>
## 🇨🇳 中文

### 痛点

盒马下单500块，三天后打开冰箱已经忘了买过什么。蔬菜烂了、东西重复买、药吃完了才发现忘了续。

传统库存App全都要**手动录入每一件商品**——没人能坚持。

### 解决方案

**上传一张小票截图，剩下的全自动。**

- **发票自动解析** — 盒马/小象超市/山姆的PDF发票，自动识别商品、分类、加emoji图标入库
- **保质期智能判断** — 鲜切水果1天、面包5天、冷冻食品按月。每天自动更新状态：✅充足 → 📌这周吃掉 → ⚠️赶紧吃
- **防冲动补货** — 标了"用完了"不会自动进购物清单。只有你主动标"需要补货"的才会进。省得逛超市管不住手
- **药品追踪** — 每天计算剩余量，**提前7天**提醒你去医院开处方。药不能断
- **消费分析** — 分类占比、分店对比、月度趋势，全在Notion里用文字进度条展示（不需要付费版）
- **营养提醒** — 速食占比过高会提醒、两周没买维C水果会提醒
- **跨平台通知** — macOS提醒事项 + Google日历（安卓/iOS同步） + 推送通知

### 设计理念

这不只是一个库存管理工具——是为"试过所有效率App最后全放弃了"的人设计的：

- **零手动录入** — 拍小票就行，别的不用管
- **没有负罪感** — "吃完了"只是归档，不会催你回购。想买才买
- **视觉优先** — 每件商品有分类emoji，状态一眼看清
- **最低操作成本** — 改个状态点一下就行，没有表单要填
- **说人话** — 不写"坚持就是胜利"这种东西，像朋友提醒你一样

### 快速开始

```bash
git clone https://github.com/byeori0821-lab/notion-grocery-manager.git
cd notion-grocery-manager
cp .env.example .env
# 在 .env 里填入你的 Notion API Token 和数据库ID
export $(cat .env | xargs)
cd src && python3 inventory_check.py
```

### 环境要求

- Python 3.9+（纯标准库，不需要pip安装任何依赖）
- [Notion Integration](https://www.notion.so/my-integrations)（需要读写权限）
- macOS（提醒事项联动用，可选）

---

<a id="한국어"></a>
## 🇰🇷 한국어

### 문제

허마에서 500위안어치 장을 봤는데, 3일 후 냉장고에 뭐가 있는지 기억이 안 남. 채소는 썩고, 같은 거 또 사고, 약은 다 먹고 나서야 알아챔.

기존 재고 관리 앱은 전부 **하나하나 수동 입력**해야 하니까 아무도 안 함.

### 해결

**영수증 캡처 한 장 올리면 끝. 나머지는 전부 자동.**

- **영수증 자동 파싱** — 허마/샤오샹/샘스클럽 PDF 영수증 → 자동 분류 + 이모지 아이콘 배정
- **유통기한 자동 판단** — 과일컷 1일, 빵 5일, 냉동식품 한 달. 매일 상태 자동 업데이트: ✅여유 → 📌이번 주에 먹자 → ⚠️빨리 먹어!
- **충동구매 방지** — "다 씀"으로 바꿔도 자동으로 장바구니에 안 들어감. "보충필요"로 표시한 것만 들어감
- **약 재고 추적** — 매일 남은 양 자동 계산, **7일 전에** 병원 가서 처방받으라고 알림. 약은 절대 끊기면 안 됨
- **소비 분석** — 카테고리별 비율, 매장별 비교, 월별 추이. Notion에서 텍스트 차트로 표시 (유료 플랜 불필요)
- **영양 리마인더** — 즉석식품 비율 너무 높으면 알림, 비타민C 과일 2주 이상 안 샀으면 알림
- **크로스 플랫폼 알림** — macOS 미리알림 + Google 캘린더(안드로이드/iOS 동기화) + 푸시 알림

### 설계 철학

생산성 앱 다 깔아보고 다 포기한 사람을 위해 만듦:

- **수동 입력 제로** — 영수증만 찍으면 됨
- **죄책감 없음** — "다 씀" = 그냥 정리됨. 다시 살지 말지는 네가 정해
- **시각 우선** — 모든 상품에 카테고리 이모지, 상태 색상 구분
- **최소 조작** — 상태 바꾸기 원클릭. 작성할 양식 없음
- **자연스러운 말투** — "화이팅!" 이런 거 안 씀. 친구가 알려주는 느낌

### 시작하기

```bash
git clone https://github.com/byeori0821-lab/notion-grocery-manager.git
cd notion-grocery-manager
cp .env.example .env
# .env에 Notion API 토큰과 데이터베이스 ID 입력
export $(cat .env | xargs)
cd src && python3 inventory_check.py
```

### 요구사항

- Python 3.9+ (표준 라이브러리만 사용, pip 설치 필요 없음)
- [Notion Integration](https://www.notion.so/my-integrations) (읽기/쓰기 권한)
- macOS (미리알림 연동용, 선택사항)

---

## 📄 License

MIT

## 👤 Author

**Agnies** — [@byeori0821-lab](https://github.com/byeori0821-lab)
