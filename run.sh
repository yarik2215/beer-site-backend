#!/bin/bash

# while !</dev/tcp/${POSTGRES_HOST}/${POSTGRES_PORT};
# do
#     echo waiting for Postgres to start...;
#     sleep 3;
# done;

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
gunicorn beer_site.wsgi:application -b 0.0.0.0:8000 -w 1