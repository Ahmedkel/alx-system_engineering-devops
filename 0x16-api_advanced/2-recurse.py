#!/usr/bin/python3
"""
list containing the titles of
all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {"User-Agent": "custom"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()["data"]
    hot_list.extend([post["data"]["title"] for post in data["children"]])

    after = data["after"]

    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
