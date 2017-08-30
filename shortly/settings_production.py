from shortly.settings import *

ALLOWED_HOSTS = ['*',]

DEBUG = False


DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'shortly',
      'USER': 'u_shortly',
      'PASSWORD': '123',
      'HOST': 'localhost',
      'PORT': '',
  }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'
STATICFILES_DIRS = [..DIRS..]
