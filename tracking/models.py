from django.db import models
import uuid


# Create your models here.
class TrackingNumber(models.Model):
    tracking_number = models.CharField(max_length=16, unique=True)
    origin_country_id = models.CharField(max_length=2)  # ISO 3166-1 alpha-2 format
    destination_country_id = models.CharField(max_length=2)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    customer_id = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=255)
    customer_slug = models.SlugField(max_length=255)

    def __str__(self) :
        return self.tracking_number
    
    
    
    