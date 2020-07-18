import requests
from bs4 import BeautifulSoup

class News:
    def __init__(self, url):
        # Google Newsのインターフェース
        self.url = url
        self.cache = []
        self.max_cache_size = 24

    def get_headline_news(self):
        # ヘッドラインニュースを取得する
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, "lxml")
        news = [item.find("title").get_text() for item in soup.find_all("item")]
        for n in news:
            if n not in self.cache:
                # 一度返したニュースはキャッシュする
                if len(self.cache) >= self.max_cache_size:
                    self.cache = []
                self.cache.append(n)
                return n 
        return news[0]
