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

def parse_detail(html):
    soup = BeautifulSoup(html, 'html.parser')
    category = None
    stock_text = None

    ul_breadcrumb = soup.find("ul", class_="breadcrumb")
    if ul_breadcrumb:
        all_li = ul_breadcrumb.find_all("li")
        target_li = all_li[-2]
        tag_a = target_li.find("a")

        if tag_a:
            category =tag_a.get_text().strip()

    p_availability = soup.find("p", class_="availability")
    if p_availability:
        stock_text = p_availability.get_text(strip=True)

    return {"category": category, "stock_text": stock_text}
    