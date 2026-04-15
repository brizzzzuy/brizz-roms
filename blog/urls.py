from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # URL for the list of all blog posts
    path('', views.post_list_view, name='post_list'),
    # URL for a single, detailed blog post
    path('<slug:slug>/', views.post_detail_view, name='post_detail'),
]
