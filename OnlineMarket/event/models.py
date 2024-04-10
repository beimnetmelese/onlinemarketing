from django.db import models
from django.core.validators import MinValueValidator
from user.models import User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "event")
    organizer = models.CharField(max_length= 255)
    title = models.CharField(max_length = 255)
    description = models.TextField(null = True,blank =True)
    event_date = models.DateField() 
    event_time = models.TimeField()
    event_place = models.CharField(max_length = 255)
    posted_date = models.DateField(auto_now_add = True)
    posted_time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='event/images',null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class EventReview(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    review = models.TextField()
    review_date = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return self.review

class EventSaved(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    saved_date = models.DateField(auto_now_add = True)