from .base import *
from decouple import config

ALLOWED_HOSTS = ["localhost", "59.23.104.33"]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DOCKER_DB_NAME'),
            'USER': config('DOCKER_DB_USER'),
            'PASSWORD': config('DOCKER_DB_PASSWORD'), #deformeditoradmin
            'HOST': config('DOCKER_DB_HOST'),
            'PORT': '5432',
            }
        }


# DATABASE_USER = config('DOCKER_DB_USER')
# DATABASE_PASSWORD = config('DOCKER_DB_PASSWORD')

# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'editor',
#             'USER': DATABASE_USER,
#             'PASSWORD': DATABASE_PASSWORD, #deformeditoradmin
#             'HOST': 'host.docker.internal',
#             'PORT': '5432',
#             }
#         }
