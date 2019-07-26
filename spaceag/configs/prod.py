import os

from spaceag.configs.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db_postgres',
        'PORT': 5432,
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join((os.path.dirname(BASE_DIR)), 'static')