#!/bin/sh
set -e

python manage.py makemigrations app
python manage.py migrate

exec "$@"
