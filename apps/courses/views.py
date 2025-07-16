from rest_framework.viewsets import ModelViewSet

from apps.courses.serializers import CourseSerializer


from .models import Course


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
