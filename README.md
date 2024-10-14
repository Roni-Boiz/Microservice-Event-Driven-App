# Microservice Event Driven Application

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
![app-1](https://github.com/user-attachments/assets/211caf3d-c0a5-40f7-a9f1-36889ee00ae8)

![app-2](https://github.com/user-attachments/assets/1ae91988-6410-4c9c-acf2-f39d4aed19e4)

![app-3](https://github.com/user-attachments/assets/b4b0242d-2697-4a90-9472-2e1acdab5654)

![app-4](https://github.com/user-attachments/assets/8ce0af48-f452-4408-8ff6-f5477add0257)

![app-5](https://github.com/user-attachments/assets/5cd3c80b-6741-40d3-8914-e15822d8a731)

#### API Endpoint Testing
![api-1](https://github.com/user-attachments/assets/0536fab0-4c9d-43e5-8cf4-9d89648c24a7)

![api-2](https://github.com/user-attachments/assets/0c4de867-5d89-45f7-bf5a-b15be63f5b43)

![api-3](https://github.com/user-attachments/assets/e256f428-0920-4afb-a268-325b4ad0c6b7)

![api-4](https://github.com/user-attachments/assets/a22b02b6-d295-4b9c-a922-e3fd7932c8b1)

![api-5](https://github.com/user-attachments/assets/07a64bdb-4ada-4953-8273-5d93591206bb)

![api-6](https://github.com/user-attachments/assets/54c221cf-49cd-4725-b483-0aee8d9e3a86)

![api-7](https://github.com/user-attachments/assets/ccca054c-3b74-4083-a332-3fb7862165ed)

![api-8](https://github.com/user-attachments/assets/e3c79d2c-95fd-4f53-a098-5ee091a7958a)
