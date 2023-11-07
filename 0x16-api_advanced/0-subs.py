#!/usr/bin/python3
""" Fetch the the number of subscribers Reddit API. """
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
