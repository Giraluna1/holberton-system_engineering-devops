#!/usr/bin/python3
"""  Module TOP TEN """

import requests


def top_ten(subreddit):
    """  the first 10 hot posts listed for a given subreddit. """

    user_agent = {'user-agent': 'my-app/0.0.1'}
    r_subs = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(
            subreddit), headers=user_agent)
    if r_subs.status_code != 200:
        print(None)
    else:
        json_subreddit = r_subs.json()
        children = json_subreddit.get('data').get('children')
        for dictionaries in children[:10]:
            tittle = dictionaries.get("data").get("title")
            print(tittle)
