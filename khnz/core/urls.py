from django.urls import path

from .views import ServiceRequestView


urlpatterns = [
    path('service-request', ServiceRequestView.as_view(), name='service-request'),
]
