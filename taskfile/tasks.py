from datetime import datetime, timedelta
import time
import json
import requests

def print_task(seconds):
    print("Starting task")
    for num in range(seconds):
        print(num, ". Hello World!")
        time.sleep(1)
    print("Task completed")

def print_numbers(seconds):
    print("Starting num task")
    for num in range(seconds):
        print(num)
        time.sleep(1)
    print("Task to print_numbers completed")

def print_response():
    f = open('response.json')
    data = json.load(f)
    for item in data:
        print(item)
        x = requests.post(f'http://localhost:9200/optimize/_doc/{item["id"]}', json = item)
        time.sleep(1)
        print(x)
        print('\n')
    f.close()
