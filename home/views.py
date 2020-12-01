from django.shortcuts import render
from feed.models import Post

def home_page_rendering(request):
    if request.method == 'GET':
        posts = Post.objects.filter(posted=True).order_by('-posting_date')
        return render(request, 'home.html', {'posts': posts})
