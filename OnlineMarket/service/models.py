from django.db import models
from django.core.validators import MinValueValidator
from user.models import User

class Service(models.Model):
    TYPECHOICE = [
        ("DL","Delivery"),
        ("PC","Repair Electronics"),
        ("OT","Other"),
        ]
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "service")
    title = models.CharField(max_length = 255)
    description = models.TextField(null = True,blank =True)
    type = models.CharField(max_length = 2, choices = TYPECHOICE, default = "OT")
    posted_date = models.DateField(auto_now_add = True)
    posted_time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='service/images',null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class ServiceReview(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    review = models.TextField()
    review_date = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return self.review

class ServiceRating(models.Model):
    RATE_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    ]
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    rate = models.PositiveIntegerField(choices = RATE_CHOICES , default = 0)
    rated_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ["service", "user"]
    
    def __str__(self) -> str:
        return str(self.rate)
    
class ServiceSaved(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    saved_date = models.DateField(auto_now_add = True)
