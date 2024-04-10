from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_fieldsets = ((
        None,
        {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2","email"),
            },
        ),
    )
     
admin.site.register(User, CustomUserAdmin)
