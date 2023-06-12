from .base import *
from decouple import config

SECRET_KEY = 'django-insecure-v1%u$ytm&g@qr_^hi5#-jfizwncnox2(jh&vq!6zv91aljb*xi'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# this disables Cross domain requests
CORS_ORIGIN_ALLOW_ALL = False 

# this allows cookie being passed cross domain    
CORS_ALLOW_CREDENTIALS = True 
ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = ["com.mywallet.personal","http://localhost:8100","http://localhost"]




DEBUG_PROPAGATE_EXCEPTIONS = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'ous3ma$mywallet',

        'USER': 'ous3ma',

        'PASSWORD': '#Ou553m4',

        'HOST': 'ous3ma.mysql.pythonanywhere-services.com',

        'PORT': '3306',

    }
}
LOGGING = {'version': 1,
           'ldisable_existing_loggers': False,
           'formatters': {
               'verbose': {
                   'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                   'datefmt': "%d/%b/%Y %1:%M:%S"
               },
               'simple': {
                   'format': '%(levelname)s %(message)s'
               },
           },
           'handlers': {
               'console': {
                   'level': 'DEBUG',
                   'class': 'logging.StreamHandler',
               },
           },
           'loggers': {
               'MYAPP': {
                   'handlers': ['console'],
                   'level': 'DEBUG',
               },
           }
           }
