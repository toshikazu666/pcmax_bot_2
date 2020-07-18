from argparse import ArgumentParser
from configparser import ConfigParser

from bot import Bot
from interface.news import News
from interface.pcmax import Pcmax

PURE = "1"
ADULT = "2"

def main():
    parser = ArgumentParser()
    parser.add_argument("-u", "--user", required=True, help="pcmax login user")
    parser.add_argument("-p", "--password", required=True, help="pcmax login password")
    args = parser.parse_args()

    config = ConfigParser()
    config.read("settings.ini")

    pcmax = Pcmax(
        config.get("pcmax", "login_url"),
        config.get("pcmax", "tweet_post_url").replace("ROOM", ADULT),
        args.user,
        args.password
    )
    news = News(config.get("news", "url"))

    bot = Bot(pcmax, news)
    bot.run()

if __name__ == "__main__":
    main()