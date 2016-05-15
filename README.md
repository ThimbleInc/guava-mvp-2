# guava-mvp-2

I'm just dumping everything here. But when this gets too big we can move it into the wiki

- Container = Docker Container
- Service = Isolated Programmatic entity centered around a single business responsibility

## Local Set Up
For this project we are developing locally using Docker. There are 4 main containers: 
- nginx: webserver
- backend: django app
- postgres: database
- postgresdata: container volume for database

To start, install Docker from https://www.docker.com/products/docker-toolbox
- Then create a docker-machine: 
  `docker-machine create --driver virtual-box guava`
- Then connect to the docker daemon (must do this everytime you open a new terminal)
  `eval $(docker-machine env default)`
- Also, make sure to grab the ip of the Virtual Machine. This is the ip that will allow you to access the website locally:
  `docker-machine ip guava`
- Now you can run the containers using Docker Compose:
  `docker-compose up`: Note this will take a minute or two

Set up your database:
- access the db and create the database guava via the command line: `psql -U postgres -h <docker-ip>` `create database guava;`
- load the db with the tables: `docker-compose exec backend python manage.py migrate`

Finally, set up a superuser for yourself: `docker-compose exec backend python manage.py createsuperuser`, and follow the directions. 

Now you can view the website in browser at the ip-address

## Basic Architecture
One of the things I wanted to try out was Service Oriented Architecture. The backend of this project is made in Django, but utilizes Django's concept of apps to create microservices. These microservices are isolated entities that are in charge of their own data models, and cannot access other services data model. All services expose an an api for that allows external entities to interact with its data model. 

Currently, backend services are encapsulated in the backend container, but can theoretically be broken out into their own container with their own data stores. For now, to keep it simple, they are in one container and share the same data store (but not models). 

Since each service exposes an api, different front end layers can interact, and coordinate the services via HTTP requests. I.e. iOS app, android app, web frontend etc... This part is still TBD

## References
#### Useful Commands
Working with Django and Docker simplifies developing websites greatly by automating many of the mundane and tedious tasks. However, this requires you to understand the different commands in place to run those automations. 
To run django commands you have to do this: `docker-compose exec backend python manage.py <command>` 

- List of Django commands: https://docs.djangoproject.com/en/1.9/ref/django-admin/
- List of Docker commands: https://github.com/wsargent/docker-cheat-sheet

#### Django
- Models: https://docs.djangoproject.com/en/1.9/ref/models/
- Settings: https://docs.djangoproject.com/en/1.9/ref/settings/
#### Django Rest Framework
Used to make our backend an api 
- http://www.django-rest-framework.org/

## Production Deployment
- TBD 
