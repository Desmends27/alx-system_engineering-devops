#!/usr/bin/python3
""" Print the top 10 posts in a subreddit """

import requests


def top_ten(subreddit):
    """ Print the top 10 posts """
    headers = {'User-Agent': 'linux:desmends:v1.2.0 \
                  (by /u/HealthyCaterpillar48'}
    params = {
            'limit': 10
            }
    result = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                          headers=headers, params=params)
    if (result.status_code == 404):
        print('None')
        return
    result = result.json()
    top = result.get('data').get('children')
    for post in top:
        print(post['data']['title'])
