#!/usr/bin/python3
""" Use a recursive function to query titles of hot posts"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'linux:desmends:v1.2.0\
                (by /u/HealthyCaterpillar48'}
    params = {
        'after': after
    }
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                          headers=headers, params=params)
    if r.status_code == 200:
        json = r.json()
        data_dict = json.get('data')
        post_list = data_dict.get('children')
        for post in post_list:
            post_data_dict = post.get('data')
            hot_list.append(post_data_dict.get('title'))
        after = data_dict.get('after')
        if data_dict.get('after') is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
