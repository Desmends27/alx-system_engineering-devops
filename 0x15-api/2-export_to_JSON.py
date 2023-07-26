#!/usr/bin/python3
""" Gather data from API and export to json format"""

from requests import get
from sys import argv
import json

if __name__ == '__main__':
    user_id = argv[1]
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    url2 = '{}/todos'.format(url1)
    users = get(url1).json()
    todo_list = get(url2).json()
    todo_dict = []
    for action in todo_list:
        task_dict = {
                "task": action["title"],
                "completed": action["completed"],
                "username": users["name"]
                }
        todo_dict.append(task_dict)
    final_dict = {user_id: todo_dict}
    with open(f"{user_id}.json", 'w') as f:
        json.dump(final_dict, f)
