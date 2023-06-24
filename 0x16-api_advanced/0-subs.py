#!/usr/bin/python3
"""
function that queries reddit api and returns no. of subs
"""

import requests


def number_of_subscribers(subreddit):
    uri = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ByronAPI'}
    res = requests.get(uri, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return res.json().get('data').get('subscribers')

    return 0
