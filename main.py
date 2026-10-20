import argparse
import logging
import sys

import config
from config import PAGE_URL
from fetcher import fetch_with_cache
from parser import parse_listing, has_next_page, parse_detail
from cleaner import clean_book
from storage import save_csv, save_json

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
            html = fetch_with_cache(book["url"])
            detail = parse_detail(html)
            book.update(detail)
        except Exception as e:
            logger.warning("Failed to fetch detail for %s: %s", book["url"], e)
            book["category"] = None
            book["stock_text"] = None
    return books


def main():
    arg_parser = argparse.ArgumentParser(description="Book scraper")
    arg_parser.add_argument("--pages", type=int, default=3)
    arg_parser.add_argument("--delay", type=float, default=config.DELAY)
    arg_parser.add_argument("--out", default=config.OUT_DIR)
    args = arg_parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    config.DELAY = args.delay

    logging.info("Start scraping %d pages", args.pages)
    raw = scrape_listings(args.pages)
    complete = enrich(raw)

    clean = []
    fail = 0

    for book in complete:
        try:
            result = clean_book(book)
            clean.append(result)
        except Exception as e:
            fail = fail + 1
            logging.warning("Failed to clean book %s: %s", book["url"], e)

    save_csv(clean, args.out + "/books.csv")
    save_json(clean, args.out + "/books.json")

    print(f"Clean books: {len(clean)}")
    print(f"Failed: {fail}")
    print(f"Saved to: {args.out}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by user")
        sys.exit(130)
    except Exception:
        logging.exception("Unexpected error")
        sys.exit(1)