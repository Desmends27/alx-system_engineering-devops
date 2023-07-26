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
    # Assuming user_id is defined or obtained from somewhere
    with open(f'{user_id}.csv', 'w') as csv_file:
        for action in todo_list:
            line = (
                    f'"{user_id}",'
                    f'"{users["name"]}",'
                    f'"{action["completed"]}",'
                    f'"{action["title"]}"\n'
                    )
            csv_file.write(line)
