from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from .serializer import UserSerializer
from rest_framework import status
from .models import User
from djoser.views import UserViewSet
from rest_framework.response import Response

class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["first_name", "last_name", "username"]
    
    def get_queryset(self):
        if self.request.method == "GET":
            return User.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer







