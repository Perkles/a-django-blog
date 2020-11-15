from django.contrib import admin
from .models import Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'posted')

@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)


