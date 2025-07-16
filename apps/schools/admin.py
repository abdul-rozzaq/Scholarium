from django.contrib import admin


from .models import Domain, School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "created_on", "schema_name"]


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ["pk", "tenant", "domain"]
