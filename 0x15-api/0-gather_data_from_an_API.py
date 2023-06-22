#!/usr/bin/python3
"""
py script that returns employee info given the employee ID
"""

import json
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    usr = argv[1]
    res = urlopen("https://jsonplaceholder.typicode.com/users/{}".format(usr))
    json_read = res.read()
    json_decode = json_read.decode()
    json_dict = json.loads(json_decode)

    if json_dict['name'] is not None:
        url = "https://jsonplaceholder.typicode.com/todos?userId="
        tasks_res = urlopen("{}{}".format(url, usr)).read().decode()
        tasks_dict = json.loads(tasks_res)

        count = 0
        for task in tasks_dict:
            if task['completed'] is True:
                count += 1

        name = json_dict['name']
        total = len(tasks_dict)
        print(f"Employee {name} is done with tasks({count}/{total}):")
        for task in tasks_dict:
            if task['completed'] is True:
                print(f"\t {task['title']}")
