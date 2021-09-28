#!/bin/bash

if [ "$DB" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py flush --no-input
# TODO: after make account model, uncomment
# python manage.py makemigrations
# python manage.py migrate
python manage.py collectstatic --no-input

# hot reload
uwsgi --ini /code/uwsgi.ini

exec "$@"