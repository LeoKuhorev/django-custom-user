# Lab-29 Django-Custom-User

## Feature Tasks and Requirements
- create Django application from scratch that has a custom user model named CustomUser
    - Custom user should use email instead of username for signup / login
    - Application should work with Django Admin

## AUTHORS

[_Leo Kukharau_](https://github.com/LeoKuhorev)

## GETTING STARTED:

- `poetry shell` to start your virtual environment
- `poetry install` to install dependencies
- create .env file with listed <a href="#env">below</a> variables and save it into 'server' directory
- `python manage.py makemigrations` - to generate DB schema
- `python manage.py migrate` - to create DB schema
- `python manage.py createsuperuser` - to create user with admin access
- `python manage.py runserver` - to run server

### <a name="env"></a> ENV variables:

SECRET_KEY=secret key for the app (typically 50-characters long string)  
DEBUG=should be set to True in development  
ALLOWED_HOSTS=localhost,127.0.0.1

## API:

`/` - landing page;  
`user/register/` - register page, handles user registration;  
`user/login/` - login page, allows a user to log in;  
`user/profile/` - profile page, allows a user to view and edit their profile information (login required);  
`user/logout/` - logout page, is shown when a user it logged out (login required);  
`admin/` - site admin page;


### Dependency Documentation:

[Python (v. 3.8)](https://docs.python.org/3.8/)  
[Django (v. 3.1)](https://docs.djangoproject.com/en/3.1/)  
[Django Crispy Forms (v. 1.9.2)](https://pypi.org/project/django-crispy-forms/)  
[Django Environ (v. 0.4.5)](https://pypi.org/project/django-environ/)  

### Dev Dependencies:

[Pylint-Django (v. 2.3.0)](https://pypi.org/project/pylint-django/)