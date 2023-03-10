#  pylint: disable=line-too-long
"""Django settings for project."""

import os
import environ

# PATHS
# -----------------------------------------------------------------------------
# ({{cookiecutter.project_slug}}/config/settings/base.py - 3 = {{cookiecutter.project_slug}}/)
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('{{cookiecutter.project_slug}}')

#ENV
# -----------------------------------------------------------------------------
env = environ.Env()
# .env file, should load only in development environment
if os.path.exists(ROOT_DIR('.env')):
    env_file = ROOT_DIR('.env')
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# GENERAL
# -----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=False)
# SECRET_KEY must be overriden in production: `$openssl rand -base64 64`
SECRET_KEY = env('DJANGO_SECRET_KEY')
# ALLOWED_HOSTS must be overriden in production
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=[])

SITE_ID = 1

# Timezone and locale
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
LANGUAGES = (('en', 'English'), )
USE_I18N = True
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [ROOT_DIR('locale')]

# APP CONFIGURATION
# -----------------------------------------------------------------------------
DJANGO_APPS = [
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # Admin
    'django.contrib.admin',
]
THIRD_PARTY_APPS = [
    'django_extensions',
]
# Apps specific for this project go here.
LOCAL_APPS = [
    '{{cookiecutter.project_slug}}.core.apps.CoreConfig',
    '{{cookiecutter.project_slug}}.users.apps.UsersConfig',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# EMAIL CONFIGURATION
# -----------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

# DATABASE CONFIGURATION
# -----------------------------------------------------------------------------
DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            APPS_DIR('templates'),
        ],
        "APP_DIRS": True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                '{{cookiecutter.project_slug}}.core.contextprocessors.from_settings',
            ],
        },
    },
]

# ADMIN
# -----------------------------------------------------------------------------
ADMIN_URL = 'dashboard/'
ADMIN_SITE_HEADER = '{{cookiecutter.project_name}}'
ENVIRONMENT_NAME = env('DJANGO_ENVIRONMENT_NAME', default='DEVELOPMENT')
ENVIRONMENT_COLOR = env('DJANGO_ENVIRONMENT_COLOR', default='gray')

# STATIC FILES
# -----------------------------------------------------------------------------
STATIC_ROOT = ROOT_DIR('staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    APPS_DIR('static'),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA
# -----------------------------------------------------------------------------
MEDIA_ROOT = ROOT_DIR('media')
MEDIA_URL = '/media/'

# URL
# -----------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# PASSWORD STORAGE SETTINGS
# -----------------------------------------------------------------------------
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# PASSWORD VALIDATION
# -----------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]

# AUTHENTICATION
# -----------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
# Custom user app defaults
AUTH_USER_MODEL = 'users.User'

# CACHING
# -----------------------------------------------------------------------------
REDIS_URL = env('REDIS_URL')
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,  # keep system run even if redis failed
        }
    }
}

# LOGGING
# -----------------------------------------------------------------------------
LOGHANDLER = 'console'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'DEBUG',
        'handlers': [LOGHANDLER],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        LOGHANDLER: {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': [LOGHANDLER],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': [LOGHANDLER],
            'propagate': False,
        },
    },
}
