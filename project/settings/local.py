import os
import sys

from common import *  # NOQA

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = '*'

SECRET_KEY = "secret_key"

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASS'],
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
