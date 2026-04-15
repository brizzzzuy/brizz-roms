# core/urls.py

from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    # When the URL is empty (the homepage), call the 'home' view
    path('', views.home, name='home'),
    path('about/', views.about, name='about_page'),

]