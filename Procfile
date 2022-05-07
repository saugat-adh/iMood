web: gunicorn iMood.wsgi --log-file - --log-level debug

heroku ps:scale web=1

release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input




