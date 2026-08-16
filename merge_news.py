#!/usr/bin/env python3
"""Safely merge a generated news batch into data.json.

The input may be either a JSON array or an object containing a ``news`` array.
Existing items are preserved, titles are de-duplicated, IDs are reassigned, and
the output is replaced atomically only after the full payload validates.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


CATEGORY_LABELS = {
    "tech": "技术前沿",
    "policy": "政策标准",
    "product": "产品方案",
    "scenario": "场景落地",
    "security": "数据安全",
}
REQUIRED_TEXT_FIELDS = ("title", "summary", "source", "url")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--data", required=True, type=Path)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--delete-input", action="store_true")
    return parser.parse_args()


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_item(raw: object, index: int, report_date: str) -> dict:
    if not isinstance(raw, dict):
        raise ValueError(f"news[{index}] must be a JSON object")

    item = dict(raw)
    for field in REQUIRED_TEXT_FIELDS:
        value = item.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"news[{index}].{field} must be non-empty text")
        item[field] = value.strip()

    parsed_url = urlparse(item["url"])
    if parsed_url.scheme not in {"http", "https"} or not parsed_url.netloc:
        raise ValueError(f"news[{index}].url must be a real http(s) URL")

    category = item.get("category")
    if category not in CATEGORY_LABELS:
        choices = ", ".join(CATEGORY_LABELS)
        raise ValueError(f"news[{index}].category must be one of: {choices}")

    item["categoryLabel"] = CATEGORY_LABELS[category]
    item["date"] = str(item.get("date") or report_date)
    item["published"] = str(item.get("published") or item["date"])

    keywords = item.get("keywords")
    if not isinstance(keywords, list) or not 3 <= len(keywords) <= 5:
        raise ValueError(f"news[{index}].keywords must contain 3 to 5 values")
    if not all(isinstance(keyword, str) and keyword.strip() for keyword in keywords):
        raise ValueError(f"news[{index}].keywords must contain non-empty text")
    item["keywords"] = [keyword.strip() for keyword in keywords]
    item.pop("id", None)
    return item


def main() -> None:
    args = parse_args()
    existing = load_json(args.data)
    incoming = load_json(args.input)

    if not isinstance(existing, dict) or not isinstance(existing.get("news"), list):
        raise ValueError("data file must be an object containing a news array")
    if isinstance(incoming, dict):
        incoming = incoming.get("news")
    if not isinstance(incoming, list):
        raise ValueError("input must be a JSON array or an object containing a news array")

    validated = [validate_item(item, index, args.date) for index, item in enumerate(incoming)]
    known_titles = {
        item.get("title", "").strip().casefold()
        for item in existing["news"]
        if isinstance(item, dict)
    }

    added = []
    skipped = 0
    for item in validated:
        key = item["title"].casefold()
        if key in known_titles:
            skipped += 1
            continue
        known_titles.add(key)
        existing["news"].append(item)
        added.append(item)

    for item_id, item in enumerate(existing["news"], start=1):
        if not isinstance(item, dict):
            raise ValueError("all existing news entries must be JSON objects")
        item["id"] = item_id
    existing["lastUpdated"] = args.date

    args.data.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{args.data.name}.", suffix=".tmp", dir=args.data.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(existing, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, args.data)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise

    if args.delete_input:
        args.input.unlink(missing_ok=True)

    result = {
        "date": args.date,
        "received": len(validated),
        "added": len(added),
        "duplicatesSkipped": skipped,
        "total": len(existing["news"]),
        "dataFile": str(args.data),
    }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
