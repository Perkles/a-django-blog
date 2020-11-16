from django.shortcuts import render
from django.views import View
from .models import Post


class ListPostsView(View):

    def get(self, request):
        posts = Post.objects.all()
        context = {'posts': posts}
        return render(request, 'templates/index.html', context)


