#!/usr/bin/python3
"""
list containing the titles of
all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'custom'}
    params = {'limit': 100, 'after': after}

    response = requests.get(base_url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        hot_list.extend(post['data']['title'] for post in posts)

        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    elif response.status_code in (302, 404):
        return None
    return None
