#!/usr/bin/python3
""" This script to export data in the CSV format """

import csv
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

    # Obtain only the name
    user_name = dic_users.get('username')

    with open('{}.csv'.format(employed_ID), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for dic in list_of_dic_todos:
            row = [employed_ID, user_name, dic.get(
                'completed'), dic.get('title')]
            writer.writerow(row)
