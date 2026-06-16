# 🛒 Notion Grocery Manager — Zero-Input Smart Inventory System

### 🇺🇸 [English](#english) · 🇨🇳 [中文](#中文) · 🇰🇷 [한국어](#한국어)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Notion API](https://img.shields.io/badge/Notion-API-000?logo=notion&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-AI_Powered-orange?logo=anthropic&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Android%20%7C%20iOS-lightgrey)

> **Upload a receipt. Everything else is automatic.**

```
📸 Receipt photo/PDF ──▶ Claude (AI parse) ──▶ Notion Inventory
                                                ├── 📦 Auto-categorized items
                                                ├── 📊 Spending analysis
                                                ├── ⏰ Expiration alerts
                                                ├── 💊 Medicine tracking
                                                └── 🔔 Cross-platform reminders
```

---

## 🏗 Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  PDF Receipt │────▶│  Claude AI       │────▶│   Notion API    │
│  (photo/PDF) │     │  + receipt_parser │     │  ┣ Inventory DB │
└─────────────┘     └──────────────────┘     │  ┣ Shopping DB  │
                                              │  ┗ Purchase DB  │
┌─────────────┐     ┌──────────────────┐     └────────┬────────┘
│  Daily Cron  │────▶│ inventory_check   │             │
│  (Claude     │     │ medicine_tracker  │◀────────────┘
│   Scheduled) │     └──────┬───────────┘
└─────────────┘            │
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

You buy groceries worth ¥500. Three days later you can't remember what's in your fridge. Vegetables rot. You buy duplicates. Medicine runs out because you forgot to refill.

Traditional inventory apps fail because they demand **manual input for every item** — nobody keeps that up.

### How It Works

