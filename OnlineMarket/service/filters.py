from django_filters.rest_framework import FilterSet
from .models import Service

class ServiceFilter(FilterSet):
    class Meta:
        model = Service
        fields = {
            "type": ["exact"],
        }