#!/usr/bin/python3
""" This script to export data in the CSV format """

import json
import requests
import sys


if __name__ == "__main__":

    r_user = requests.get('https://jsonplaceholder.typicode.com/users')
    # Obtein the content of json
    dic_users = r_user.json()

    dic_of_id = {}
    for user in dic_users:
        user_name = user.get('username')
        id = user.get('id')
        dic_of_id[id] = user_name

    r_todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos')

    list_of_dic_todos = r_todo.json()

    dic_of_task = {}

    for dic in list_of_dic_todos:
        user_id = dic.get("userId")
        username = dic_of_id[user_id]
        task = dic.get("title")
        completed = dic.get("completed")
        data = {"username": username, "task": task, "completed": completed}

        if dic_of_task.get(user_id):
            dic_of_task.get(user_id).append(data)
        else:
            dic_of_task[user_id] = [data]

    with open('todo_all_employees.json', 'w', newline='') as jsonfile:
        json.dump(dic_of_task, jsonfile)
