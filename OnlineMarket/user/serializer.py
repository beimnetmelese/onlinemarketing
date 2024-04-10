from rest_framework import serializers
from django.db.models.aggregates import Avg
from .models import User
from product.models import Product, ProductRating
from service.models import Service,ServiceRating
from event.models import Event
from djoser.serializers import UserCreateSerializer, UserSerializer as DjoserUserSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id","title", "rating", "price", "image"]
    
    rating = serializers.SerializerMethodField(method_name= "rating_calculate")
    
    def rating_calculate(self,product:Product):
        average = ProductRating.objects.filter(product_id = product.id).aggregate(average=Avg("rate"))
        return average["average"]
    
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "title", "rating", "image"]
    
    rating = serializers.SerializerMethodField(method_name= "rating_calculate")
    
    def rating_calculate(self,service:Service):
        average = ServiceRating.objects.filter(service_id = service.id).aggregate(average=Avg("rate"))
        return average["average"]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "organizer","title", "event_date","event_place"]

class UserCreationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ["id","profile","first_name", "last_name", "username", "email","bio","sex","phone","password"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","profile", "bio","first_name", "last_name", "email", "username", "sex", "phone", "product","event", "service"]
    
    product = ProductSerializer(many=True)
    event = EventSerializer(many =True)
    service = ServiceSerializer(many=True) 

class CurrentUser(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        model = User
        fields = ["first_name", "last_name", "email", "username", "sex", "phone","profile", "bio"]
        
