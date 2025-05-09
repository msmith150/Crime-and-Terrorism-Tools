import requests
from bs4 import BeautifulSoup
import re

# List of news websites to scrape
news_websites = [
    "https://www.bbc.com/news",
    "https://www.reuters.com/news",
    "https://www.theguardian.com/world"
]

# Function to fetch and parse articles
def fetch_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all article links - Modify this depending on the website structure
    articles = soup.find_all('a', href=True)
    
    relevant_articles = []
    
    for article in articles:
        link = article['href']
        if re.search(r'\bterrorism\b', article.text, re.IGNORECASE):  # Check if "terrorism" is mentioned
            relevant_articles.append({
                'title': article.text.strip(),
                'url': link
            })
    
    return relevant_articles

# Scrape articles from all websites
all_articles = []
for website in news_websites:
    articles = fetch_articles(website)
    all_articles.extend(articles)

# Print the collected articles
for article in all_articles:
    print(f"Title: {article['title']}\nURL: {article['url']}\n")

