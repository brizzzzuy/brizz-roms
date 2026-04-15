# devices/urls.py
from django.urls import path
from . import views

app_name = 'devices' # This is for URL namespacing

urlpatterns = [
    path('', views.device_list_view, name='device_list'),
    path('<str:codename>/', views.device_detail_view, name='device_detail'),
]