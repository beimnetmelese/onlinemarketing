from django.contrib import admin
from .models import SavedProduct

class Savedadmin(admin.ModelAdmin):
    list_display = ["product", 'item_id', 'user']
    list_filter = ['product']

admin.site.register(SavedProduct, Savedadmin)
