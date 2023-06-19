import requests
from bs4 import BeautifulSoup
import csv

def extract_books():
    base_url = "https://books.toscrape.com/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    categories = soup.select(".side_categories > ul > li > ul > li > a")
    for category in categories:
        category_url = base_url + category["href"]
        category_name = category.text.strip()
        books = []
        page_url = category_url
        while True:
            response = requests.get(page_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            book_list = soup.select(".product_pod")
            for book in book_list:
                title = book.select("h3 > a")[0]["title"]
                price = book.select(".price_color")[0].text.strip()
                availability = book.select(".availability")[0].text.strip()
                books.append([title, price, availability])
            next_page = soup.select(".next > a")
            if len(next_page) == 0:
                break
            page_url = base_url + next_page[0]["href"]
        with open(f"{category_name}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(books)

extract_books()