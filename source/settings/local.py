# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

BRAND_SHORT = BRAND_SHORT + ' -dev-'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'contrat',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '',
        'PORT': '',
    },
}

STATIC_URL = '/static/'
STATIC_ROOT = path('../storage/static/')

INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'JQUERY_URL': None,
}

SECRET_KEY = 'n&fkas87aoijw49us9((H\lkdsu90fklsjf90z09o)_1e-mtvb'