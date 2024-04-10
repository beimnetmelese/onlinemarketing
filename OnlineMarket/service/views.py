from django.shortcuts import render
from .serializer import CreateServiceSerializer,GetServiceSerializer, ReviewSerializer, CreateReviewSerializer, CreateRatingSerializer, GetRatingSerializer,SavedSerializer,CreateSavedSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Service,ServiceRating,ServiceReview,ServiceSaved
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin,RetrieveModelMixin,ListModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from .filters import ServiceFilter
from django.db import IntegrityError
from rest_framework.response import Response
from django.http import JsonResponse


class ServiceViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ServiceFilter
    search_fields = ["title", "description"]
    ordering_fields = ["posted_time", "rating"]

    def get_queryset(self):
        if self.request.method == "PUT":
            return Service.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return Service.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return Service.objects.filter(user_id = self.request.user.id)
        else:
            return Service.objects.all()
        
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetServiceSerializer
        return CreateServiceSerializer
        
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
    

class ReviewViewSet(ModelViewSet):

    def get_queryset(self):
        if self.request.method == "PUT":
            return ServiceReview.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return ServiceReview.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return ServiceReview.objects.filter(user_id = self.request.user.id)
        else:
            return ServiceReview.objects.filter(service_id = self.kwargs["service_pk"])
        
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReviewSerializer
        return CreateReviewSerializer

    def get_serializer_context(self):
        return {
            "service_id" : self.kwargs["service_pk"],
            "user_id" : self.request.user.id
            }

class RatingViewSet(ModelViewSet):
    try:
        def get_serializer_class(self):
            if self.request.method == "GET":
                return GetRatingSerializer
            return CreateRatingSerializer
        def get_queryset(self):
            if self.request.method == "PUT":
                return ServiceRating.objects.filter(user_id = self.request.user.id)
            elif self.request.method == "PATCH":
                return ServiceRating.objects.filter(user_id = self.request.user.id)
            elif self.request.method == "DELETE":
                return ServiceRating.objects.filter(user_id = self.request.user.id)
            else:
                return ServiceRating.objects.filter(service_id = self.kwargs["service_pk"])
        def get_permissions(self):
            if self.request.method == "GET":
                return [AllowAny()]
            return [IsAuthenticated()]
        def get_serializer_context(self):
            return {
                "service_id" : self.kwargs["service_pk"],
                "user_id" : self.request.user.id
                }
    except IntegrityError:
        def error(request):
            return Response({'error': "You can't rate twice"}, status=400)

class SaveViewSet(CreateModelMixin, ListModelMixin ,RetrieveModelMixin, DestroyModelMixin, GenericViewSet):

    def get_queryset(self):
        if self.request.method == "DELETE":
            return ServiceSaved.objects.filter(user_id = self.request.user.id)
        else:
            return ServiceSaved.objects.filter(user_id = self.request.user.id)
        
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SavedSerializer
        return CreateSavedSerializer

    def get_serializer_context(self):
        return {
            "service_id" : self.kwargs["service_pk"],
            "user_id" : self.request.user.id
            }
