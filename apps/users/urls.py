from django.urls import path
from .views import PhoneLoginAPIView, RefreshTokenAPIView, WhoAmIAPIView

urlpatterns = [
    path("login/", PhoneLoginAPIView.as_view(), name="phone_login"),
    path("refresh/", RefreshTokenAPIView.as_view(), name="refresh_token"),
    path("whoami/", WhoAmIAPIView.as_view(), name="whoami"),
]
