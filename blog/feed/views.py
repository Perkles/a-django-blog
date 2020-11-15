from django.views.generic import ListView
from .models import Post


class PostsList(ListView):
    model = Post


