#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn beer_site.wsgi:application -b 0.0.0.0:${1:-8000} -w 1