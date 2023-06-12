from .base import *

SECRET_KEY = 'django-insecure-v1%u$ytm&g@qr_^hi5#-jfizwncnox2(jh&vq!6zv91aljb*xi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
# this disables Cross domain requests
CORS_ORIGIN_ALLOW_ALL = False 

# this allows cookie being passed cross domain    
CORS_ALLOW_CREDENTIALS = True 
CORS_ALLOWED_ORIGINS = ["http://localhost:8100"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'mywallet',

        'USER': 'mywallet',

        'PASSWORD': 'mywallet',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}
