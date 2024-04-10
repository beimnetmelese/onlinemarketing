from django.db import models
from django.core.validators import MinValueValidator
from user.models import User

class Product(models.Model):
    TYPECHOICE = [
        ("FD","Food"),
        ("PC","Personal Computer"),
        ("MB","Mobile"),
        ("OE", "Other Electronics"),
        ("SK","Sticker"),
        ("CL","Clothes"),
        ("ST", "Stationary"),
        ("BG","Bag"),
        ("OT","Other"),

    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "product")
    title = models.CharField(max_length = 255)
    description = models.TextField(null = True,blank =True)
    price = models.DecimalField(max_digits = 8, decimal_places = 2, validators = [MinValueValidator(1)])
    type = models.CharField(max_length = 2, choices = TYPECHOICE, default = "OT")
    posted_date = models.DateField(auto_now_add = True)
    posted_time = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='product/images',null=True, blank=True)
    rating = models.DecimalField(max_digits = 8, decimal_places = 2)

    def __str__(self) -> str:
        return self.title

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    review = models.TextField()
    review_date = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return self.review

class ProductRating(models.Model):
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
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    rate = models.PositiveIntegerField(choices = RATE_CHOICES , default = 0)
    rated_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ["product", "user"]
    
    def __str__(self) -> str:
        return str(self.rate)

class ProductSaved(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    saved_date = models.DateField(auto_now_add = True)