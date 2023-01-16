# DJango-Github-API-Backend

This is a Django-based backend for a DJango REST API . It allows you to access github rest api endpoints(like username,repostories ..etc).

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


## Prerequirities
- Python 3.7+
- Django 3.2+
- Django REST framework
- pip
- Other dependencies listed in `requirements.txt`

# Installation

## 1.Clone the repository
Copy code
```bash
git clone https://github.com/as4c/Django-Github-Api-backend.git
```
## 2.Create a virtual environment and activate it
Copy code
```bash
python -m venv venv
source venv/bin/activate
```
## 3.Install the required packages
Copy code
```bash
pip install -r requirements.txt
```

## 4.Make migrations and migrate

Copy code
```bash
python manage.py makemigrations
python manage.py migrate
```
## 5.Create a superuser
Copy code
```bash
python manage.py createsuperuser
```
## 6.Run the server
Copy code
```bash
python manage.py runserver
```
## API Endpoints
The API endpoints are listed in gitrepobackend/urls.py that is the following :
```bash
/api/user/<str:username> - for sending requests from backend to github rest api server
```
## 7.Testing
Run the following command to run tests
Copy code
```bash
python manage.py test
```
## Screenshots
After running the server it will look like that-
![App Screenshot]('https://github.com/as4c/Django-Github-Api-backend/blob/master/User%20%E2%80%93%20Django%20REST%20framework.png')
# Built With
Django - The web framework used
# Django REST framework - Used for building RESTful API
# Authors
sagar kumar- as4c
# License
This project is licensed under the MIT License - see the LICENSE.md file for details

# Acknowledgments
some youtube chanel
