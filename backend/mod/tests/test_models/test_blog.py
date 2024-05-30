from django.test import TestCase
from mod.models import Blog
from django.contrib.auth.models import User

class BlogTestCase(TestCase):
    """Test case for the Blog class Model"""
    @classmethod
    def setUpTestData(cls):
        """sets up ou unittest for the { Blog } class model"""
        cls.test_user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        cls.blog = Blog.objects.create(user=cls.test_user, title='Test Blog', content='This is a test blog')

    def test_blog_create(self):
        """Test for blog creation"""
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.user.username, 'testuser')
        self.assertEqual(blog.title, 'Test Blog')
        self.assertEqual(blog.content, 'This is a test blog')
        self.assertIsNotNone(blog.created_at)

    def test_blog_title_max_length(self):
        """tests for the max length set for the blogs titles"""
        blog = self.blog
        max_length = self.blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_blog_created_auto_add_now(self):
        """test for auto-add the blog model class"""
        blog = self.blog
        self.assertIsNotNone(blog.created_at)

    def test_blog_save(self):
        """Tests if a blog has saved."""
        blog1 = Blog.objects.create(user=self.testuser, title='Test Title 1', description='Test Description 1', viewed=True)
        blog2 = Blog.objects.create(user=self.testuser, title='Test Title 2', description='Test Description 2', viewed=True)
        blog1.save()
        blog2.save()
        self.assertTrue(blog1.viewed)
        self.assertTrue(blog1.viewed)
        self.assertEqual(list(Blog.objects.all()), [self.post, blog1, blog2])

    def test_post_content_edited(self):
        """Test for editing some post content"""
        blog1 = Blog.objects.create(user=self.testuser, title='Test Title 1', description='Test Description 1', viewed=True)
        blog2 = Blog.objects.create(user=self.testuser, title='Test Title 2', description='Test Description 2', viewed=True)
        blog1.save()
        blog2.save()
        blog2 = Blog.objects.alter(user=self.testuser, title='Test Title', description='Test Description 2', viewed=True)
        blog2.save()
        self.assertIsNotNone(blog2.updated_at)