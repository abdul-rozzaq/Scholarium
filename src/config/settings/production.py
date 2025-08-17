# ruff: noqa: F405 F403

from .base import *

DEBUG = False

ALLOWED_HOSTS = env.str("ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = env.str("CSRF_TRUSTED_ORIGINS").split(",")
