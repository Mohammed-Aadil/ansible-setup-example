# Ansible playbook setup with django + Angular + React

This project contains ansible playbook setup for common configuration of django, angular and react.
It install all dependencies related to project from requirement.txt and package.json file. 
It contains roles for common, angular and react project.

## Common role
It will complete following steps:
1. Creating project user and group
2. installing python 3.6 
3. Install linux dependencies and env var
4. install git and pull latest code
5. create env file for django proj
6. Install redis server
7. Install rabbitmq server
8. Install postgres and create database user and db
9. Install pip requirements
10. Do migrations on db
11. Create superuser via custom commands (It read user detail from ansible var)
12. Do collect statics file for django
13. Install nginx and create nginx conf for django project
14. Install gunicorn and create gunicorn runner shell file (used by supervisor)
15. Install supervisor, create project conf file and run django, celery and celery-beat

## Angular role
It will complete following steps:
1. Install nodejs 8.x
2. Build the angular app using production build
3. Install nginx and create nginx conf for angular project

## React role
It will complete following steps:
1. Install nodejs 8.x
1. Install yarn
2. Build the react app using production build
3. Install nginx and create nginx conf for angular project

## Other dependencies
1. sshpass
