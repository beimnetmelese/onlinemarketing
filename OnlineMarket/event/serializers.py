from rest_framework import serializers
from .models import EventReview, Event,EventSaved
from user.models import User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id","organizer","title", "event_date","event_time", "event_place", "image"]

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "organizer", "description", "event_date","event_time", "event_place", "image","posted_date"]

    def create(self, validated_data):
        user = User.objects.get(id = self.context["user_id"])
        return Event.objects.create(user= user, **validated_data)
    

class GetEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id","user","organizer","title","description", "event_date","event_time", "event_place", "image"]
    
    user = GetUserSerializer()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReview
        fields = ["id","user","review", "review_date"]
    
    user = GetUserSerializer()

class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReview
        fields = ["id", "review"]
    def create(self, validated_data):
        event_id = self.context["event_id"]
        user = User.objects.get(id = self.context["user_id"])
        return EventReview.objects.create(event_id= event_id, user = user ,**validated_data)

class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSaved
        fields = ["id","event", "saved_date"]
    event = EventSerializer()

class CreateSavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSaved
        fields = ["id","saved_date"]

    def create(self, validated_data):
        event_id = self.context["event_id"]
        user = User.objects.get(id = self.context["user_id"])
        return EventSaved.objects.create(event_id= event_id, user = user ,**validated_data)