"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# check running on docker
if not os.path.exists("/.dockerenv"):
    from dotenv import load_dotenv

    load_dotenv(os.path.join(str(BASE_DIR), "django.env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "account",
    "core",
    "timemanager",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# auth user model
AUTH_USER_MODEL = "account.Organization"

# CORS
# CORS_ORIGIN_ALLOW_ALL = True
# nextを動かすサーバーを以下に追加する or 上記のCORS_ORIGIN_ALLOW_ALLをTrueにする
CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://127.0.0.1:3000",
)

# rest framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAdminUser"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}

# authentication
LOGIN_URL = "/api-auth/login"
LOGIN_REDIRECT_URL = "/api//waiting_time_history"

# logging
LOG_HANDLER_LEVEL = os.environ.get("DJANGO_LOG_HANDLER_LEVEL", "WARNING")
LOG_HANDLER_LEVEL_NULL = os.environ.get("DJANGO_LOG_HANDLER_LEVEL_NULL", LOG_HANDLER_LEVEL)
LOG_HANDLER_LEVEL_CONSOLE = os.environ.get("DJANGO_LOG_HANDLER_LEVEL_CONSOLE", LOG_HANDLER_LEVEL)
LOG_HANDLER_LEVEL_MAIL = os.environ.get("DJANGO_LOG_HANDLER_LEVEL_MAIL", LOG_HANDLER_LEVEL)
LOG_HANDLER_LEVEL_FILE = os.environ.get("DJANGO_LOG_HANDLER_LEVEL_FILE", LOG_HANDLER_LEVEL)
LOG_HANDLER_FILE_PATH = os.environ.get("DJANGO_LOG_HANDLER_FILE_PATH", "/var/log/django.log")
LOG_LOGGER_LEVEL = os.environ.get("DJANGO_LOG_LOGGER_LEVEL", "WARNING")
LOG_FILE_MAX_BYTES = int(os.environ.get("DJANGO_LOG_FILE_MAX_BYTES", 1024 * 1024))
LOG_FILE_BACKUP_COUNT = int(os.environ.get("DJANGO_LOG_FILE_BACKUP_COUNT", 5))

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s"},
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {},
    "handlers": {
        "null": {
            "level": LOG_HANDLER_LEVEL_NULL,
            "class": "logging.NullHandler",
        },
        "console": {
            "level": LOG_HANDLER_LEVEL_CONSOLE,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "mail": {
            "level": LOG_HANDLER_LEVEL_MAIL,
            "class": "django.utils.log.AdminEmailHandler",
        },
        "file": {
            "level": LOG_HANDLER_LEVEL_FILE,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_HANDLER_FILE_PATH,
            "formatter": "verbose",
            "maxBytes": LOG_FILE_MAX_BYTES,
            "backupCount": LOG_FILE_BACKUP_COUNT,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["null"],
            "propagate": True,
            "level": LOG_LOGGER_LEVEL,
        },
        "django.security.csrf": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
            "propagate": False,
        },
        "config": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
        },
        "account": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
        },
        "core": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
        },
        "timemanager": {
            "handlers": ["console", "file"],
            "level": LOG_LOGGER_LEVEL,
        },
    },
}
