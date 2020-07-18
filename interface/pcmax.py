import requests
from bs4 import BeautifulSoup

class Pcmax:
    def __init__(self, login_url, tweet_post_url, user, password):
        # PCMAXのインターフェース
        self.login_url = login_url
        self.user = user
        self.password = password
        self.tweet_post_url = tweet_post_url

    def login(self):
        # ログインしてセッションを作る
        self.session = requests.session()
        login_info = {
            "login_id": self.user,
            "login_pw": self.password,
            "save_on": "false",
            "login": "1"
        }
        res = self.session.post(self.login_url, data=login_info)
        res.raise_for_status()

    def get_tweet_input(self):
        # つぶやきのPOSTに必要なinputを取得する
        res = self.session.get(self.tweet_post_url)
        soup = BeautifulSoup(res.text, "lxml")
        write_form = soup.find(id="write_form")
        inputs = write_form.find_all("input")
        return {i["name"]: i["value"] for i in inputs}

    def post_tweet(self, tweet):
        # つぶやきPOSTする
        input_values = self.get_tweet_input()
        input_values["tweet_body"] = tweet
        res = self.session.post(self.tweet_post_url, data=input_values)
        res.raise_for_status()
        return res
