#!/usr/bin/python3
""" prints the titles of the first 10 hot posts """
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "custom"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
