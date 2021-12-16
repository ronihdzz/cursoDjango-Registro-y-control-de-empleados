from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER':get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT':'5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# esta sera la URL que djando usara para acceder a los archivos estaticos
STATIC_URL = '/static/'
# esta contendra la ubicación de las carpetas que almacenan el contenido
# estatico de la pagina web

import os


STATICFILES_DIRS =  [
                        str(BASE_DIR)+os.sep+'static',

                    ]
# esta sera la URL que djando usara para acceder a los archivos media
MEDIA_URL='/media/'

# esta sera la ruta en donde se encuentren todos los archivos media
MEDIA_ROOT=str(BASE_DIR)+os.sep+'media'