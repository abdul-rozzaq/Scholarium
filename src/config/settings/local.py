# ruff: noqa: F405 F403

from .base import *

DEBUG = True

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

INSTALLED_APPS += [
    # "silk",     
    # 'query_counter',
]

MIDDLEWARE += [
    # "silk.middleware.SilkyMiddleware",
    "query_counter.middleware.DjangoQueryCounterMiddleware",
]

INTERNAL_IPS = ["127.0.0.1"]