This system is powered by **[Claude](https://claude.ai) + Notion API**. Claude acts as the AI brain that parses your receipts and manages your inventory. Here's the actual workflow:

#### 📸 Step 1: Upload a Receipt

Send a receipt photo or PDF to Claude (via Claude Desktop App, Claude Code, or claude.ai):

```
You:  [attach receipt.pdf]
      "这是今天盒马的小票，帮我录入"

Claude: ✓ Parsed 31 items from 盒马
        ✓ Auto-categorized into 8 categories
        ✓ Added to Notion inventory
```

That's it. No forms. No manual entry. Just send the receipt.

#### ⏰ Step 2: Daily Auto-Check (Runs by Itself)

A scheduled routine runs every morning and automatically:
- Checks what's expiring → updates status (✅ → 📌 → ⚠️)
- Calculates medicine remaining doses
- Moves "needs restock" items to shopping list
- Updates spending analysis & nutrition reminders
- Sends push notifications + macOS Reminders

#### 🛒 Step 3: Go Shopping

Open Notion on your phone → check the shopping list → done.

### Setup Guide (15 minutes)

#### Prerequisites
- A [Notion](https://notion.so) account (free plan works)
- [Claude](https://claude.ai) account with Claude Code or Claude Desktop App
- Python 3.9+ (pre-installed on macOS)

#### 1. Set Up Notion

1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click **+ New integration** → name it `Grocery Manager` → Submit
3. Copy the **Internal Integration Secret** (starts with `ntn_`)
4. Create a new page in Notion → share it with your integration (click `···` → Connections → add your integration)

#### 2. Clone This Repo

```bash
git clone https://github.com/byeori0821-lab/notion-grocery-manager.git
cd notion-grocery-manager
cp .env.example .env
```

#### 3. Configure

Edit `.env` with your Notion credentials:
```
NOTION_TOKEN=ntn_your_token_here
INVENTORY_DB=your_inventory_database_id
SHOPPING_DB=your_shopping_list_database_id
PURCHASE_DB=your_purchase_history_database_id
GROCERY_PAGE=your_grocery_page_id
```

> **How to find Database IDs:** Open the database in Notion as a full page → the URL looks like `notion.so/abc123def456...` → that `abc123def456` part is the ID.

#### 4. Initialize Databases

```bash
export $(cat .env | xargs)
cd src
python3 -c "
from notion_client import api
# This creates the required database structure in your Notion page
print('Setting up databases...')
# See docs/setup.md for full initialization script
"
```

#### 5. Set Up Daily Routine (Optional)

If using Claude Code, place the routine config in:
```
~/.claude/scheduled-tasks/grocery-inventory-check/SKILL.md
```
See [SKILL.md template](docs/SKILL_TEMPLATE.md) in this repo.

#### 6. Start Using

Send any grocery receipt to Claude with:
> "이거 장보기 영수증이야, 재고에 넣어줘" / "这是今天的小票，帮我录入库存"

Done. Everything flows from there.

### Features

| Feature | How |
|---|---|
| **Receipt parsing** | Send PDF/photo to Claude → auto-categorized into Notion |
| **Expiration tracking** | Daily auto-check: cut fruit 1d, bread 5d, frozen 30d+ |
| **Smart restock** | "Used up" ≠ auto-rebuy. Only "needs restock" enters shopping list |
| **Medicine tracking** | Daily dose calc, 7-day advance alert, can't run out |
| **Spending analysis** | Category breakdown, store comparison (text charts, no paid plan) |
| **Nutrition nudges** | Low produce ratio alert, vitamin C fruit reminder |
| **Notifications** | macOS Reminders + Google Calendar + Claude push |

### Design Philosophy

Built for people who've tried every productivity app and quit them all:

- **Zero manual entry** — send a receipt, done
- **No guilt** — "used up" just archives. You decide what to rebuy
- **Visual-first** — emoji icons, color-coded statuses
- **One-tap actions** — change status with a single click
- **Gentle tone** — like a friend reminding you, not a productivity coach

---

<a id="中文"></a>
## 🇨🇳 中文

### 痛点

盒马下单500块，三天后打开冰箱已经忘了买过什么。蔬菜烂了、东西重复买、药吃完了才发现忘了续。

传统库存App全都要**手动录入每一件商品**——没人能坚持。

### 它是怎么工作的

这套系统由 **[Claude](https://claude.ai)（AI助手）+ Notion API** 驱动。Claude 负责解析小票、管理库存，你只需要动动手指。

#### 📸 第1步：上传小票

把小票拍照或PDF发给 Claude（通过 Claude 桌面端、Claude Code 或 claude.ai 网页版）：

```
你：  [附上 receipt.pdf]
     "这是今天盒马的小票，帮我录入"

Claude: ✓ 解析了31件商品
        ✓ 自动分成8个类别
        ✓ 已录入 Notion 库存
```

不用填表、不用手动输入，发小票就行。

#### ⏰ 第2步：每日自动巡检（自己跑）

每天早上自动执行：
- 检查快过期的 → 更新状态（✅充足 → 📌这周吃 → ⚠️赶紧吃）
- 计算药品剩余天数
- 把标了"需要补货"的自动搬进购物清单
- 更新消费分析和营养提醒
- 发推送通知 + macOS提醒

#### 🛒 第3步：去超市

手机打开 Notion → 看购物清单 → 搞定。

### 安装教程（15分钟）

#### 你需要准备
- [Notion](https://notion.so) 账号（免费版就行）
- [Claude](https://claude.ai) 账号（需要 Claude Code 或 Claude 桌面端）
- Python 3.9+（macOS 自带）

#### 1. 配置 Notion

1. 打开 [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. 点 **+ 新建集成** → 名字写 `Grocery Manager` → 提交
3. 复制 **Internal Integration Secret**（以 `ntn_` 开头的那串）
4. 在 Notion 新建一个页面 → 把集成连接上去（点 `···` → 连接 → 添加你的集成）

#### 2. 下载代码

```bash
git clone https://github.com/byeori0821-lab/notion-grocery-manager.git
cd notion-grocery-manager
cp .env.example .env
```

#### 3. 填入配置

编辑 `.env` 文件，填入你的 Notion 信息：
```
NOTION_TOKEN=ntn_你的token
INVENTORY_DB=库存数据库ID
SHOPPING_DB=购物清单数据库ID
PURCHASE_DB=采购记录数据库ID
GROCERY_PAGE=买菜页面ID
```

> **怎么找数据库ID：** 在 Notion 里把数据库全屏打开 → 看浏览器地址栏 `notion.so/abc123def456...` → 那串 `abc123def456` 就是ID。

#### 4. 开始使用

把任何一张超市小票发给 Claude：
> "这是今天盒马的小票，帮我录入库存"

完事。后面全自动。

### 功能清单

| 功能 | 说明 |
|---|---|
| **小票自动解析** | 发PDF/照片给Claude → 自动分类入Notion |
| **保质期追踪** | 每天自动检查：果切1天、面包5天、冷冻30天+ |
| **防冲动补货** | "吃完了"只归档，不自动回购。标"要补"才进清单 |
| **药品追踪** | 每天算剩余量，提前7天提醒去开处方 |
| **消费分析** | 分类/分店对比，文字进度条（不需付费版） |
| **营养提醒** | 速食占比过高、维C水果太久没买都会提醒 |
| **跨平台通知** | macOS提醒事项 + Google日历 + Claude推送 |

### 设计理念

为"试过所有效率App最后全放弃了"的人设计：

- **零手动录入** — 拍小票就行
- **没有负罪感** — "吃完了"不催你回购，想买才买
- **视觉优先** — 每件商品有emoji、状态有颜色
- **一步操作** — 改状态点一下，没有表单
- **说人话** — 不写"坚持就是胜利"

---

<a id="한국어"></a>
## 🇰🇷 한국어

### 문제

허마에서 500위안어치 장을 봤는데, 3일 후 냉장고에 뭐가 있는지 기억이 안 남. 채소는 썩고, 같은 거 또 사고, 약은 다 먹고 나서야 알아챔.

기존 재고 관리 앱은 전부 **하나하나 수동 입력**해야 해서 아무도 안 씀.

### 어떻게 작동하나

**[Claude](https://claude.ai) (AI 어시스턴트) + Notion API** 로 돌아감. Claude가 영수증 읽고 재고 관리해줌. 너는 사진 보내기만 하면 됨.

#### 📸 1단계: 영수증 보내기

영수증 사진이나 PDF를 Claude한테 보냄 (Claude 데스크톱 앱, Claude Code, 또는 claude.ai):

```
나:    [receipt.pdf 첨부]
      "오늘 허마 영수증이야, 재고에 넣어줘"

Claude: ✓ 31개 상품 파싱 완료
        ✓ 8개 카테고리로 자동 분류
        ✓ Notion 재고에 추가됨
```

양식 작성 없음. 수동 입력 없음. 영수증만 보내면 끝.

#### ⏰ 2단계: 매일 자동 체크 (알아서 돌아감)

매일 아침 자동으로:
- 유통기한 체크 → 상태 업데이트 (✅ → 📌 → ⚠️)
- 약 남은 양 계산
- "보충필요" 표시한 거 → 장바구니로 이동
- 소비 분석 & 영양 리마인더 업데이트
- 푸시 알림 + macOS 미리알림

#### 🛒 3단계: 장보러 가기

폰에서 Notion 열고 → 장바구니 확인 → 끝.

### 설치 가이드 (15분)

#### 준비물
- [Notion](https://notion.so) 계정 (무료 플랜 OK)
- [Claude](https://claude.ai) 계정 (Claude Code 또는 Claude 데스크톱 앱)
- Python 3.9+ (macOS에 기본 설치됨)

#### 1. Notion 설정

1. [notion.so/my-integrations](https://www.notion.so/my-integrations) 열기
2. **+ New integration** → 이름: `Grocery Manager` → 제출
3. **Internal Integration Secret** 복사 (`ntn_`으로 시작하는 거)
4. Notion에서 새 페이지 만들기 → 인테그레이션 연결 (`···` → 연결 → 추가)

#### 2. 코드 다운로드

```bash
git clone https://github.com/byeori0821-lab/notion-grocery-manager.git
cd notion-grocery-manager
cp .env.example .env
```

#### 3. 설정

`.env` 파일에 Notion 정보 입력:
```
NOTION_TOKEN=ntn_너의토큰
INVENTORY_DB=재고DB아이디
SHOPPING_DB=장바구니DB아이디
PURCHASE_DB=구매기록DB아이디
GROCERY_PAGE=장보기페이지아이디
```

> **데이터베이스 ID 찾는 법:** Notion에서 DB를 전체 페이지로 열기 → 주소창에서 `notion.so/abc123def456...` → 그 `abc123def456` 부분이 ID.

#### 4. 사용 시작

아무 영수증이나 Claude한테 보내기:
> "이거 오늘 장본 영수증이야, 재고에 넣어줘"

끝. 나머지는 다 자동.

### 기능

| 기능 | 설명 |
|---|---|
| **영수증 자동 파싱** | PDF/사진을 Claude한테 보내면 → Notion에 자동 분류 입력 |
| **유통기한 추적** | 매일 자동 체크: 과일컷 1일, 빵 5일, 냉동 30일+ |
| **충동구매 방지** | "다 씀" = 그냥 정리됨. "보충필요"만 장바구니에 들어감 |
| **약 재고 추적** | 매일 남은 양 계산, 7일 전에 병원 가라고 알림 |
| **소비 분석** | 카테고리/매장별 비교, 텍스트 차트 (유료 플랜 불필요) |
| **영양 리마인더** | 즉석식품 비율 높으면 알림, 비타민C 과일 오래 안 샀으면 알림 |
| **크로스 플랫폼 알림** | macOS 미리알림 + Google 캘린더 + Claude 푸시 |

### 설계 철학

생산성 앱 다 깔아보고 다 포기한 사람을 위해 만듦:

- **수동 입력 제로** — 영수증만 보내면 됨
- **죄책감 없음** — "다 씀" = 정리됨. 다시 살지는 네가 정해
- **시각 우선** — 이모지 아이콘, 색상별 상태 구분
- **원클릭** — 상태 바꾸기 한 번 클릭
- **자연스러운 말투** — "화이팅!" 안 씀. 친구가 알려주는 느낌

---

## 🛠 Tech Stack

- **Python 3.9+** — stdlib only, zero pip dependencies
- **Notion API** (2022-06-28) — database CRUD, block management
- **Claude AI** — receipt parsing, scheduled routines, push notifications
- **AppleScript** — macOS Reminders integration
- **Google Calendar URL Scheme** — cross-platform calendar events

## 📄 License

MIT

## 👤 Author

**Agnies** — [@byeori0821-lab](https://github.com/byeori0821-lab)
