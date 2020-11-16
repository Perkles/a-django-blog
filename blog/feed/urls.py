from django.urls import path
from .views import ListPostsView, PostDetailView

urlpatterns = [
    path('', ListPostsView.as_view(), name="post_list"),
    path('post/<int:id>', PostDetailView.as_view(), name="post_detail"),
]