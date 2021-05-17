#!/usr/bin/python3
""" This module print the first 10 hot postts listed subreddit """

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribes """

    if subreddit:
        user_agent = {'user-agent': 'my-app/0.0.1'}
        r_subs = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(
                subreddit), headers=user_agent)
        json_subreddit = r_subs.json()
        return json_subreddit.get('data').get("subscribers")
    else:
        return 0
