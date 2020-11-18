from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostTestCase(TestCase):

    def setUp(self):
        user = User(username="test user", first_name='test',
                    last_name='user', email='test@test.com',
                    password='abc123')
        user.save()
        post = Post(author=user, posting_date= '1ad1321',
                    title='main title', content='Loren',
                    posted=False)
        post.save()

    def test_post_exists(self):
        post = Post.objects.all().count()
        self.assertEqual(post, 1)
