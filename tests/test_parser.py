from pathlib import Path

from config import PAGE_URL
from parser import parse_listing, parse_detail

FIXTURES = Path(__file__).parent / "fixtures"


def read_fixture(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


def test_parse_listing_returns_20_books():
    html = read_fixture("listing.html")
    books = parse_listing(html, PAGE_URL.format(1))
    assert len(books) == 20


def test_parse_listing_book_has_all_keys():
    html = read_fixture("listing.html")
    books = parse_listing(html, PAGE_URL.format(1))
    expected_keys = {"title", "price_raw", "rating_raw", "stock_raw", "url"}
    for book in books:
        assert expected_keys <= set(book.keys())
        assert book["url"].startswith("http")


def test_parse_detail():
    html = read_fixture("detail.html")
    detail = parse_detail(html)
    assert detail["category"] is not None
    assert "In stock" in detail["stock_text"]