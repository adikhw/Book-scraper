import logging
from config import PAGE_URL
from fetcher import fetch_url, fetch_with_cache
from parser import parse_listing, has_next_page, parse_detail

logger = logging.getLogger(__name__)

def scrape_listings(max_pages):
    all_books = []
    n = 1

    while n <= max_pages:
        url = PAGE_URL.format(n)
        try:
            html = fetch_with_cache(url)
            book = parse_listing(html, url)
            all_books.extend(book)
        except Exception as e:
            logger.warning("Failed to scrape listing page %s: %s", url, e)
            n = n + 1
            continue

        if not has_next_page(html):
            break

        n = n + 1
    return all_books

def enrich(books):
    for book in books:
        try:
            html = fetch_url(book["url"])
            detail = parse_detail(html)
            book.update(detail)
        except Exception as e:
            logger.warning("Failed to fetch detail for %s: %s", book["url"], e)
            book["category"] = None
            book["stock_text"] = None
    return books