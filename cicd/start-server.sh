#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd fairqueue; python manage.py createsuperuser --no-input)
fi
(cd fairqueue; python manage.py makemigrations; python manage.py migrate;
python manage.py loaddata fixtures/alldbdata.json; python manage.py runserver 0.0.0.0:8000)
#(. ./django_queue_venv/bin/activate; cd fairqueue; python manage.py runserver)
