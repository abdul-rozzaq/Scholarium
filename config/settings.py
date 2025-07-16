from pathlib import Path
from environs import Env

from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()


SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = ["*"]


CORS_ALLOW_ALL_ORIGINS = True


SHARED_APPS = [
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.contenttypes",
    # External apps
    "django_tenants",
    "corsheaders",
    "rest_framework",
    "django_extensions",
    "rest_framework_simplejwt",
    "drf_yasg",
    # Internal apps
    "apps.schools",
    "apps.users",
]

TENANT_APPS = [
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.messages",
    # Internal apps
    "apps.courses",
]

INSTALLED_APPS = list(dict.fromkeys(SHARED_APPS + TENANT_APPS))


TENANT_MODEL = "schools.School"
TENANT_DOMAIN_MODEL = "schools.Domain"

DATABASE_ROUTERS = ("django_tenants.routers.TenantSyncRouter",)


MIDDLEWARE = [
    "django_tenants.middleware.main.TenantMainMiddleware",
    "apps.common.middlewares.TenantOnlyMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "apps.common.permissions.TenantUserPermission",
    ],
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=3),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}


SWAGGER_SETTINGS = {
    "PERSIST_AUTH": True,
    "DOC_EXPANSION": "none",
    "DEEP_LINKING": True,
}


ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django_tenants.postgresql_backend",
        "NAME": env.str("DATABASE_NAME", default="scholarium_db"),
        "USER": env.str("DATABASE_USER", default="postgres"),
        "PASSWORD": env.str("DATABASE_PASSWORD", default="yourpassword"),
        "HOST": env.str("DATABASE_HOST", default="localhost"),
        "PORT": env.str("DATABASE_PORT", default="5432"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]


LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

AUTH_USER_MODEL = "users.User"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
