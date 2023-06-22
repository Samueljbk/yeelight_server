import os
import datetime
import time
import pytz
import requests
from pprint import pprint
from yeelight import Bulb
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

yeelight_ip = os.environ["BULB_IP"]
bulb = Bulb(yeelight_ip)
username = os.environ["GITHUB_USERNAME"]


def set_light_colour(colour):
    if colour == "red":
        bulb.set_rgb(255, 154, 138)
    elif colour == "green":
        bulb.set_rgb(119, 221, 119)


def get_todays_contributions() -> int:
    url = f"https://github.com/users/{username}/contributions"
    response = requests.get(url)
    content = response.content.decode("utf-8")
    pprint(content)

    soup = BeautifulSoup(content, "html.parser")
    current_time = datetime.datetime.now(pytz.timezone("Pacific/Auckland"))
    todays_date = current_time.strftime("%Y-%m-%d")

    rect_tags = soup.find_all("rect", {"data-date": todays_date})
    if rect_tags:
        return int(rect_tags[0]["data-count"])
    return 0


def has_committed_today() -> bool:
    todays_contributions = get_todays_contributions()
    return todays_contributions > 0


def update_light_colour():
    if has_committed_today():
        print("Pushed Today")
        set_light_colour("green")
    else:
        print("No Push Today")
        set_light_colour("red")


while True:
    try:
        update_light_colour()
    except Exception as e:
        print(e)
    time.sleep(30)
