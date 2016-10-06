# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

BRAND_SHORT = BRAND_SHORT + ' -stg-'

ALLOWED_HOSTS = ['10.26.16.8']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'contrat',
        'USER': 'contrat',
        'PASSWORD': 'stagingcontrat',
        'HOST': '',
        'PORT': '',
    },
}

AUTHENTICATION_BACKENDS = (
	'apps.users.backends.OpenLdapUHOBackend',
	'django.contrib.auth.backends.ModelBackend',
)

STATIC_URL = '/contratacion/static/'
STATIC_ROOT = path('../storage/static/')

SECRET_KEY = 'n&aksdjf90sdk349irrg;dsryw0e59jdfgjsipej5-y/gf.h,b'