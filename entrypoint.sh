#!/bin/bash
# Entrypoint script for Railway
set -e

echo "Running migrations..."
python manage.py migrate --noinput || echo "Migration warning"

echo "Starting gunicorn on port $PORT..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --timeout 120
