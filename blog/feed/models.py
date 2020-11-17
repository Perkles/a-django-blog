from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    creation_date = models.DateField(auto_now=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    tag_name = models.TextField(max_length=200)

    def __str__(self):
        return self.tag_name


class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    posting_date = models.DateField(auto_now=True)
    title = models.TextField(max_length=400)
    content = models.TextField()
    posted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', kwargs={'username': self.author.username, 'id': self.id})
