from django.urls import path

from .views import GetUpdateShopAPIView


urlpatterns = [
    path("", GetUpdateShopAPIView.as_view()),
]
