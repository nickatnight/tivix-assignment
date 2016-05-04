from django.test import TestCase
from models import Post
import os


class PostModelTest(TestCase):
    def test_str_representation(self):
        post = Post(title='My First Post')
        self.assertEqual(str(post), post.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Post._meta.verbose_name_plural), "Post Entries")


class PageTests(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin_page(self):
        response = self.client.get('/admin/login/?next=/admin/')
        self.assertEqual(response.status_code, 200)
