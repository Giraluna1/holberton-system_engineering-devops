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

    for dic in list_of_dic_todos:
        list_key = []
        list_values = []

        list_key.append("task")
        list_values.append(dic.get("title"))
        list_key.append("completed")
        list_values.append(dic.get("completed"))
        list_key.append("username")
        list_values.append(user_name)

        dic_of_task[employed_ID].append(dict(zip(list_key, list_values)))

    with open('{}.json'.format(employed_ID), 'w', newline='') as jsonfile:
        json.dump(dic_of_task, jsonfile)
