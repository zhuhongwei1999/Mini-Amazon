#!/bin/bash
while [ "1"=="1" ]
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py populate_products
do  
    python3 manage.py runserver 0.0.0.0:8000
    sleep 1
done
