#!/usr/bin/python3
""" Python script to export data in the JSON format """
import requests
import json


def export_all_tasks():
    # Fetch all employee data
    employee_response = requests.get(
            'https://jsonplaceholder.typicode.com/users')
    employee_data = employee_response.json()

    # Prepare tasks for all employees
    all_tasks = {}
    for employee in employee_data:
        employee_id = str(employee['id'])
        employee_name = employee['username']

        # Fetch todo data for each employee
        todo_response = requests.get(
                f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
                )
        todo_url = base_url + todo_endpoint
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Prepare tasks for the current employee
        tasks = [{"username": employee_name,
                  "task": task["title"],
                  "completed": task["completed"]}
                 for task in todo_data]

        # Add tasks to the dictionary
        all_tasks[employee_id] = tasks

    # Export all tasks to a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f)


if __name__ == "__main__":
    export_all_tasks()
