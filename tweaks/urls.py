from django.urls import path
from . import views

app_name = 'tweaks'

urlpatterns = [
    # URL for the list of all tweaks
    path('', views.tweak_list_view, name='tweak_list'),
]
