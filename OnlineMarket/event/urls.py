from django.urls import path,include
from rest_framework_nested import routers
from . import views
router = routers.DefaultRouter()
router.register("event", views.EventViewSet, basename="event")

event_routers = routers.NestedDefaultRouter(router, "event", lookup = "event")
event_routers.register("review", views.ReviewViewSet, basename="event-review")
event_routers.register("save", views.SaveViewSet, basename="event-save")
urlpatterns = [
    path("", include(router.urls)),
    path("", include(event_routers.urls)),
]