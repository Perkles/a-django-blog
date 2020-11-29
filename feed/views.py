from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView
from .models import Post, Tag
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin


class ListPostsView(View):

    def get(self, request, **kwargs):
        username = self.kwargs['username']
        user_logged = self.request.user.username
        user = get_object_or_404(User, username=username)

        if user_logged == username:
            posts = Post.objects.filter(author=user)
        else:
            posts = Post.objects.filter(author=user, posted=True)

        context = {'posts': posts, 'author': user, 'user_logged': user_logged}
        return render(request, 'post/index.html', context)


class DetailPostView(DetailView):
    template_name = "post/post_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)


class DeletePostView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post/confirm_post_delete.html"

    def test_func(self):
        return self.request.user.username == self.kwargs.get("username")

    def get_success_url(self):
        return reverse('post-list', args=[self.request.user.username])

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)


class UpdatePostView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post/update.html"

    def test_func(self):
        return self.request.user.username == self.kwargs.get("username")

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)


class PublishPostView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['posted']
    template_name = "post/update.html"

    def test_func(self):
        return self.request.user.username == self.kwargs.get("username")

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)


class TagCreateView(UserPassesTestMixin, CreateView):
    model = Tag
    fields = ['tag_name']
    template_name = "tag/new.html"

    def get_success_url(self):
        return reverse('post-new', args=[self.request.user.username])

    def test_func(self):
        return self.request.user.username == self.kwargs.get("username")

@login_required
def create_post_view(request, username):
    if request.method == 'GET':
        author = request.user
        tags = Tag.objects.all()
        if username != author.username:
            return redirect(reverse('post-new', args=[author.username]))
        return render(request, 'post/new.html', {'author': author, 'tags': tags})

    if request.method == 'POST':
        post_tag = get_object_or_404(Tag, id=request.POST.get('tag'))
        new_post = Post.objects.create(
            author=request.user,
            title=request.POST.get('title'),
            content=request.POST.get('content'),
        )
        new_post.tags.add(post_tag)
        return redirect(reverse('post-list', args=[request.user.username]))

