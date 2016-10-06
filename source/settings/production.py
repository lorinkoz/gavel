# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import *


def config(dir, default=''):
    dir = path(dir)
    try:
        with open(dir, 'rb+') as f:
            return f.read().strip()
    except:
        return default


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['sistemas.vrea.uho.edu.cu']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'contrat',
        'USER': 'contrat',
        'PASSWORD': config('../storage/config/dbpwd'),
        'HOST': '',
        'PORT': '',
    },
}

AUTHENTICATION_BACKENDS = (
    'apps.users.backends.OpenLdapUHOBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SESSION_COOKIE_AGE = 14400
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = CSRF_COOKIE_SECURE = True

STATIC_URL = '/contratacion/static/'
STATIC_ROOT = path('../storage/static/')

SECRET_KEY = config('../storage/config/hash')