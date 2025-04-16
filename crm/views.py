from .models import User, Room
from .serializer import UserSerializer, RoomSerializer
from .permissions import IsManagerOrAdmin

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import Response


class StaffViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    @action(["GET"], detail=False)
    def get_me(self, request, *args, **kwargs):
        return Response(self.get_serializer(request.user).data)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsManagerOrAdmin]
