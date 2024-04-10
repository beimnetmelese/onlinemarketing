from django.urls import path,include
from rest_framework_nested import routers
from . import views

route  = routers.DefaultRouter()
route.register("user", views.UserViewSet, basename="user")

urlpatterns = [
    path("", include(route.urls)),

]