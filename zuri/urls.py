from django.urls import path
from .views import arithmetic_operation

urlpatterns = [
    path('', arithmetic_operation, name='operation')
]