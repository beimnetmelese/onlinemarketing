from django.db import models
from user.models import User
from product.models import Product
from event.models import Event
from service.models import Service


class SavedItemBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.IntegerField()  # Or appropriate field type
    saved_on = models.DateTimeField(auto_now_add=True)  # Optional: Timestamp

    class Meta:
        abstract = True  # Mark as abstract to prevent accidental creation of instances



class SavedProduct(SavedItemBase):
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
 
class SavedEvent(SavedItemBase):
    event = models.ForeignKey(Event, on_delete = models.PROTECT)
    

    
class SavedService(SavedItemBase):
    service = models.ForeignKey(Service, on_delete = models.PROTECT)
    
