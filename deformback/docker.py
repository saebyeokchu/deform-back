from .base import *

ALLOWED_HOSTS = ["localhost", "59.23.104.33"]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'deform',
            'USER': 'postgres',
            'PASSWORD': 'deformeditoradmin',
            'HOST': 'host.docker.internal',
            'PORT': '5432',
            }
        }
