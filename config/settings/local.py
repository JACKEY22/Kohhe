from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kmd@5b2&mbtb5sd7jd58g=&w%q5si_bn2_&=y=9&4n=d2uq4@c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}