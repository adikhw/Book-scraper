from config import PAGE_URL
from fetcher import fetch_url
from parser import parse_listing, has_next_page

def scrape_listings(max_pages):
    all_books = []
    n = 1

    while n <= max_pages:
        url = PAGE_URL.format(n)
        html = fetch_url(url)
        book = parse_listing(html, url)
        all_books.append(book)

        if not has_next_page():
            break

        n = n + 1
    return all_books
