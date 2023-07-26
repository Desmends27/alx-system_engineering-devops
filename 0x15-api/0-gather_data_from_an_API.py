#!/usr/bin/python3
""" Gather data from an API """

from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    url2 = '{}/todos'.format(url1)
    users = get(url1).json()
    todo_list = get(url2).json()
    completed = 0
    total = 0
    for entry in todo_list:
        if entry['completed'] is True:
            completed += 1
        total += 1
    print("Employee {} is done with tasks({}/{}):".format(users['name'],
                                                          completed, total))
    for entry in todo_list:
        print(' \t{}'.format(entry['title']))
