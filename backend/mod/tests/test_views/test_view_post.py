from django.contrib.auth.models import User
from django.test import TransactionTestCase
from rest_framework.test import APIClient

class PostTestAPI(TransactionTestCase):
    """
    Test case for Post API endpoints
    """
    def setUp(self):
        """
        Setup data for the post view tests"""
        self.user = User.objects.create(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_empty_database(self):
        """Test for empty database"""
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_single_post(self):
        """Test for single post"""
        post_data = {'title': 'Test Post', 'description': 'Test Description'}
        response = self.client.post('/api/posts/', post_data, format='json')
        self.assertEqual(response.status_code, 201)
        post_id = response.data['id']

        response = self.client.get('/api/posts/{ post_id }/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Post')

        updated_post_data = {'title': 'Updated Post', 'description': 'Updated Description'}
        response = self.client.put(f'/api/posts/{'post_id'}', updated_post_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Post')

        response = self.client.delete(f'/api/posts/{'post_id'}')
        self.assertEqual(response.status_code, 200)

    """
    Test multiple posts, permission, validation, error_handling
    """

    def test_multiple_posts(self):
        """Test for multiple posts"""
        post1_data = {'title': 'Post 1', 'description': 'Description 1'}
        post2_data = {'title': 'Post 2', 'description': 'Description 2'}
        self.client.post('/api/posts/', post1_data, format='json')
        self.client.post('/api/posts/', post2_data, format='json')

        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_permission(self):

        #check on no admin users
        no_admin = User.objects.create_user(username='user', password='testpassword')
        self.client.login(username='user', password='passpass')
        response = self.client.get('/api/posts')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/api/posts/', {'title': 'New Post', 'description': 'New Description'}, format='json')
        self.assertEqual(response.status_code, )