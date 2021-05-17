#!/usr/bin/python3
""" This module print the first 10 hot postts listed subreddit """

import requests

def number_of_subscribers(subreddit):
    """ Returns the number of subscribes """

    if subreddit:
        r_subs = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit))
        json_subreddit = r_subs.json()
        return json_subreddit.get('data').get("subscribers")
    else:
        return 0
