#!/usr/bin/python3
""" This module print the first 10 hot postts listed subreddit """

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribes """

    if subreddit:
        user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
        r_subs = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit), headers=user_agent)
        json_subreddit = r_subs.json()
        return json_subreddit.get('data').get("subscribers")
    else:
        return 0
