from decouple import config
from .base import *

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "59.23.104.33"]

DATABASE_USER = config('DEV_DB_USER')
DATABASE_PASSWORD = config('DEV_DB_PASSWORD')

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'editor',
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD, #dgepw
            'HOST': '127.0.0.1',
            'PORT': '5432',
            }
        }
