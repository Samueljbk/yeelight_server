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
username = os.environ["GITHUB_USERNAME"]

g = Github(token)

user = g.get_user(username)


def set_light_colour(colour):
    if colour == "red":
        bulb.set_rgb(255, 0, 0)
    elif colour == "green":
        bulb.set_rgb(0, 255, 0)


def get_last_commit_time() -> datetime.datetime:
    all_events = list(user.get_events())
    push_events = [e for e in all_events if e.type == "PushEvent"]
    latest_event = max(push_events, key=lambda e: e.created_at)
    latest_event_time = latest_event.created_at
    utc_dt = pytz.utc.localize(latest_event_time)

    # Step 3: Convert the localized UTC datetime to the desired local timezone
    local_tz = pytz.timezone("Pacific/Auckland")  # Replace with your desired timezone
    local_dt = utc_dt.astimezone(local_tz)

    return local_dt


def has_committed_today():
    last_commit_time = get_last_commit_time()
    current_time = datetime.datetime.now(pytz.timezone("Pacific/Auckland"))

    return last_commit_time.date() == current_time.date()


def update_light_colour():
    if has_committed_today():
        print("Pushed Today")
        set_light_colour("green")
    else:
        print("No Push Today")
        set_light_colour("red")


while True:
    update_light_colour()
    time.sleep(30)

# TODO GOAL: Set light colour to be one colour before commiting and one colour after

# TODO: Write has_commited function, colour functions for before and after, time of day function
# (is_past_seven or is_past_due_date etc)
# Make a while True loop with a sleep that calls the correct colour function
# Look at discord controller for inso on how to do bulb functions
