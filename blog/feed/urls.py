from django.urls import path
from .views import ListPostsView, PostDetailView

urlpatterns = [
    path('<str:username>', ListPostsView.as_view(), name="post_list"),
    path('<str:username>/post/<int:id>', PostDetailView.as_view(), name="post_detail"),
]

