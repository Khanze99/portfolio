from django.contrib import admin

from .models import ServiceRequest

# Register your models here.


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    pass
