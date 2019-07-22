"""
Django settings for scarylog project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = eval(os.getenv('DEBUG'))

ALLOWED_HOSTS = ['scarylog.com', 'www.scarylog.com', '127.0.0.1', 'localhost']
INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'location_field.apps.DefaultConfig',
    'crispy_forms',
    'ckeditor',
    'stdimage',
    'django_select2',
    'algoliasearch_django',
    'story',
    'apps.profile',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # 'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',


]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',

]

ROOT_URLCONF = 'scarylog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'scarylog.context_processors.template_global_params',
            ],
        },
    },
]

WSGI_APPLICATION = 'scarylog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http" if DEBUG else "https"
LOGIN_REDIRECT_URL = '/profile/update/'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
AUTH_PROFILE_MODULE = 'apps.profile.UserProfile'

DEFAULT_HTTP_PROTOCOL = "https"
SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email'],
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bangkok'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROLLBAR = {
    'access_token': os.getenv('ROLLBAR_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'root': BASE_DIR,
}


import rollbar
rollbar.init(**ROLLBAR)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets/'),
]

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SECURE_URLS = True
AWS_DEFAULT_ACL = 'private'
STATIC_URL = '/assets/' if DEBUG else 'https://cdn.scarylog.com/'


if not DEBUG or 'collectstatic' in sys.argv:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_S3_CUSTOM_DOMAIN = 'cdn.scarylog.com'

else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/')
    INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar', ]
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware', ] + MIDDLEWARE
    LOCATION_FIELD_PATH = STATIC_URL + 'location_field'


LOCATION_FIELD = {
    'map.provider': 'mapbox',
    'map.zoom': 12,

    # Mapbox
    'provider.mapbox.access_token': 'pk.eyJ1Ijoic2Nhcnlsb2ciLCJhIjoiY2p4b2xnOHRwMDg4MDNudXF2dnNoZ2w3NCJ9.ptdreoxFUFHQZAW2VQuzTw',
    'provider.mapbox.max_zoom': 12,
    'provider.mapbox.id': 'scarylog.cjxomi1xz2m8y1cmy5cpcw2ol',

    # misc
    'resources.root_path': 'https://cdn.scarylog.com/location_field',
    'resources.media': {
        'js': (
            'https://cdn.scarylog.com/location_field' + '/js/form.js',
            'https://cdn.scarylog.com/location_field' + '/leaflet.js',
        ),
    },
}

ALGOLIA = {
    'APPLICATION_ID': os.getenv('ALGOLIA_APPLICATION_ID'),
    'API_KEY': os.getenv('ALGOLIA_API_KEY')
}


CRISPY_TEMPLATE_PACK = 'bootstrap4'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_story': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', ]},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            '/',  # put this to force next toolbar on new line
        ],
        'toolbar': 'story',
    },
}
