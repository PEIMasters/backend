# ---------------------------------------------------------------------------- #

"""
Django settings for tuichain project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

# ---------------------------------------------------------------------------- #

from dotenv import load_dotenv
from os import environ
from pathlib import Path
from tuichain_ethereum import Address, PrivateKey
from web3 import (
    EthereumTesterProvider,
    HTTPProvider,
    IPCProvider,
    WebsocketProvider,
)

# ---------------------------------------------------------------------------- #

dotenv_path = Path(__file__).resolve().parent.parent / ".env"

if dotenv_path.exists():
    load_dotenv(dotenv_path)

# ---------------------------------------------------------------------------- #

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = {"True": True, "False": False}[environ["DEBUG"]]

ALLOWED_HOSTS = environ["ALLOWED_HOSTS"].split()

# ---------------------------------------------------------------------------- #
# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # Django Rest Framework
    "rest_framework",
    "rest_framework.authtoken",
    # Apps
    "tuichain.api",
    # Documentation
    "drf_yasg",
    # CORS
    "corsheaders",
]

if environ["FRONTEND_DIR"]:
    INSTALLED_APPS.append("django.contrib.staticfiles")

MIDDLEWARE = [
    # CORS
    "corsheaders.middleware.CorsMiddleware",
    # Django
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tuichain.urls"

WSGI_APPLICATION = "tuichain.wsgi.application"

# ---------------------------------------------------------------------------- #
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

if environ["FRONTEND_DIR"]:

    FRONTEND_DIR = Path(environ["FRONTEND_DIR"])

    STATIC_URL = "/static/"
    STATICFILES_DIRS = [FRONTEND_DIR / "static"]
    STATICFILES_STORAGE = None
    STATICFILES_FINDERS = [
        "django.contrib.staticfiles.finders.FileSystemFinder"
    ]

else:

    FRONTEND_DIR = None

# ---------------------------------------------------------------------------- #
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": environ["DATABASE_ENGINE"],
        "NAME": environ["DATABASE_NAME"],
        "USER": environ["DATABASE_USER"],
        "PASSWORD": environ["DATABASE_PASSWORD"],
        "HOST": environ["DATABASE_HOST"],
        "PORT": environ["DATABASE_PORT"],
    }
}

# ---------------------------------------------------------------------------- #
# Email

EMAIL_USE_TLS = {"True": True, "False": False}[environ["EMAIL_USE_TLS"]]
EMAIL_PORT = int(environ["EMAIL_PORT"])
EMAIL_HOST = environ["EMAIL_HOST"]
EMAIL_HOST_USER = environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = environ["EMAIL_HOST_PASSWORD"]
EMAIL_BACKEND = environ["EMAIL_BACKEND"]

# ---------------------------------------------------------------------------- #
# Ethereum

eth_provider = environ["ETHEREUM_PROVIDER"]
eth_master_acc = environ["ETHEREUM_MASTER_ACCOUNT_PRIVATE_KEY"]
eth_controller_address = environ["ETHEREUM_CONTROLLER_ADDRESS"]

if eth_provider == "test":
    ETHEREUM_PROVIDER = EthereumTesterProvider()
elif eth_provider.startswith("http://") or eth_provider.startswith("https://"):
    ETHEREUM_PROVIDER = HTTPProvider(eth_provider)
elif eth_provider.startswith("ws://"):
    ETHEREUM_PROVIDER = WebsocketProvider(eth_provider)
else:
    ETHEREUM_PROVIDER = IPCProvider(eth_provider)

ETHEREUM_MASTER_ACCOUNT_PRIVATE_KEY = (
    PrivateKey(bytes.fromhex(eth_master_acc)) if eth_master_acc else None
)

ETHEREUM_CONTROLLER_ADDRESS = (
    Address(eth_controller_address) if eth_controller_address else None
)

# ---------------------------------------------------------------------------- #
# CORS

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# ---------------------------------------------------------------------------- #
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# ---------------------------------------------------------------------------- #
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---------------------------------------------------------------------------- #
# REST

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        #'rest_framework.authentication.SessionAuthentication'
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        #     'rest_framework.permissions.IsAuthenticated',
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ),
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
        }
    },
}

# ---------------------------------------------------------------------------- #
