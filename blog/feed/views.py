from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import DetailView
from .models import Post


class ListPostsView(View):

    def get(self, request, **kwargs):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        posts = Post.objects.filter(author=user)
        context = {'posts': posts}
        return render(request, 'index.html', context)


class PostDetailView(DetailView):
    template_name = "post_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)





