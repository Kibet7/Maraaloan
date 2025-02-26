
# Install dependencies
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput
