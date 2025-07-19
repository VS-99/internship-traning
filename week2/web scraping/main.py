import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes_to_csv():
    base_url = "http://quotes.toscrape.com/page/"
    all_quotes = []

    for page in range(1, 6):  # First 5 pages
        url = base_url + str(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]
            all_quotes.append([text, author, ", ".join(tags)])

    # Save to CSV
    with open("D:/algoanalytics/internship-training/week2/web scraping/quotes.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Quote", "Author", "Tags"])
        writer.writerows(all_quotes)

    print("✅ Quotes saved to quotes.csv")

scrape_quotes_to_csv()





def get_inshorts_headlines():
    url = "https://inshorts.com/en/read"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    news_cards = soup.find_all("div", class_="news-card")
    
    print("📰 Top News Headlines:\n")
    for i, card in enumerate(news_cards[:10]):  # Top 10
        headline = card.find("span", itemprop="headline").text
        print(f"{i+1}. {headline}")

get_inshorts_headlines()
