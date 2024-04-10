from django.shortcuts import render
from .serializers import GetEventSerializer, CreateEventSerializer, ReviewSerializer, CreateReviewSerializer, SavedSerializer, CreateSavedSerializer
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import EventReview, Event, EventSaved

class EventViewSet(ModelViewSet):
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ["organizer","title", "description"]
    ordering_fields = ["event_date","event_time"]
    def get_queryset(self):
        if self.request.method == "PUT":
            return Event.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return Event.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return Event.objects.filter(user_id = self.request.user.id)
        else:
            return Event.objects.all()
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetEventSerializer
        return CreateEventSerializer
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    def get_serializer_context(self):
        return {"user_id": self.request.user.id}

class ReviewViewSet(ModelViewSet):

    def get_queryset(self):
        if self.request.method == "PUT":
            return EventReview.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "PATCH":
            return EventReview.objects.filter(user_id = self.request.user.id)
        elif self.request.method == "DELETE":
            return EventReview.objects.filter(user_id = self.request.user.id)
        else:
            return EventReview.objects.filter(event_id = self.kwargs["event_pk"])
        
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
            "event_id" : self.kwargs["event_pk"],
            "user_id" : self.request.user.id
            }


class SaveViewSet(CreateModelMixin, ListModelMixin ,RetrieveModelMixin, DestroyModelMixin, GenericViewSet):

    def get_queryset(self):
        if self.request.method == "DELETE":
            return EventSaved.objects.filter(user_id = self.request.user.id)
        else:
            return EventSaved.objects.filter(user_id = self.request.user.id)
        
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
            "event_id" : self.kwargs["event_pk"],
            "user_id" : self.request.user.id
            }