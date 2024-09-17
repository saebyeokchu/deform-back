from .base import *

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "59.23.104.33"]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'deform',
            'USER': 'postgres',
            'PASSWORD': 'deformeditoradmin',
            'HOST': '127.0.0.1',
            'PORT': '5432',
            }
        }
