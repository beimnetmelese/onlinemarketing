from rest_framework import serializers
from django.db.models.aggregates import Avg
from .models import Service,ServiceRating,ServiceReview,ServiceSaved
from user.models import User

class ServiceSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "title", "type", "image"]

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
class GetRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRating
        fields = ["id", "user","rate"]
    user = GetUserSerializer()

class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "title", "description", "type", "posted_date", "image"]
    
    def create(self, validated_data):
        user = User.objects.get(id = self.context["user_id"])
        return Service.objects.create(user = user, **validated_data)

class GetServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id","user","title", "description", "type", "posted_date","image","rating"]
    
    rating = serializers.SerializerMethodField(method_name= "rating_calculate")
    user = GetUserSerializer()
    
    def rating_calculate(self,service:Service):
        average = ServiceRating.objects.filter(service_id = service.id).aggregate(average=Avg("rate"))
        if average["average"] is None:
            return average["average"]
        return round(average["average"])

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceReview
        fields = ["id","user","review", "review_date"]
    
    user = GetUserSerializer()

class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceReview
        fields = ["id", "review"]
    def create(self, validated_data):
        service_id = self.context["service_id"]
        user = User.objects.get(id = self.context["user_id"])
        return ServiceReview.objects.create(service_id= service_id, user = user ,**validated_data)
    
class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRating
        fields = ["id", "rate"]
    
    def create(self, validated_data):
        service_id = self.context["service_id"]
        user_id = self.context["user_id"]

        return ServiceRating.objects.create(service_id=service_id, user_id=user_id,**validated_data)

class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSaved
        fields = ["id","service", "saved_date"]
    service = ServiceSerilizer()

class CreateSavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSaved
        fields = ["id","saved_date"]

    def create(self, validated_data):
        service_id = self.context["service_id"]
        user_id = self.context["user_id"]
        return ServiceSaved.objects.create(service_id=service_id, user_id=user_id,**validated_data)