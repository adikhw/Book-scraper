from urllib.parse import urljoin
from bs4 import BeautifulSoup

def parse_listing(html, page_url):
    soup = BeautifulSoup(html, 'html.parser')
    books = []

    for book in soup.find_all("article", class_="product_pod"):
        link = book.find("h3").find("a")
        title = link["title"]
        href = link["href"]
        url = urljoin(page_url, href)

        price = book.find("p", class_="price_color").get_text(strip=True)
        rating = book.find("p", class_="star-rating")["class"][1]
        stock = book.find("p", class_="instock").get_text(strip=True)

        books.append({
            
            "title": title,
            "price_raw": price,
            "rating_raw": rating,
            "stock_raw": stock,
            "url": url
        })
    return books

def has_next_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    next_page = soup.find("li", class_="next")

    return next_page is not None