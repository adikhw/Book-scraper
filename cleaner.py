import re

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def clean_price(text):
    result = re.sub(r'[^0-9.]', '', text)
    if not result:
        return None
    return float(result)

def clean_rating(words):
    return RATING_MAP.get(words)

def clean_stock(text):
    number = re.search(r'\d+', text)
    
    if number:
        return int(number.group())
    return 0

def clean_book(book):
    return {
        "title": book["title"],
        "price": clean_price(book["price_raw"]),
        "rating": clean_rating(book["rating_raw"]),
        "category": book["category"],
        "in_stock":"In stock" in book["stock_text"],
        "stock_count": clean_stock(book["stock_text"]),
        "url": book["url"]
    }