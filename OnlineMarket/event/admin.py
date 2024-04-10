from django.contrib import admin
from .models import EventReview, Event

class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "organizer", "event_date","event_time", "event_place","posted_time"]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "event", "review", "review_date"]



admin.site.register(Event,EventAdmin)
admin.site.register(EventReview, ReviewAdmin)
