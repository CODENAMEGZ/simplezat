#!/bin/sh

cd simplezat
pipenv run python manage.py migrate --setting=simplezat.settings.dev
pipenv run  python manage.py runserver 0.0.0.0:8000 --setting=simplezat.settings.dev