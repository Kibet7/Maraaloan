#!/bin/bash

# Upgrade pip and install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Apply migrations
python3 manage.py migrate --noinput

# Collect static files (fixing missing directory issue)
mkdir -p staticfiles_build  # Ensure the directory exists
python3 manage.py collectstatic --noinput --clear --verbosity 3 -i admin -i rest_framework
mv static staticfiles_build  # Move static files to expected directory
