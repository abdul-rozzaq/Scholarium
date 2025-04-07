from crm.models import User
from .serializer import UserSerializer


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

    
    