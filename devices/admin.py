from django.contrib import admin
from .models import Device, Build # Import both models

admin.site.register(Device)
admin.site.register(Build)