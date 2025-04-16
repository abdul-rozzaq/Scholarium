from rest_framework.routers import DefaultRouter
from .views import StaffViewSet, RoomViewSet


router = DefaultRouter()
router.register("staff", StaffViewSet)
router.register("room", RoomViewSet)
