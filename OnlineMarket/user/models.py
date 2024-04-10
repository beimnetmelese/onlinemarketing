from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    SEXCHOICE = [
        ("M" ,"Male"),
        ("F" ,"Female"),
        ("N" ,"Neutral"),
    ]
    profile = models.ImageField(upload_to='user/images',null=True, blank=True)
    bio = models.CharField(max_length = 255, null = True, blank = True)
    email = models.EmailField(unique = True)
    phone = models.IntegerField(null = True, blank = True)
    sex = models.CharField(max_length = 1, choices = SEXCHOICE, default = "N" )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


