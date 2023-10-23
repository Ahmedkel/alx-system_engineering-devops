#!/usr/bin/python3
""" Fetch employee data and covert it to JSON """
import json
import requests
import sys


def get_todo_list_progress(employee_id):
    # Fetch employee data
    employee_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['username']

    # Fetch todo data
    todo_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Prepare tasks in the required format
    tasks = [{"task": task["title"],
              "completed": task["completed"],
              "username": employee_name} for task in todo_data]

    # Export tasks to a JSON file
    with open(f'{employee_id}.json', 'w') as f:
        json.dump({employee_id: tasks}, f)


if __name__ == "__main__":
    get_todo_list_progress(int(sys.argv[1]))
