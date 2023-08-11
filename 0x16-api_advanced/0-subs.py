#!/usr/bin/python3

""" Get the number of subscribers for a subreddit """

import requests


def number_of_subscribers(subreddit):
    """ get data about a subreddit """
    headers = {'User-Agent': 'linux:desmends:v1.2.0 \
                  (by /u/HealthyCaterpillar48'}
    result = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                          headers=headers)
    result = result.json().get('data').get('subscribers')
    return result
