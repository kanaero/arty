#/bin/sh
python manage.py makemigrations operations
python manage.py migrate
python manage.py populate_history --auto

