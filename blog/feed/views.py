from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from .models import Post


class ListPostsView(View):

    def get(self, request):
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, 'templates/index.html', context)


class PostDetailView(DetailView):
    template_name = "templates/post_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)





