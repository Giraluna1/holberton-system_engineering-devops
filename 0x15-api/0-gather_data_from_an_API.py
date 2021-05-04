#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    employed_ID = sys.argv[1]
    r_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            employed_ID))

    query = {"userId": employed_ID}
    r_todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos', params=query)

    # Obtein the content of json
    dic_users = r_user.json()
    list_of_dic_todos = r_todo.json()

    # Obtain only the name
    name = dic_users.get('name')
    list_task = []
    total_task = 0
    done = 0
    # Obtain task
    for dic in list_of_dic_todos:
        total_task += 1
        completed = dic.get('completed')
        if completed == True:
            done += 1
            title = dic.get('title')
            list_task.append(title)
    print('Employee {} is done with tasks ({}/{}):'.format(name, done, total_task))
    for element in list_task:
        print('\t {}'.format(element))
