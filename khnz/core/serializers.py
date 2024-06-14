from rest_framework import serializers
from .models import ServiceRequest


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = [
            'customer_request_name',
            'email_customer',
            'customer_phone_number',
            'title',
            'description'
        ]
