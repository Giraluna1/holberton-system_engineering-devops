#!/usr/bin/python3
"""  Rcurse it """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """ list containing the titles of all hot articles for a given subreddit """

    user_agent = {'user-agent': 'my-app/0.0.1'}
    filter = {'after': after}
    r_subs = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(
            subreddit), headers=user_agent, params=filter)
    if after is None:
        return hot_list
    if r_subs.status_code != 200:
        return None
    else:
        json_subreddit = r_subs.json()
        after = json_subreddit.get('data').get('after')
        children = json_subreddit.get('data').get('children')
        for dictionaries in children:
            hot_list.append(dictionaries.get("data").get("title"))
        return recurse(subreddit, hot_list, after)
