from .base import *

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "59.23.104.33"]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'editor',
            'USER': 'postgres',
            'PASSWORD': '1234', #dgepw
            'HOST': '127.0.0.1',
            'PORT': '5432',
            }
        }
