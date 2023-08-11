#!/usr/bin/python3

import requests
from sys import argv
subreddit = argv[1]
headers = {'User-Agent':'desmends'}
res = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers);
res = res.json()
print(res['data']['subscribers'])
