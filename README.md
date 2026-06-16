# 🛒 Notion Grocery Manager — Smart Inventory Template

### 🇺🇸 [English](#english) · 🇨🇳 [中文](#中文) · 🇰🇷 [한국어](#한국어)

![Notion](https://img.shields.io/badge/Notion-Template-000?logo=notion&logoColor=white)
![AI Agnostic](https://img.shields.io/badge/AI-Any_Chatbot-blueviolet)
![Zero Install](https://img.shields.io/badge/Install-Zero-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-All_Devices-lightgrey)

> **One-click Notion template. Works with ANY AI. No coding needed.**

```
📸 Receipt / Order Screenshot
        │
        ▼
🤖 ANY AI (ChatGPT, Gemini, Kimi, 豆包, Claude...)
        │ "Parse this receipt"
        ▼
📋 Copy → Paste into Notion table
        │
        ▼
🛒 Notion auto-calculates everything:
   ├── 📦 Categorized inventory
   ├── ⏰ Freshness alerts (formula-powered)
   ├── 💊 Medicine tracking
   ├── 💰 Monthly spending breakdown
   └── 🛒 Smart shopping list
```

---

<a id="english"></a>
## 🇺🇸 English

### The Problem

You spend ¥500 on groceries. Three days later you can't remember what's in your fridge. Vegetables rot. You buy duplicates. Medicine runs out because you forgot to refill.

Traditional inventory apps fail because they demand **manual input for every item** — nobody keeps that up.

### The Solution: A Notion Template That Thinks

This is a **ready-to-use Notion template** with built-in formulas that auto-calculate freshness, track medicine doses, and organize your shopping list. No app to install. No code to run.

### How It Works (3 Steps)

#### 📸 Step 1: Send Receipt to ANY AI

Take a photo of your receipt or screenshot your order. Send it to **any chatbot** with this prompt:

> "Parse this receipt into a tab-separated table with columns: 이름 品名, 분류, 가격 价格, 수량, 출처, 구매일"

Works with: ChatGPT, Claude, Gemini, Kimi, 豆包, Copilot, DeepSeek, 通义 — any AI that can read images.

**Supports:** Paper receipts 📃, e-invoices 🧾, app order screenshots 📱 (盒马, 美团, 饿了么, 京东...), even multiple images at once 🖼️

#### 📋 Step 2: Paste into Notion

Copy the AI's table output → paste directly into the 📦 Inventory table in Notion. Done.

#### 🧮 Step 3: Everything Auto-Calculates

The template's built-in formulas handle the rest:
- **경과일 (Days)** — auto-counts days since purchase
- **신선도 (Freshness)** — auto-alerts based on food category:
  - 🥬 Vegetables/fruit: warn at 3 days, alert at 5 days
  - 🥛 Dairy: warn at 7 days, alert at 10 days
  - 🧊 Refrigerated: warn at 3 days, alert at 5 days
  - 🧊 Frozen: shows "🧊 냉동보관중" (safe in freezer)
  - 🥫 Shelf-stable: always OK
- **월 Month** — auto-groups purchases by month for spending analysis

### Status System

| Status | Meaning | What Happens |
|---|---|---|
| ✅ 충분 | Stocked | Nothing — you're good |
| 📌 이번 주에 쓰자 | Use this week | Gentle reminder |
| ⚠️ 빨리 먹어! | Eat it NOW | It's about to expire |
| 🔄 보충필요 | Need restock | → Goes to shopping list |
| ❌ 다 씀 | Used up | Archived. Does NOT auto-reorder |
| 🧊 냉동보관중 | In freezer | Relax, it's frozen |

### 💊 Medicine Tracking

Built-in medicine inventory with:
- Remaining dose calculation
- 7-day advance restock alert
- Status: ✅ 충분 → 📌 이번 주에 쓰자 → 🔄 보충필요

**Medications cannot run out.** The system alerts you a full week before you're empty.

### Quick Start (2 minutes)

1. **Duplicate** the Notion template (link below)
2. **Send** a receipt/order screenshot to any AI with the prompt
3. **Paste** the result into the inventory table
4. **Watch** the formulas auto-calculate everything

> 📎 [Get the template →](https://www.notion.so/381b6fe634e781faad5feff0f300cbd7)

### Pro Tips

- **Inventory board view** → Group by `신선도` to see ⚠️ items at the top
- **Monthly spending** → Group Purchase History by `월 Month`
- **Phone shopping** → Open Notion on your phone at the supermarket for the shopping list
- **Multiple screenshots** → Send 2-3 order screenshots to AI at once, it merges them

---

<a id="中文"></a>
## 🇨🇳 中文

### 痛点

盒马下单500块，三天后打开冰箱已经忘了买过什么。蔬菜烂了、东西重复买、药吃完了才发现忘了续。

所有库存App都要**手动录入每一件商品**——没人能坚持。

### 解决方案：一个会自动算的 Notion 模板

这是一个**即用型 Notion 模板**，内置公式自动计算新鲜度、追踪药品余量、管理补货清单。**不用装App，不用写代码。**

### 怎么用（3步）

#### 📸 第1步：把小票/订单截图发给任意AI

拍小票照片，或截订单页面。发给**任何一个AI聊天机器人**，附上这段话：

> "请解析这些购物记录，输出 Tab 分隔的表格，列名：이름 品名、분류、가격 价格、수량、출처、구매일"

支持的AI：ChatGPT、Claude、Gemini、Kimi、豆包、Copilot、DeepSeek、通义——只要能看图的AI都行。

**支持的输入：** 纸质小票📃、电子发票🧾、APP订单截图📱（盒马、美团、饿了么、京东、淘宝、山姆、多多买菜……）、多张图片一起发🖼️

**手机不支持长截图？** 截2-3张，一起发给AI，它会自动合并成一张表。

#### 📋 第2步：粘贴进 Notion

复制AI输出的表格 → 直接粘贴进 📦 库存表。完事。

#### 🧮 第3步：全部自动计算

模板内置公式自动处理：
- **경과일（天数）** — 自动算购买了几天
- **신선도（新鲜度）** — 根据食品类别自动提醒：
  - 🥬 蔬菜/水果：3天提醒，5天警告
  - 🥛 乳制品：7天提醒，10天警告
  - 🧊 冷藏：3天提醒，5天警告
  - 🧊 冷冻：显示"冷冻保管中"
  - 🥫 常温/饮料：一直OK
- **월 Month** — 自动按月份分组，看消费趋势

### 状态说明

| 状态 | 意思 | 会发生什么 |
|---|---|---|
| ✅ 충분 | 库存充足 | 啥也不用做 |
| 📌 이번 주에 쓰자 | 这周吃掉 | 温和提醒 |
| ⚠️ 빨리 먹어! | 赶紧吃！ | 快过期了 |
| 🔄 보충필요 | 需要补货 | → 进补货清单 |
| ❌ 다 씀 | 吃完了 | 归档，**不**自动回购 |
| 🧊 냉동보관중 | 冻着呢 | 不急，慢慢吃 |

### 💊 药品追踪

- 自动计算剩余量和剩余天数
- **提前7天**提醒补货（药不能断！）
- 状态：✅ 충분 → 📌 이번 주에 쓰자 → 🔄 보충필요

### 快速开始（2分钟）

1. **复制**下面的 Notion 模板
2. **发**小票/订单截图给任意AI，带上提示词
3. **粘贴**到库存表里
4. 公式**自动算**好一切

> 📎 [获取模板 →](https://www.notion.so/381b6fe634e781faad5feff0f300cbd7)

### 实用技巧

- **库存看板** → 按`신선도`分组，⚠️的自动排最前
- **月度消费** → 消费记录按`월 Month`分组
- **超市购物** → 去超市前手机打开Notion看补货清单
- **不支持长截图** → 截2-3张发给AI，自动合并

---

<a id="한국어"></a>
## 🇰🇷 한국어

### 문제

허마에서 500위안어치 장을 봤는데, 3일 후 냉장고에 뭐가 있는지 기억이 안 남. 채소는 썩고, 같은 거 또 사고, 약은 다 먹고 나서야 알아챔.

기존 재고 관리 앱은 전부 **하나하나 수동 입력**해야 해서 아무도 안 씀.

### 해결책: 알아서 계산하는 Notion 템플릿

**바로 쓸 수 있는 Notion 템플릿**. 내장 수식이 신선도, 약 잔량, 장바구니를 자동으로 관리. **앱 설치 불필요. 코딩 불필요.**

### 사용법 (3단계)

#### 📸 1단계: 영수증/주문 캡처를 아무 AI한테 보내기

영수증 사진 찍거나, 주문 페이지 캡처. **아무 AI 챗봇**한테 보내면서:

> "이 영수증을 탭 구분 표로 파싱해줘. 열: 이름 品名, 분류, 가격 价格, 수량, 출처, 구매일"

지원 AI: ChatGPT, Claude, Gemini, Kimi, 豆包, Copilot, DeepSeek, 通义 — 이미지 읽을 수 있는 AI면 다 됨.

**지원 입력:** 종이 영수증📃, 전자 영수증🧾, 앱 주문 캡처📱 (허마, 메이투안, 어러머, 징동...), 여러 장 동시 전송🖼️

**긴 스크린샷 안 되는 폰?** 2-3장 캡처해서 AI한테 같이 보내면 알아서 합쳐줌.

#### 📋 2단계: Notion에 붙여넣기

AI가 출력한 표를 복사 → 📦 재고 테이블에 바로 붙여넣기. 끝.

#### 🧮 3단계: 전부 자동 계산

템플릿 내장 수식이 알아서:
- **경과일** — 구매 후 며칠 지났는지 자동 계산
- **신선도** — 식품 분류별 자동 알림:
  - 🥬 채소/과일: 3일 주의, 5일 경고
  - 🥛 유제품: 7일 주의, 10일 경고
  - 🧊 냉장: 3일 주의, 5일 경고
  - 🧊 냉동: "냉동보관중" 표시
  - 🥫 저장식품/음료: 항상 OK
- **월 Month** — 월별 자동 그룹핑으로 소비 트렌드 확인

### 상태 시스템

| 상태 | 의미 | 일어나는 일 |
|---|---|---|
| ✅ 충분 | 재고 OK | 아무것도 안 해도 됨 |
| 📌 이번 주에 쓰자 | 이번 주에 먹기 | 부드러운 리마인더 |
| ⚠️ 빨리 먹어! | 지금 당장! | 곧 상함 |
| 🔄 보충필요 | 재구매 필요 | → 장바구니로 이동 |
| ❌ 다 씀 | 다 먹음 | 정리됨. 자동 재주문 **안 함** |
| 🧊 냉동보관중 | 냉동 중 | 천천히 먹으면 됨 |

### 💊 약 재고 추적

- 남은 양/일수 자동 계산
- **7일 전** 보충 알림 (약은 끊기면 안 됨!)
- 상태: ✅ 충분 → 📌 이번 주에 쓰자 → 🔄 보충필요

### 빠른 시작 (2분)

1. 아래 Notion 템플릿 **복제**
2. 영수증/주문 캡처를 아무 AI한테 **보내기**
3. 결과를 재고 테이블에 **붙여넣기**
4. 수식이 알아서 **계산**

> 📎 [템플릿 받기 →](https://www.notion.so/381b6fe634e781faad5feff0f300cbd7)

### 꿀팁

- **재고 보드 뷰** → `신선도`로 그룹핑하면 ⚠️가 맨 위에 옴
- **월별 소비** → 소비기록을 `월 Month`로 그룹핑
- **마트 갈 때** → 폰에서 Notion 열어서 🛒 장바구니 확인
- **긴 스크린샷 안 될 때** → 2-3장 찍어서 AI한테 같이 보내기

---

## 🛠 Two Versions

### 🟢 Template Version (Recommended — Everyone)
- **Zero install** — duplicate the Notion template, done
- **Any AI** — works with ChatGPT, Gemini, Kimi, etc.
- **Auto formulas** — freshness alerts calculate themselves
- **All devices** — anything with Notion app

### 🔵 Developer Version (Advanced)
Python scripts for automation: daily cron checks, push notifications, macOS Reminders integration.

```
src/
├── config.py              # Environment variables
├── notion_client.py       # Notion API client (zero dependencies)
├── setup_template.py      # Template formula setup
├── inventory_check.py     # Expiration + auto-restock
├── medicine_tracker.py    # Dose calculation + alerts
├── receipt_parser.py      # Category classification
├── import_receipt.py      # CLI JSON import
└── notifications.py       # macOS Reminders + Google Calendar
```

```
prompts/
└── receipt_prompt.md      # Universal AI prompt (copy & use)
```

## 📄 License

MIT

## 👤 Author

**Agnies** — [@byeori0821-lab](https://github.com/byeori0821-lab)
