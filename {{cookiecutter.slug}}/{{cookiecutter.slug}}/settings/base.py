"""
Django settings for {{cookiecutter.project}}.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""


from email.utils import getaddresses
from pathlib import Path

from environ import Env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
APP_DIR = BASE_DIR / "{{cookiecutter.slug}}"


# Django-environ
# https://django-environ.readthedocs.io/en/latest/

env = Env()
env.read_env(BASE_DIR / ".env")


# Application definition

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "widget_tweaks",
    # {{cookiecutter.project}}
    "{{cookiecutter.slug}}.core",
    "{{cookiecutter.slug}}.members",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # https://whitenoise.evans.io/en/latest/django.html#enable-whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{{cookiecutter.slug}}.urls"

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

WSGI_APPLICATION = "{{cookiecutter.slug}}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {
    "default": env.db(default="sqlite:///db.sqlite3"),
}


# Cache
# https://docs.djangoproject.com/en/stable/ref/setting/#caches

CACHES = {
    "default": env.cache(default="locmemcache://"),
}


# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
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


# Password hashing
# https://docs/djangoproject.com/en/stable/topics/auth/passwords/#using-argon2-with-django

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]


# Custom user model
# https://docs.djangoproject.com/en/stable/topics/auth/customizing/#substituting-a-custom-user-model

AUTH_USER_MODEL = "members.Member"
LOGIN_URL = "auth:login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"


# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = env("LANGUAGE_CODE", default="en-us")

LOCALE_PATHS = [APP_DIR / "locale"]

TIME_ZONE = env("TIME_ZONE", default="UTC")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/


STATIC_HOST = env("DJANGO_STATIC_HOST", default="")
STATIC_ROOT = env("DJANGO_STATIC_ROOT", default=BASE_DIR / "static_files")
STATIC_URL = f"{STATIC_HOST}/static/"
# https://whitenoise.evans.io/en/latest/django.html#add-compression-and-caching-support
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        # https://whitenoise.readthedocs.io/en/latest/django.html#add-compression-and-caching-support
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Media files (user uploaded)
# https://docs.djangoproject.com/en/stable/topics/files/

MEDIA_ROOT = env("DJANGO_MEDIA_ROOT", default=BASE_DIR / "media_files")
MEDIA_URL = "/media/"


# Default primary key field type
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Email
# https://docs.djangoproject.com/en/stable/topics/email/

EMAIL_CONFIG = env.email_url("EMAIL_URL", default="consolemail://")
vars().update(EMAIL_CONFIG)
ADMINS = getaddresses([env("DJANGO_ADMINS", default="")])
MANAGERS = getaddresses([env("DJANGO_MANAGERS", default="")])
DEFAULT_FROM_EMAIL = env("DJANGO_FROM_EMAIL", default="webmaster@localhost")
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default="root@localhost")
