from django.contrib.auth.models import User
from django.test import TransactionTestCase
from rest_framework.test import APIClient

class BlogTestView(TransactionTestCase):
    """Test cases for the blog api view"""
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_empty_database(self):
        response = self.client.get('/api/blog')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_single_blog(self):
        # test for a single blog upload
        blog_data = {'title': 'TestBlog', 'description': 'TestDescription'}
        response = self.client.post('/api/blog', blog_data, format='json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/blog')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'TestBlog')

        updated_blog_data = {'title': 'UpdatedBlog', 'description': 'UpdatedDescription'}
        response = self.client.put('/api/blog', updated_blog_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'UpdatedBlog')

        response = self.client.delete('/api/blog')
        self.assertEqual(response.status_code, 200)


    def test_multiple_blog(self):
        blog1_data = {'title': 'Blog1 Title', 'description': 'Blog1 Description'}
        blog2_data = {'title': 'Blog2 Title', 'description': 'Blog2 Description'}
        response = self.client.post('/api/blog', blog1_data, format='json')
        response = self.client.post('/api/blog', blog2_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_no_admin(self):
        user = User.objects.create_user(username='testuser', password='passwordtest')
        self.client.login(username='testuser', password='passwordtest')
        response = self.client.get('/api/blog')
        self.assertEqual(response.status_code, 200)