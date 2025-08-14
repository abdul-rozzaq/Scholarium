from rest_framework.generics import GenericAPIView
from rest_framework.views import Response

from apps.schools.serializers import SchoolSerializer


class GetUpdateShopAPIView(GenericAPIView):
    serializer_class = SchoolSerializer

    def get_object(self):
        return self.request.tenant

    def get(self, request, *args, **kwargs):
        school = self.get_object()
        serializer = self.get_serializer(school)

        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
