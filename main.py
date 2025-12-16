import requests
from bs4 import BeautifulSoup
import json

URL = "https://kun.uz/"
response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
items = soup.select("li.main-news__right-item")[:5]

news = []
for item in items:
    link_tag = item.select_one("a.main-news__right-link")
    title_tag = item.select_one("p.main-news__right-text")
    meta_tag = item.select_one("div.gray-text p")

    news.append({
        "title": title_tag.get_text(strip=True),
        "link": URL + link_tag["href"],
        "category_time": meta_tag.get_text(strip=True)
    })
with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=4)

print("Oxirgi 5 ta yangilik JSON faylga saqlandi")
