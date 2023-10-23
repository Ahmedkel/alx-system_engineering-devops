#!/usr/bin/python3
""" Export to CSV format """
import csv
import requests
import sys


def export_to_csv(employee_id):
    # Fetch employee data
    employee_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch todo data
    todo_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Prepare data for CSV
    rows = [[employee_id, employee_name, task['completed'],
             task['title']] for task in todo_data]

    # Write to CSV
    with open(f'{employee_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)


if __name__ == "__main__":
    export_to_csv(int(sys.argv[1]))
