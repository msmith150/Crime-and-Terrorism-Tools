import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import time

news_websites = [
    "https://www.bbc.com/news",
    "https://www.reuters.com/news",
    "https://www.theguardian.com/world"
]

KEYWORD = "terrorism"

def fetch_articles(url, keyword):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    relevant_articles = []
    seen = set()

    for link in links:
        text = link.get_text(strip=True)
        href = link['href']

        if keyword.lower() in text.lower():
            full_url = urljoin(url, href)
            if full_url not in seen:
                seen.add(full_url)
                relevant_articles.append({
                    'title': text,
                    'url': full_url,
                    'source': url
                })

    return relevant_articles


# Print the collected articles
for article in all_articles:
    print(f"Title: {article['title']}\nURL: {article['url']}\n")

import csv

if __name__ == "__main__":
    results = scrape_news(news_websites, KEYWORD)

    # Save to CSV
    with open('terrorism_articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'url', 'source']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for article in results:
            writer.writerow(article)

    print(f"Saved {len(results)} articles to 'terrorism_articles.csv'")

