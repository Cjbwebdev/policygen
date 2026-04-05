#!/bin/bash
cd "$(dirname "$0")"
python manage.py makemigrations && python manage.py migrate
python manage.py runserver
