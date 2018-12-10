#!/bin/sh

cd simplezat
pipenv run python manage.py migrate --setting=simplezat.settings.dev
pipenv run  python manage.py collectstatic --noinput --setting=simplezat.settings.prod
pipenv run uwsgi --ini uwsgi.prod.ini