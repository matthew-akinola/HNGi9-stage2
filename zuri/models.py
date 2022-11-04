from django.db import models
from enum import Enum

# Create your models here.
class OperationType(Enum):
    addition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"


class Arithmetic(models.Model):
    operation_type = models.CharField(
        max_length=50, choices=[(tag.name, tag.value) for tag in OperationType]
        )
    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)