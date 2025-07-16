from django_tenants.models import TenantMixin, DomainMixin
from django.db import models


class School(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    telegram_bot_token = models.CharField(max_length=255, null=True, blank=True, default=None)
    auto_create_schema = True


class Domain(DomainMixin):
    pass
