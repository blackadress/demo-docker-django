#!bin/bash
docker-compose build
docker-compose run django_app python manage.py migrate
docker-compose up