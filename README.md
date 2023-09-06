
<p align='center'>

![logo_two.svg](auths%2Fstatic%2Fsvg%2Flogo_two.svg)

</p>

# GhostTalk
GhostTalk is chat web application designed using django MVT(Model View Template)
.The application is designed for people to connect together while their identity remains a secrete 
.The application also provides platforms such as Ghost secrete where users intend to keep information
either personal or from the public.

# Motivation 💪🏻
 Using various anonymous chat application, the dread to uncover how they function and work under the hood
is a fuel to make an anonymous chat application. To make thing much fun, the GhostTalk application 
allows multiple users to  chat simultaneously in real time.

# 🔥Output


# Technology Used To Develop GhostTalk 🛠
The GhostTalk application uses the following technology or tools:<br/> 

- Django(Python Web Framework)
- Jinja (Django templating language)
- JavaScript (Scripting Language)
- PostgresSQL
- django-channels
- docker
- redis
- CSS3

# How to use 
## 🔥Cloning the application
- click the fork icon in the top right conner of this repository 
- from the repo you forked to your account click code then copy the ssh or https link 
- create a directory for your project then write this in the terminal

 ```commandline
 git clone 'https-or-ssh-link'
 cd project_file
 ```

## 💨Running the application 
1. using pyhon environment 
2. using Docker

### 🐍Using python environment 
Install necessary requirements and make necessary migrations

```dotenv
# postgres enviroment variables 
    DB_PASSWORD='your_password'
    DB_NAME='db_name'
    DB_USER='postgres'
    DB_PORT=''
    DB_HOST=''
```
Or using SQLite<br/>
```python
DATABASES = {
    'default': {
     'ENGINE': 'django.db.backends.sqlite3', 
     'NAME': 'new.db',
    }
}
```
requirements and running 
```commandline
  pip install -r requirements.txt  
  py manage.py makemigrations
  py manage.py migrate
  py manage.py runserver
```

### 📦Using Docker

```commandline
    docker-compose build
    docker-compose up
```
