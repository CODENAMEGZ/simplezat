#!/bin/sh

cd simplezat
pipenv run python manage.py migrate --setting=simplezat.settings.dev
pipenv run python manage.py collectstatic --noinput --setting=simplezat.settings.dev
pipenv run uwsgi --ini uwsgi.dev.ini