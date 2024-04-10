from django.urls import path,include
from django.views.generic import TemplateView
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("product", views.ProductViewSet, basename="product")

product_routers = routers.NestedDefaultRouter(router, "product", lookup = "product")
product_routers.register("review", views.ReviewViewSet, basename="product-review")
product_routers.register("rating", views.RatingViewSet, basename="product-rating")
product_routers.register("save", views.SaveViewSet, basename="product-save")
urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_routers.urls)),
    path("", TemplateView.as_view(template_name = "index.html"), name="home")
]