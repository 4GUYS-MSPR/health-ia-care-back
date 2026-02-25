import os
import logging

from datetime import timedelta
from pathlib import Path
from typing import cast

from dotenv import load_dotenv

from logs.handler import InterceptHandler

load_dotenv('.env')

ENV_NEEDS = [
    'SECRET_KEY',
    'DJANGO_DEBUG',
    'ALLOWED_HOSTS',
    'CSRF_TRUSTED_ORIGINS',
    'CORS_ALLOWED_ORIGINS',
    'PAGINATION',
    'POSTGRES_DB',
    'POSTGRES_USER',
    'POSTGRES_PASSWORD',
    'POSTGRES_PORT',
    'POSTGRES_HOST'
]
for x in ENV_NEEDS:
    ENV = os.getenv(x)
    if not ENV:
        raise ValueError(f"{x} environment variable not set")

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DJANGO_DEBUG') == 'True'

ALLOWED_HOSTS = cast(str, os.getenv('ALLOWED_HOSTS')).split(',')
CSRF_TRUSTED_ORIGINS = cast(str, os.getenv('CSRF_TRUSTED_ORIGINS')).split(',')
CORS_ALLOWED_ORIGINS = cast(str, os.getenv('CORS_ALLOWED_ORIGINS')).split(',')

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
] # À définir

INSTALLED_APPS = [
    'jazzmin',
    'drf_redesign',
    'app.apps.HealIaAppConfig',
    'core.apps.CoreConfig',
    'logs.apps.LogsConfig',
    'nutrition.apps.NutritionConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_spectacular',
    'admin_extra_buttons',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': int(os.getenv('PAGINATION')),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'HealthIA API',
    'DESCRIPTION': 'API documentation for HealthIA',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SERVE_PERMISSIONS': [
        'rest_framework.permissions.IsAdminUser'
    ],
}

JAZZMIN_SETTINGS = {
    "custom_css": "css/admin_custom.css",
    "site_brand": "HealthIA",
    "site_header": "HealthIA",
    "site_logo": "/logo.webp",
    "site_title": "HealthIA",
    "welcome_sign": "Welcome to HealthIA !",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'logs.middleware.logging.LoggingMiddleware',
]

ROOT_URLCONF = 'healthIA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'healthIA.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}

if os.getenv('DATABASE_URL') == "sqlite:///:memory:":
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}

logging.basicConfig(handlers=[InterceptHandler()], level=0)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
