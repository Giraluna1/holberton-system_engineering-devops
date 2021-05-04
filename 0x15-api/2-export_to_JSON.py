#!/usr/bin/python3
""" This script to export data in the CSV format """

import json
import requests
import sys


if __name__ == "__main__":

    employed_ID = int(sys.argv[1])
    r_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            employed_ID))

    query = {"userId": employed_ID}
    r_todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos', params=query)

    # Obtein the content of json
    dic_users = r_user.json()
    list_of_dic_todos = r_todo.json()

    # Obtain only the username
    user_name = dic_users.get('username')
    dic_of_task = {employed_ID: []}
    data = {}
    for dic in list_of_dic_todos:
        data['task'] = dic.get('title')
        data['completed'] = dic.get('completed')
        data['username'] = user_name
        dic_of_task[employed_ID].append(data)

    with open('{}.json'.format(employed_ID), 'w', newline='') as jsonfile:
        json.dump(dic_of_task, jsonfile)
