#!/usr/bin/python3

from datetime import datetime, timedelta
import time
from redis import Redis
from rq import Queue
import sys
sys.path.append('./taskfile/')
from taskfile import tasks

queue = Queue(connection=Redis())

def queue_tasks():
    # queue.enqueue(tasks.print_task, 50)
    # queue.enqueue_in(timedelta(seconds=10), tasks.print_numbers, 5)
    queue.enqueue(tasks.print_response)

def main():
    queue_tasks()

if __name__ == "__main__":
    main()
