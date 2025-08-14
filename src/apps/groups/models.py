from django.db import models

from apps.courses.models import Course
from apps.users.models import User


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={"role": "teacher"})
    schedule = models.JSONField()

    def __str__(self):
        return self.name
