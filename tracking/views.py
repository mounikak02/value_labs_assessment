from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TrackingNumber
from .serializers import TrackingNumberSerializer
import uuid
from django.utils.text import slugify
from django.db import IntegrityError
import threading
import random
import string


# lock for thread safety
lock = threading.Lock()

def generate_tracking_number():
    # regex pattern: ^[A-Z0-9]{1,16}$
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

@api_view(['GET'])
def get_tracking_number(request):
    origin_country_id = request.query_params.get('origin_country_id')
    destination_country_id = request.query_params.get('destination_country_id')
    weight = request.query_params.get('weight')
    created_at = request.query_params.get('created_at')
    customer_id = request.query_params.get('customer_id')
    customer_name = request.query_params.get('customer_name')

    if not (origin_country_id and destination_country_id and weight and customer_id and customer_name):
        return Response({'error': 'Missing required parameters'}, status=400)

    customer_slug = slugify(customer_name)
    
    tracking_number = None
    
    with lock:
        while tracking_number is None:
            try:
                
                tracking_number = generate_tracking_number()

                # Create tracking number entry
                new_tracking = TrackingNumber(
                    tracking_number=tracking_number,
                    origin_country_id=origin_country_id,
                    destination_country_id=destination_country_id,
                    weight=weight,
                    customer_id=uuid.UUID(customer_id),
                    customer_name=customer_name,
                    customer_slug=customer_slug
                )
            except IntegrityError:
                # If there's a duplicate, reset tracking_number and retry
                tracking_number = None
                

    serializer = TrackingNumberSerializer(new_tracking)
    return Response(serializer.data)
