from rest_framework import serializers
from .models import Arithmetic

class ArithmeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arithmetic
        fields = ['operation_type', 'x', 'y']



