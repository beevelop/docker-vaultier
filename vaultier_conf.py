"""
Vaultier configuration file
"""

from vaultier.settings.prod import *
import os

DEBUG = True

DATA_DIR = '/opt/vaultier/data'

RAVEN_CONFIG = {
    'dsn': os.environ.get('RAVEN_DSN', '')
}

aHost = os.environ.get('WEBLATE_ALLOWED_HOSTS', ['localhost', '127.0.0.1'])
ALLOWED_HOSTS = aHost.split(',') if isinstance(aHost, str) else aHost

VAULTIER.update({
    'raven_key': '',
    'registration_allow': False,
    'allow_anonymous_usage_statistics': False,
    'from_email': 'noreply@example.com',
})

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(DATA_DIR, 'static')
STATIC_URL = '/static/'

SECRET_KEY = os.environ.get('SECRET_KEY', 'b*hm3x8g_)3&xj8mvygbupqm%iyy^3kjq1(*^y+puxtgr(yacg');

DATABASES = {}

if 'DATABASE_PORT_3306_TCP_ADDR' in os.environ:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_ENV_MYSQL_DATABASE'],
        'TEST': {'NAME': os.environ['DATABASE_ENV_MYSQL_DATABASE']},
        'USER': os.environ['DATABASE_ENV_MYSQL_USER'],
        'PASSWORD': os.environ['DATABASE_ENV_MYSQL_PASSWORD'],
        'HOST': os.environ['DATABASE_PORT_3306_TCP_ADDR'],
        'PORT': os.environ['DATABASE_PORT_3306_TCP_PORT'],
        'OPTIONS': {
           'init_command': 'SET storage_engine=INNODB',
           'charset': 'utf8',
        }
    }
elif 'DATABASE_PORT_5432_TCP_ADDR' in os.environ:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_ENV_POSTGRES_USER'],
        'TEST': {'NAME': os.environ['DATABASE_ENV_POSTGRES_USER']},
        'USER': os.environ['DATABASE_ENV_POSTGRES_USER'],
        'PASSWORD': os.environ['DATABASE_ENV_POSTGRES_PASSWORD'],
        'HOST': os.environ['DATABASE_PORT_5432_TCP_ADDR'],
        'PORT': os.environ['DATABASE_PORT_5432_TCP_PORT'],
    }
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'vaultier.db')
    }

# url of site used in emailing, templates and so.
SITE_URL = 'http://example.com/'

# Email server
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
