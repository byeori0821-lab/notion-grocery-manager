"""Lightweight Notion API client using only stdlib (no dependencies)."""

import json
import urllib.request
from config import NOTION_TOKEN, NOTION_VERSION, NOTION_BASE_URL


def api(method, path, body=None):
    url = f"{NOTION_BASE_URL}{path}" if path.startswith("/") else path
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def query_database(db_id, filter_obj=None, page_size=100):
    body = {"page_size": page_size}
    if filter_obj:
        body["filter"] = filter_obj
    return api("POST", f"/databases/{db_id}/query", body)


def create_page(db_id, properties, icon_emoji=None):
    body = {"parent": {"database_id": db_id}, "properties": properties}
    if icon_emoji:
        body["icon"] = {"type": "emoji", "emoji": icon_emoji}
    return api("POST", "/pages", body)


def update_page(page_id, properties):
    return api("PATCH", f"/pages/{page_id}", {"properties": properties})


def get_block_children(block_id):
    return api("GET", f"/blocks/{block_id}/children?page_size=100")


def append_blocks(block_id, children):
    return api("PATCH", f"/blocks/{block_id}/children", {"children": children})


def update_block(block_id, content):
    return api("PATCH", f"/blocks/{block_id}", content)


def delete_block(block_id):
    return api("DELETE", f"/blocks/{block_id}")


def rich_text(text, bold=False, color="default"):
    return {
        "type": "text",
        "text": {"content": text},
        "annotations": {"bold": bold, "color": color},
    }
