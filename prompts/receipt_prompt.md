# Receipt Parsing Prompt
# 适用于任何 AI：ChatGPT / Claude / Gemini / Kimi / 豆包 / Copilot / 通义 ...
# 把这段话和小票图片/PDF一起发给任意AI即可

---

请解析这张小票/发票，输出以下JSON格式（不要输出其他内容，只输出JSON）：

```json
{
  "store": "店铺名称（如：盒马、小象超市、山姆）",
  "date": "YYYY-MM-DD",
  "items": [
    {
      "name": "商品名称",
      "price": 12.9,
      "qty": "数量（如：1、300g、2盒、500ml×3）"
    }
  ]
}
```

规则：
- price 是单项实付金额（数字，不带¥）
- 如果有折扣/优惠，用折后价
- qty 保留原始规格描述
- 只输出纯JSON，不要解释
