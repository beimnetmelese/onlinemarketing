from django.urls import path,include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("service", views.ServiceViewSet, basename="service")

service_routers = routers.NestedDefaultRouter(router, "service", lookup = "service")
service_routers.register("review", views.ReviewViewSet, basename="service-review")
service_routers.register("rating", views.RatingViewSet, basename="service-rating")
service_routers.register("save", views.SaveViewSet, basename="service-save")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(service_routers.urls)),
]