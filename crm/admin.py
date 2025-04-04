from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class UserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = User
    list_display = ("id", "first_name", "last_name", "phone", "role", "is_active", "is_staff")
    list_filter = ("role", "is_active", "is_staff")
    search_fields = ("first_name", "last_name", "phone")
    ordering = ("first_name",)

    fieldsets = (
        (None, {"fields": ("password",)}),
        ("Personal Info", {"fields": ("first_name", "last_name", "phone", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important Dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "phone", "password1", "password2", "role", "is_active", "is_staff"),
            },
        ),
    )
