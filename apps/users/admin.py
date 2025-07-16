from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["id", "full_name", "phone_number", "school", "role", "is_active", "is_staff", "is_superuser"]
    list_filter = ["is_active", "is_staff", "is_superuser", "role"]

    fieldsets = (
        (_("Asosiy ma'lumotlar"), {"fields": ("phone_number", "full_name", "password", "role", "school")}),
        (_("Ruxsatlar"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Tizim ma'lumotlari"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            _("Yangi foydalanuvchi"),
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "full_name",
                    "password1",
                    "password2",
                    "role",
                    "school",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

    search_fields = ["phone_number", "full_name"]
