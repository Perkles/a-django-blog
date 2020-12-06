from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import ListPostsView, DetailPostView, DeletePostView, UpdatePostView, PublishPostView, TagCreateView,\
    create_post_view

urlpatterns = [
    path('<str:username>', ListPostsView.as_view(), name="post-list"),
    path('<str:username>/new', create_post_view, name="post-new"),
    path('<str:username>/post/<int:id>', DetailPostView.as_view(), name="post-detail"),
    path('<str:username>/post/<int:id>/edit', login_required(UpdatePostView.as_view()), name="post-update"),
    path('<str:username>/post/<int:id>/publish', login_required(PublishPostView.as_view()), name="post-publish"),
    path('<str:username>/post/<int:id>/delete', login_required(DeletePostView.as_view()), name="post-delete"),
    path('<str:username>/tag/new', login_required(TagCreateView.as_view()), name="tag-new"),
]


