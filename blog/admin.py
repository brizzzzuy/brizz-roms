from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

# This class will auto-fill the slug field based on the title
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
