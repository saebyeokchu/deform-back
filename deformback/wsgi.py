"""
WSGI config for deformback project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deformback.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deformback.docker')

application = get_wsgi_application()
