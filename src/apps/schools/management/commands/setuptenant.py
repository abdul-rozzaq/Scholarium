from django.core.management.base import BaseCommand
from apps.schools.models import School, Domain


class Command(BaseCommand):
    help = "Sets up a default tenant for local development"

    def add_arguments(self, parser):
        parser.add_argument("--domain", type=str, help="Domain for the tenant (default: 127.0.0.1)", default="127.0.0.1")
        parser.add_argument("--name", type=str, help="School name (default: domain value)")
        parser.add_argument("--schema", type=str, help="Schema name (default: domain value)")

    def handle(self, *args, **options):
        domain_value = options["domain"]
        schema_name = options["schema"] or domain_value
        name = options["name"] or schema_name

        tenant, created = School.objects.get_or_create(schema_name=schema_name, defaults={"name": name})

        domain, created = Domain.objects.get_or_create(
            domain=domain_value,
            defaults={
                "tenant": tenant,
                "is_primary": True,
            },
        )

        self.stdout.write(self.style.SUCCESS(f"Tenant {tenant.name} created or updated"))
