from django.test import TransactionTestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class PostTestAPI(TransactionTestCase):
    """
    Test cases for Post API endpoints
    """
    def setUp(self):
        """
        setup data for post view tests"""
        self.user = User.objects.create(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_empty_database(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_single_post(self):
        # Upload test post
        post_data = {'title': 'Test post', 'description': 'Test Description'}
        response = self.client.post('/api/posts/', post_data, format='json')
        self.assertEqual(response.status_code, 201)
        post_id = response.data['id']

        # get uploaded test post by the post title 
        response = self.client.get('/api/posts/{ post_id }/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test post')

        # update test post data
        updated_post_data = {'title': 'Updated post data', 'description': 'Updated Description'}
        response = self.client.put('/api/posts/', updated_post_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test post')

        # delete a specific test post specified by the post id
        response = self.client.delete(f'/api/posts/{'post_id'}')
        self.assertEqual(response.status_code, 200)

    def test_multiple_posts(self):
        # test case for multiple test posts uploads
        post1_data = {'title': 'Test post1', 'description': 'Test description1'}
        post2_data = {'title': 'Test post2', 'description': 'Test description2'}
        self.client.post('/api/posts/', post1_data, format='json')
        self.client.post('/api/posts/', post2_data, format='json')

        # get multiple test uploads test case
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_permissions(self):
        #check on non-admin users
        no_admin = User.objects.create_user(username='user', password='testpassword')
        self.client.login(username='user', password='testpassword')
        response = self.client.get('/api/posts')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/api/posts/', {'title': 'Post title', 'description': 'New description'}, format='json')
        self.assertEqual(response.status_code)