# ruff: noqa: F405 F403

from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django_tenants.postgresql_backend",
        "NAME": env.str("POSTGRES_DB", default="scholarium_db"),
        "USER": env.str("POSTGRES_USER", default="postgres"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", default="yourpassword"),
        "HOST": env.str("POSTGRES_HOST", default="localhost"),
        "PORT": env.str("POSTGRES_PORT", default="5432"),
    }
}

INSTALLED_APPS += [
    # "silk",
    "query_counter",
]

MIDDLEWARE += [
    # "silk.middleware.SilkyMiddleware",
    "query_counter.middleware.DjangoQueryCounterMiddleware",
]
