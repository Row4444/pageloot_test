#!/bin/bash

docker compose up -d --build

echo "Waiting for PostgreSQL to be ready..."
until docker compose exec db pg_isready -U postgres
do
  sleep 2
done


echo "Running migrations"
docker compose exec web python manage.py migrate

echo "Server started"