from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class ServiceRequest(models.Model):
    customer_request_name = models.CharField(max_length=50)
    email_customer = models.EmailField(max_length=254, unique=True)
    customer_phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.email_customer}'

    class Meta:
        verbose_name = 'Service Request'
        verbose_name_plural = 'Service Requests'
