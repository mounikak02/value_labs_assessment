from django.urls import path
from .views import get_tracking_number

urlpatterns = [
    path('next-tracking-number/', get_tracking_number, name='next-tracking-number'),
]