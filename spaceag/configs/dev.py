import os

from spaceag.configs.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db'
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }

STATIC_ROOT = os.path.join(os.path.abspath(os.path.join(BASE_DIR, os.pardir)), 'static')
# STATICFILES_DIRS = (os.path.join(os.path.abspath(os.path.join(BASE_DIR, os.pardir)), 'static'),)