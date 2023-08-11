#!/usr/bin/python3
""" Use a recursive function to query titles of hot posts"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'linux:desmends:v1.2.0\
                (by /u/HealthyCaterpillar48'}
    params = {
        'after': after
    }
    result = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                          headers=headers, params=params)

    if result.status_code == 404:
        return None

    result = result.json()
    posts = result.get('data').get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    after = result.get('data').get('after')
    if result.get('data').get('after') is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
