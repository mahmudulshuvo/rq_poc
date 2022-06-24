#!/bin/bash

# pip install -r requirements.txt
rq worker --with-scheduler
chmod +x app.py
./app.py