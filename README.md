# Event Driven Microservice Application

This demo application showcases an event driven system built using a microservices architecture. It features two backend services: one for admin management, developed with the Django framework, and another for user interactions, built with Flask. The frontend is developed using React with TypeScript. Each backend service is connected to its own MySQL database, and RabbitMQ is used to orchestrate events and enable communication between services. The entire application is deployed in Docker containers, ensuring easy setup and consistent environments across different systems.

### Important Commands
```bash
# create python environment
$ python3 -m venv venv

# activate python environemnt
$ source venv/bin/activate

# install django
$ pip install django

# install djangorestframework
$ pip install djangorestframework

# create djando app
$ django-admin startproject admin

# runn the djando app
$ python3 manage.py runserver

# create and start docker cotainers
$ doocker compose up
# stop and remove docker cotainers
$ doocker compose down

# connect to running intance of docker containers
$ docker compose exec backend sh

# connect to mysql databse run inside the docker
$ sudo mysql -h 127.0.0.1 -P 33066 -u root -p --ssl-mode=DISABLED

# create admin database
$ python manage.py startapp products
$ python manage.py makemigrations
$ python manage.py migrate

# change owner of files if required
$ sudo chown -R <user>:<user> /path/to/products

# create main database
$ python manager.py db init
$ python manager.py db migrate
$ python manager.py db upgrade

# allow rabbitmq admin and main network
$ docker network connect admin_default rabbitmq
$ docker network connect main_default rabbitmq
$ docker network inspect admin_default

$ docker compose up -d db

# install forntend dependencies
$ npm install
# run react frontend
$ npm start
```

### Aplication Images

#### Application Testing



#### API Endpoint Testing


