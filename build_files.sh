#!/bin/bash

# Install dependencies inside the Vercel environment
pip install -r requirements.txt

# Apply migrations
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput
