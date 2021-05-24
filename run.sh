#!/bin/bash

echo Applying migrations
python manage.py migrate
echo Starting server
gunicorn beer_site.wsgi:application -b 0.0.0.0:${1:-8000} -w 1