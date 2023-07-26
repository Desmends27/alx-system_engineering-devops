#!/usr/bin/python3
""" Gather data from an API  and use it to generate a list of employees"""

from requests import get
from sys import argv
import json

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    url1 = f'{url}users'
    users = get(url1).json()
    final_dict = {}
    for user in users:
        url2 = '{}/{}/todos'.format(url1, user['id'],)
        todos = get(url2).json()
        todos_list = []
        for action in todos:
            task_dict = {
                "username": user["name"],
                "task": action["title"],
                "completed": action["completed"],
                }
            todos_list.append(task_dict)
        final_dict[user['id']] = todos_list
    with open('todo_all_employees.json', 'w') as f:
        json.dump(final_dict, f)
