import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/page-1.html"
books = []

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        availability = book.find("p", class_="instock availability").text.strip()
        books.append([title, price, availability])

    # Find next page link
    next_button = soup.find("li", class_="next")
    url = "http://books.toscrape.com/catalogue/" + next_button.a["href"] if next_button else None

# Write to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Availability"])
    writer.writerows(books)

print("✅ Data saved to books.csv")
