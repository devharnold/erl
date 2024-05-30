from django.test import TestCase
from django.contrib.auth.models import User
from mod.models import Post

class PostTestCase(TestCase):
    """Test case for the model post class implementation"""
    @classmethod
    def setUpTestData(cls):
        """sets up our unittest for the { Post } class model"""
        cls.test_user = User.objects.create_user(username='testuser', email='user@example.com', password='testpassword')
        cls.test_post = Post.objects.create_post(user=cls.test_user, title='Test Title', content='Test Content')

    def test_post_creation(self):
        """Test if a post is successfully created"""
        post = Post.objects.get(id=1)
        self.assertEqual(post.user.username, 'testuser')
        self.assertEqual(post.title, 'Test Title')
        self.assertEqual(post.content, 'Test Content')
        self.assertTrue(post.viewed)
        self.assertIsNotNone(post.created_at)

    def test_post_title_max_length(self):
        """Testsfor the max length of the post titles"""
        post = self.post
        max_length = self.post._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_post_created_at_auto_add_now(self):
        """Test if a post is created"""
        post = self.post
        self.assertIsNotNone(post.created_at)

    def test_post_save(self):
        """Tests if a post has saved."""
        post1 = Post.objects.create(user=self.testuser, title='Test Title 1', description='Test Description 1', viewed=True)
        post2 = Post.objects.create(user=self.testuser, title='Test Title 2', description='Test Description 2', viewed=True)
        post1.save()
        post2.save()
        self.assertTrue(post1.viewed)
        self.assertTrue(post1.viewed)
        self.assertEqual(list(Post.objects.all()), [self.post, post1, post2])

    def test_post_content_edited(self):
        """Test for editing some post content"""
        post1 = Post.objects.create(user=self.testuser, title='Test Title 1', description='Test Description 1', viewed=True)
        post2 = Post.objects.create(user=self.testuser, title='Test Title 2', description='Test Description 2', viewed=True)
        post1.save()
        post2.save()
        post2 = Post.objects.alter(user=self.testuser, title='Test Title', description='Test Description 2', viewed=True)
        post2.save()
        self.assertIsNotNone(post2.updated_at)

    def test_post_according_to_priority(self):
        """Tests for certain priority in posts"""
        post1 = Post.objects.create(user=self.testuser, title='Test Title 1', description='Test Description 1', viewed=True)
        post2 = Post.objects.create(user=self.testuser, title='Test Title 2', description='Test Description 2', viewed=True)
        post1.priority = 2
        post1.save()
        post2.priority = 1
        post2.save()
        self.assertEqual(
            post1.priority, 2,
            post2.priority, 1,
        )
