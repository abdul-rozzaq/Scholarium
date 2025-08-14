from django.db import models

from apps.common.models import BaseModel
from apps.schools.models import School


class Course(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
