import os
import datetime
import time
import pytz
from yeelight import Bulb
from github import Github
from dotenv import load_dotenv


load_dotenv()

yeelight_ip = os.environ["BULB_IP"]
bulb = Bulb(yeelight_ip)
token = os.environ["PERSONAL_ACCESS_TOKEN"]

g = Github(token)

user = g.get_user("Samueljbk")


def set_light_colour(colour):
    if colour == "red":
        bulb.set_rgb(255, 0, 0)
    elif colour == "green":
        bulb.set_rgb(0, 255, 0)


def check_commit_status():
    all_events = list(user.get_events())
    push_events = [e for e in all_events if e.type == "PushEvent"]
    latest_event = max(push_events, key=lambda e: e.created_at)
    latest_event_time = latest_event.created_at

    # Convert the latest_event_time to your local timezone
    local_timezone = pytz.timezone("Pacific/Auckland")
    local_latest_event_time = latest_event_time.astimezone(local_timezone)

    if local_latest_event_time.date() == datetime.date.today():
        print("Pushed Today")
        set_light_colour("green")
    else:
        print("No Push Today")
        set_light_colour("red")


check_commit_status()

while True:
    current_time = datetime.datetime.now()
    if current_time.hour == 0 and current_time.minute == 0:
        set_light_colour("red")
        time.sleep(60)
    else:
        check_commit_status()
        time.sleep(30)

# TODO GOAL: Set light colour to be one colour before commiting and one colour after

# TODO: Write has_commited function, colour functions for before and after, time of day function
# (is_past_seven or is_past_due_date etc)
# Make a while True loop with a sleep that calls the correct colour function
# Look at discord controller for inso on how to do bulb functions
