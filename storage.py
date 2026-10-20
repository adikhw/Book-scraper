import json
import csv
from pathlib import Path

COLUMN = ["title", "price", "rating", "category", "in_stock", "stock_count", "url"]

def save_csv(books, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames= COLUMN)
        writer.writeheader()
        writer.writerows(books)

def save_json(books, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2, ensure_ascii=False)
