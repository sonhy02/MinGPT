# scrap_news.py
import korean_news_scraper

keywords = ["Iran"]
korean_news_scraper.save_article_links(keywords, "data", lang="en-EN")
korean_news_scraper.extract_article_content("data")
