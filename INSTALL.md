# DCPG: APIs-web-server Installation Guide

## Requirement:

    Python 3.7+

## Step 1 - Install MongoDB and create an instance:

    Follow the official guide from MongoDB to install and run the program:
    https://docs.mongodb.com/manual/installation/

## Step 2 - Download/ clone the source code:

    Open terminal and run the command:

    git clone https://github.com/intek-training-jsc/digital-camera-photo-geolocation-restful-api-server-khang_tran_khang_vu.git
    << ENTER YOUR ACCOUNT FROM INTEK INSTITUTE >>

    cd << PATH_TO_DIR >>/digital-camera-photo-geolocation-restful-api-server-khang_tran_khang_vu

    git checkout develop

## Step 3 - Install requirement libs and modules from file requirement.txt

    On terminal, run the command:

    pip3 install -r requirement.txt

## Step 3 - Run server

    On terminal, run the command:

    python3 manage.py makemigrations photo_geotag

    python3 manage.py migrate

    python3 manage.py runserver

    The server is ready and listening at localhost:8000
