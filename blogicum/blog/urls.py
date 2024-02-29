from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),  # Detailed view of a post
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),  # Posts by category

]