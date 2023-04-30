#!/bin/bash
while [ "1"=="1" ]
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py populate_products
do
    python3 /code/backend/amazon_server.py
    sleep 1
done
