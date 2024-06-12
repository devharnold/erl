#!/usr/bin/env python3

from django.test import TestCase
from django.contrib.auth.models import User
from mod.models import Blog

class BlogTestCase(TestCase):
    """testcase for the { Blog } object model"""
    @classmethod
    def setUpTestData(cls):
        cls.test_user=User.objects.create_user(
            username='testuser',
            email='email@example.com',
            password='testpassword'
        )
        cls.test_blog=Blog.objects.create(
            user=cls.test_user,
            title='Test Title',
            location='Test Location',
            description='Test Description'
        )
        #cls.test_user = User.objects.create_user(username='testuser', email='email@example.com', passsword='testpassword')
        #cls.test_blog = Blog.objects.create_blog(user=cls.test_user, title='Test Title', location='Test Location', description='Test Description')

    def test_blog_creation (self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.title, 'Test Title')
        self.assertEqual(blog.location, 'Test Location')
        self.assertEqual(blog.description, 'Test Description')
        self.assertIsNotNone(blog.created_at)

    def test_blog_created_auto_now_add(self):
        blog = self.test_blog
        self.assertIsNotNone(blog.created_at)

    def test_blog_save(self):
        blog_1 = Blog.objects.create(
            user=self.test_user,
            title='Test Title 1',
            location='Test Location 1',
            description='Test Description 1'
        )
        blog_2 = Blog.objects.create(
            user=self.test_user,
            title='Test Title 2',
            location='Test Location 2',
            description='Test Description 2'
        )
        blog_1.save()
        blog_2.save()
        blogs = Blog.objects.order_by('created_at')
        self.assertEqual(list(blogs), [self.test_blog, blog_1, blog_2])