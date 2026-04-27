import logging
import os

from datetime import timedelta
from pathlib import Path
from typing import cast

from dotenv import load_dotenv

from django.urls import reverse_lazy

from logs.handler import InterceptHandler

load_dotenv('.env')

ENV_NEEDS = [
    'SECRET_KEY',
    'DEBUG',
    'ALLOWED_HOSTS',
    'CSRF_TRUSTED_ORIGINS',
    'CORS_ALLOWED_ORIGINS',
    'CORS_ALLOWED_ORIGIN_REGEXES',
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

DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = cast(str, os.getenv('ALLOWED_HOSTS')).split(',')
CSRF_TRUSTED_ORIGINS = cast(str, os.getenv('CSRF_TRUSTED_ORIGINS')).split(',')
CORS_ALLOWED_ORIGINS = cast(str, os.getenv('CORS_ALLOWED_ORIGINS')).split(',')

raw_whitelist = os.getenv('CORS_ALLOWED_ORIGIN_REGEXES', '')
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"{}".format(reg.strip()) # pylint: disable=consider-using-f-string
    for reg in raw_whitelist.split(',')
    if reg.strip()
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
] # À définir

INSTALLED_APPS = [
    "daphne",
    "django_prometheus",
    "app.apps.HealIaAppConfig",
    "core.apps.CoreConfig",
    "nutrition.apps.NutritionConfig",
    "social_network.apps.SocialNetworkConfig",
    "logs.apps.LogsConfig",
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "drf_redesign",
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "django_cleanup.apps.CleanupConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_spectacular",
    "admin_extra_buttons",
]

PAGINATION = str(os.getenv('PAGINATION')) if os.getenv('PAGINATION') is not None else '100'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': int(PAGINATION),
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

UNFOLD = {
    'SITE_TITLE': 'HealthIA',
    'SITE_HEADER': 'HealthIA',
    'SITE_SYMBOL': 'speed',
    'SITE_ICON': {
        'light': '/static/logo.webp',
        'dark': '/static/logo.webp',
    },
    'COLORS': {
        'primary': {
            '50': '#d1fae5',
            '100': '#a7f3d0',
            '200': '#6ee7b7',
            '300': '#34d399',
            '400': '#10b981',
            '500': '#059669',
            '600': '#047857',
            '700': '#065f46',
            '800': '#064e3b',
            '900': '#022c22',
            '950': "#011f18",
        },
    },
    'SITE_FAVICONS': [
        {
            'rel': 'icon',
            'sizes': '32x32',
            'type': 'image/webp',
            'href': '/static/logo.webp',
        },
    ],
    'BORDER_RADIUS': '10px',
    'DASHBOARD_CALLBACK': 'core.views.dashboard_callback',
    'SIDEBAR': {
        'show_search': True,
        'command_search': True,
        'navigation': [
            {
                'title': 'HealthIA',
                'items': [
                    {
                        'title': 'Comment',
                        'icon': 'chat',
                        'link': reverse_lazy('admin:social_network_comment_changelist'),
                    },
                    {
                        'title': 'Diet recommendations',
                        'icon': 'verified',
                        'link': reverse_lazy('admin:nutrition_dietrecommendation_changelist'),
                    },
                    {
                        'title': 'Exercices',
                        'icon': 'hiking',
                        'link': reverse_lazy('admin:app_exercice_changelist'),
                    },
                    {
                        'title': 'Foods',
                        'icon': 'nutrition',
                        'link': reverse_lazy('admin:nutrition_food_changelist'),
                    },
                    {
                        'title': 'Members',
                        'icon': 'group',
                        'link': reverse_lazy('admin:app_member_changelist'),
                    },
                    {
                        'title': 'Publications',
                        'icon': 'image',
                        'link': reverse_lazy('admin:social_network_publication_changelist'),
                    },
                    {
                        'title': 'Sessions',
                        'icon': 'timer',
                        'link': reverse_lazy('admin:app_session_changelist'),
                    },
                ],
            },
            {
                'title': 'Authentication',
                'items': [
                    {
                        'title': 'Users',
                        'icon': 'group',
                        'link': reverse_lazy('admin:auth_user_changelist'),
                    },
                    {
                        'title': 'Groups',
                        'icon': 'hub',
                        'link': reverse_lazy('admin:auth_group_changelist'),
                    },
                ],
            },
            {
                'title': 'Enums',
                'collapsible': True,
                'items': [
                    {
                        'title': 'Activities',
                        'icon': 'directions_run',
                        'link': reverse_lazy('admin:nutrition_activity_changelist'),
                    },
                    {
                        'title': 'Allergies',
                        'icon': 'medical_services',
                        'link': reverse_lazy('admin:nutrition_allergie_changelist'),
                    },
                    {
                        'title': 'Body parts',
                        'icon': 'neurology',
                        'link': reverse_lazy('admin:app_bodypart_changelist'),
                    },
                    {
                        'title': 'Categories',
                        'icon': 'category',
                        'link': reverse_lazy('admin:app_category_changelist'),
                    },
                    {
                        'title': 'Dietary restrictions',
                        'icon': 'no_meals',
                        'link': reverse_lazy('admin:nutrition_dietaryrestriction_changelist'),
                    },
                    {
                        'title': 'Disease types',
                        'icon': 'fastfood',
                        'link': reverse_lazy('admin:nutrition_diseasetype_changelist'),
                    },
                    {
                        'title': 'Equipments',
                        'icon': 'exercise',
                        'link': reverse_lazy('admin:app_equipment_changelist'),
                    },
                    {
                        'title': 'Food categories',
                        'icon': 'flatware',
                        'link': reverse_lazy('admin:nutrition_category_changelist'),
                    },
                    {
                        'title': 'Genders',
                        'icon': 'transgender',
                        'link': reverse_lazy('admin:app_gender_changelist'),
                    },
                    {
                        'title': 'Levels',
                        'icon': 'bar_chart',
                        'link': reverse_lazy('admin:app_level_changelist'),
                    },
                    {
                        'title': 'Meal types',
                        'icon': 'room_service',
                        'link': reverse_lazy('admin:nutrition_mealtype_changelist'),
                    },
                    {
                        'title': 'Muscles',
                        'icon': 'weight',
                        'link': reverse_lazy('admin:app_muscle_changelist'),
                    },
                    {
                        'title': 'Preferred cuisines',
                        'icon': 'kitchen',
                        'link': reverse_lazy('admin:nutrition_preferredcuisine_changelist'),
                    },
                    {
                        'title': 'Recommendations',
                        'icon': 'verified',
                        'link': reverse_lazy('admin:nutrition_recommendation_changelist'),
                    },
                    {
                        'title': 'Severities',
                        'icon': 'device_thermostat',
                        'link': reverse_lazy('admin:nutrition_severity_changelist'),
                    },
                    {
                        'title': 'Subscriptions',
                        'icon': 'attach_money',
                        'link': reverse_lazy('admin:app_subscription_changelist'),
                    },
                ],
            },
        ],
    },
}

MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "app.middleware.last_activity.LastActivityMiddleware",
    "logs.middleware.logging.LoggingMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

ROOT_URLCONF = "healthIA.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "healthIA.wsgi.application"
ASGI_APPLICATION = "healthIA.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}

if os.getenv("DATABASE_URL") == "sqlite:///:memory:":
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
}

logging.basicConfig(handlers=[InterceptHandler()], level=0)

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Paris"
USE_I18N = True
USE_TZ = False

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "core", "media")

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
