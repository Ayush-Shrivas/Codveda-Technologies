import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://quotes.toscrape.com/"

# Get the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data - in this case, quotes and authors
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Prepare CSV file
csv_filename = "scraped_data.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])  # Header

    for quote, author in zip(quotes, authors):
        writer.writerow([quote.get_text(strip=True), author.get_text(strip=True)])

print(f"Data scraped and saved to {csv_filename}")
