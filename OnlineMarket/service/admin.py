from django.contrib import admin
from django.contrib import admin
from .models import Service,ServiceRating,ServiceReview

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "posted_time"]
    list_filter = ["type"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "service", "review", "review_date"]

class RatingAdmin(admin.ModelAdmin):
    list_display = ["user", "service", "rate", "rated_at"]

admin.site.register(ServiceReview,ReviewAdmin)
admin.site.register(Service, ProductAdmin)
admin.site.register(ServiceRating, RatingAdmin)

