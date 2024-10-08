from rest_framework import serializers
from .models import TrackingNumber

class TrackingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingNumber
        fields = ['tracking_number', 'created_at', 'origin_country_id', 'destination_country_id', 
                  'weight', 'customer_id', 'customer_name', 'customer_slug']