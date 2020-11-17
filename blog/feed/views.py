from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import DetailView, CreateView
from .models import Post, Tag
from django.urls import reverse
from .forms import PostForm
from django.contrib.auth.decorators import login_required


class ListPostsView(View):

    def get(self, request, **kwargs):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        posts = Post.objects.filter(author=user)
        context = {'posts': posts, 'author': user}
        return render(request, 'index.html', context)


class PostDetailView(DetailView):
    template_name = "post_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)


# class CreatePostView(CreateView):
#     form_class = PostForm
#     template_name = 'posts/new.html'

@login_required
def create_post_view(request, username):
    if request.method == 'GET':
        author = request.user
        tags = Tag.objects.all()
        if username != author.username:
            return redirect(reverse('post_new', args=[author.username]))
        return render(request, 'posts/new.html', {'author': author, 'tags': tags})

    if request.method == 'POST':
        print('=========bateu=========')
        author = get_object_or_404(User, username=username)
        print(request.POST.get('user'))
        return redirect(reverse('post_list', args=[author.username]))
