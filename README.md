# AI News Scraper

## 專案目標
這個專案用來抓取最新 AI / 資安新聞，整理成 CSV 檔，方便查看與分析。  
適合作為 Python 網頁爬蟲與資料處理的小型專案展示。

## 使用技術
- Python 3
- requests
- BeautifulSoup
- pandas

## 功能
1. 從 [The Hacker News](https://thehackernews.com/) 抓取最新 5 篇新聞
2. 取得新聞標題與連結
3. 將結果存成 CSV (`ai_news_report.csv`)
4. (可擴展) 未來可加入 AI 摘要、自動分類或排程自動抓新聞

## 執行方式
1. 安裝套件：
```bash
pip install -r requirements.txt
