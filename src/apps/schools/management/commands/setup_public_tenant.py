from django.core.management.base import BaseCommand
from apps.schools.models import School, Domain


class Command(BaseCommand):
    help = "Sets up a default tenant for local development"

    def handle(self, *args, **kwargs):
        tenant, created = School.objects.get_or_create(
            name="Public Tenant",
            schema_name="public",
        )

        domain, created = Domain.objects.get_or_create(
            domain="127.0.0.1",
            tenant=tenant,
            is_primary=True,
        )

        domain, created = Domain.objects.get_or_create(
            domain="localhost",
            tenant=tenant,
            is_primary=True,
        )

        self.stdout.write(self.style.SUCCESS(f"Tenant {tenant.name} created or updated"))
