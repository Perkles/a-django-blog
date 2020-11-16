from django.urls import path
from .views import ListPostsView

urlpatterns = [
    path('blog', ListPostsView.as_view(), name="blog"),
]