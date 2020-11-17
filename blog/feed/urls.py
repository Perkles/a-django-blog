from django.urls import path
from .views import ListPostsView, PostDetailView, create_post_view

urlpatterns = [
    path('<str:username>', ListPostsView.as_view(), name="post_list"),
    path('<str:username>/post/<int:id>', PostDetailView.as_view(), name="post_detail"),
    path('<str:username>/new', create_post_view, name="post_new"),
]

