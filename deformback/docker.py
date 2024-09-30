from .base import *

ALLOWED_HOSTS = ["localhost", "59.23.104.33"]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'deform',
            'USER': 'postgres',
            'PASSWORD': '1234',
            'HOST': 'host.docker.internal',
            'PORT': '5432',
            }
        }
