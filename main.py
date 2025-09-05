import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_articles():
    url = "https://thehackernews.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    articles = soup.find_all("a", class_="story-link")
    news_list = []
    for a in articles[:5]:
        h2 = a.find("h2")
        if h2:
            title = h2.text.strip()
            link = a["href"]
            news_list.append({"title": title, "link": link, "summary": title})
    return news_list

def main():
    news_list = get_articles()
    df = pd.DataFrame(news_list)
    df.to_csv("ai_news_report.csv", index=False, encoding="utf-8-sig")
    print("已輸出報告:ai_news_report.csv")

if __name__ == "__main__":
    main()
