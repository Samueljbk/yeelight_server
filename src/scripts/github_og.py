from github import Github
import os
import datetime
import time

token = os.environ["PERSONAL_ACCESS_TOKEN"]

g = Github(token)

user = g.get_user("Samueljbk")
all_events = list(user.get_events())
push_events = [e for e in all_events if e.type == "PushEvent"]
latest_event = max(push_events, key=lambda e: e.created_at)
latest_event_time = latest_event.created_at
if latest_event_time.date() == datetime.date.today():
    print("Pushed Today")

print(latest_event)

# TODO GOAL: Set light colour to be one colour before commiting and one colour after

# TODO: Write has_commited function, colour functions for before and after, time of day function (is_past_seven or is_past_due_date etc)
# Make a while True loop with a sleep that calls the correct colour function
# Look at discord controller for inso on how to do bulb functions
