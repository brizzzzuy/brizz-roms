from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tweak

class TweakAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    search_fields = ['name', 'description']

admin.site.register(Tweak, TweakAdmin)
