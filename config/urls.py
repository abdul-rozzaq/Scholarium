from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Scholarium API",
        default_version="v1",
        description="API documentation for Scholarium",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


api_urls = [
    path("auth/", include("apps.users.urls")),
    path("courses/", include("apps.courses.urls")),
    path("school/", include("apps.schools.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_urls)),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
