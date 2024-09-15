from django.test import TestCase
from django.contrib.auth.models import User
from mod.models import Post
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import tempfile
import os

class PostModelTestCase(TestCase):
    """Test case for the Post model."""

    @classmethod
    def setUpTestData(cls):
        # Create a user for setup
        cls.test_user = User.objects.create_user(
            username='testuser',
            email='email@example.com',
            password='testpassword'
        )

        # Create a temporary image file for setup
        cls.test_image = cls.create_test_image(size=(500, 500))
        cls.uploaded_image_url = SimpleUploadedFile(
            name='test_image.jpg',
            content=cls.test_image.read(),
            content_type='image/jpeg'
        )

        # Create a post with the uploaded image
        cls.test_post = Post.objects.create(
            title='Test Post',
            description='Test Description',
            image_url=cls.uploaded_image_url
        )

    @classmethod
    def create_test_image(cls, size=(1000, 1000)):
        """Creates a temporary test image."""
        image = Image.new('RGB', size)
        temp_image = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        image.save(temp_image, format='JPEG')
        temp_image.seek(0)
        return temp_image

    def test_post_creation(self):
        """Test to confirm if posts are successfully created."""
        post_count_before = Post.objects.count()
        post = Post.objects.create(
            title='Another test post',
            description='Another test description',
            image_url=self.uploaded_image_url
        )
        post_count_after = Post.objects.count()
        self.assertEqual(post_count_after, post_count_before + 1)

    def test_blank_image_url(self):
        """Test creation of a post with no image."""
        post_count_before = Post.objects.count()
        post = Post.objects.create(
            title='Test Title',
            description='Test Description',
            image_url=None
        )
        post_count_after = Post.objects.count()
        self.assertEqual(post_count_after, post_count_before + 1)

    def test_image_resizing(self):
        """Test for image resizing."""
        test_image = self.create_test_image(size=(1000, 1000))
        uploaded_file = SimpleUploadedFile(
            name='test_large_image.jpg',
            content=test_image.read(),
            content_type='image/jpeg'
        )
        post = Post.objects.create(
            title='Resize test post',
            description='Description',
            image_url=uploaded_file
        )
        post.refresh_from_db()
        saved_image = Image.open(post.image_url.path)

        # Check the resized dimensions; the model resizes to 800x800
        self.assertEqual(saved_image.width, 800)
        self.assertEqual(saved_image.height, 800)

        # Clean up temporary files
        test_image.close()
        os.remove(test_image.name)
        saved_image.close()
        os.remove(post.image_url.path)

