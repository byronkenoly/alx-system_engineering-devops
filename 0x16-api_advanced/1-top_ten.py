#!/usr/bin/python3
"""
queries reddit API and prints titles of 1st 10 hot posts
"""

import requests


def top_ten(subreddit):
    uri = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "ByronAPI"}

    res = requests.get(uri, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        posts = res.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
