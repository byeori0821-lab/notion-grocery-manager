import os

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
INVENTORY_DB = os.environ.get("INVENTORY_DB", "")
SHOPPING_DB = os.environ.get("SHOPPING_DB", "")
PURCHASE_DB = os.environ.get("PURCHASE_DB", "")
GROCERY_PAGE = os.environ.get("GROCERY_PAGE", "")

NOTION_VERSION = "2022-06-28"
NOTION_BASE_URL = "https://api.notion.com/v1"
