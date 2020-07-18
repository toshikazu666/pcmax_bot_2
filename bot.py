import time
import datetime

import schedule
from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader

class Bot:
    def __init__(self, pcmax, news):
        self.pcmax = pcmax
        self.news = news

        self.weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    
    def tweet(self):
        # つぶやく
        now = datetime.datetime.now()
        now_datetime = "{}月{}日({}) {}時ちょうど".format(now.month, now.day, self.weekdays[now.weekday()], now.hour)
        headline_news = self.news.get_headline_news()
        tweet = self.generate_tweet("template", "tweet.j2", {"time": now_datetime, "news": headline_news})

        self.pcmax.login()
        result = self.pcmax.post_tweet(tweet.encode("shift_jis", "replace"))

        print("[{}] post tweet".format(now.strftime("%Y/%m/%d %H:%M:%S")))
        print("result: {}".format(result))
        print("-----")
        print(tweet)
        print("-----")
        print("status: bot is aliving")

    def generate_tweet(self, directory, template_file, data={}):
        # jinja2テンプレートからつぶやきを生成する
        env = Environment(loader=FileSystemLoader(directory))
        template = env.get_template(template_file)
        return str(template.render(data))

    def try_wrapper(self, func, args=[]):
        # 例外でbotが死なないようにラップする
        try:
            func(*args)
        except Exception as e:
            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            print("[{}] some exception was captured, skip process".format(now))
            print("-----")
            print(e)
            print("-----")
            print("status: bot is aliving")

    def run(self):
        # 毎時間つぶやくスケジュール
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        print("[{}] process begin".format(now))
        print("status: bot is aliving")

        schedule.every().day.at("00:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("01:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("02:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("03:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("04:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("05:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("06:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("07:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("08:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("09:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("10:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("11:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("12:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("13:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("14:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("15:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("16:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("17:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("18:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("19:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("20:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("21:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("22:00").do(self.try_wrapper, self.tweet)
        schedule.every().day.at("23:00").do(self.try_wrapper, self.tweet)

        while True:
            schedule.run_pending()
            time.sleep(10)


