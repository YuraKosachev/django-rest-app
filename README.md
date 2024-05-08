# django-rest-app
django-rest project architecture
# Create the project directory
mkdir tutorial
cd tutorial

# Create a virtual environment to isolate our package dependencies locally
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..

# if you using postgresql
pip install psycopg2 

python manage.py migrate

# create super user 
python manage.py createsuperuser --username admin --email admin@example.com

python manage.py runserver    

# Setup swagger UI
pip install django-rest-swagger

settings.py

REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }

INSTALLED_APPS = [
    ...
    'rest_framework_swagger',
    ...
]

pip install  drf-yasg

pip install django-filter