from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),  # Root URL shows the posts index page
    path('<int:post_id>/', views.detail, name='detail'),
    path('create/', views.create_post, name='create'),
    path('create/', views.create_post, name='create_post'),
]
