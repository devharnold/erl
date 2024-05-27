from django.test import TestCase
from mod.models import Blog
from django.contrib.auth.models import User

class BlogTestCase(TestCase):
    """Test case for the Blog class Model"""
    @classmethod
    def setUpTestData(cls):
        """sets up test data for the test operations"""
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

    #def test_blog_str(self):
    #    """tests the __str__ method of the Blog class"""
    #    self.assertEqual(str(self.blog), 'Test Blog')
#
    #def test_blog_user(self):
    #    """tests the user attribute of the Blog class"""
    #    self.assertEqual(self.blog.user, self.test_user)