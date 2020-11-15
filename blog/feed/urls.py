from django.urls import path
from .views import PostsList

urlpatterns = [
    path('posts/', PostsList.as_view()),
]