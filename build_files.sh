#!/bin/bash

# Upgrade pip and install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Apply migrations
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput
