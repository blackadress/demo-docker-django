#!bin/bash
docker-compose build
docker-compose run django_app py.test