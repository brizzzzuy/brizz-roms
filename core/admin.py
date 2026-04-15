from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TeamMember # Import the new model

# Register the TeamMember model
admin.site.register(TeamMember)
