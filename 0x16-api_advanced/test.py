#!/usr/bin/python3

import requests
import json
from sys import argv
subreddit = argv[1]
headers = {'User-Agent':'desmends'}
params = {
        'limit':10
        }
res = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers=headers, params=params, allow_redirects=False);
res = res.json()
print(res)
#for r in res["data"]["children"]:
 #   print(r['data']['title'])

