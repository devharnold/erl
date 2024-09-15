from django.test import TransactionTestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from mod.models import Post


class PostTestAPI(TransactionTestCase):
    """
    Test cases for Post API endpoints
    """
    def setUp(self):
        """
        setup data for post view tests"""
        self.user = User.objects.create(username='testuser', password='testpass')
        self.client = APIClient()
        self.post = Post.objects.create(title='Test Post', description='Test Post Description')
        self.client.login(username='testuser', password='testpass')

    def test_empty_database(self):
        response = self.client.get('api/post/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_single_post(self):
        # Upload test post
        post_data = {
            'title': 'Test Post Title',
            'description': 'Test Post Description',
            'content_type': 'image',
            'file': self.create_mock_file('test_post_image', content=b'test content', content_type='image/jpeg')
        }
        response = self.client.post('/api/post/', post_data, format='multipart')
        self.assertEqual(response.status_code, 201)
        post_id = response.data['id']

        # get uploaded test post by the post title 
        response = self.client.get(f'/api/post/{ post_id }/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test post')
        self.assertEqual(response.data['content_type'], 'image')

        updated_post_data = {
            'title': 'Updated Post Title',
            'description': 'Updated Post Description',
            'content_type': 'image',
            'file': self.create_mock_file('updated_test_post_image', content=b'updated test content', content_type='image/jpeg')
        }
        response = self.client.put(f'/api/post/{post_id}/', updated_post_data, format='multipart')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Post Title')

        # deleting a post according to the post id
        response = self.client.delete(f'/api/post/{post_id}')
        self.assertEqual(response.status_code, 204)

    def test_multiple_posts(self):
        # test case for multiple test posts uploads
        post_1_data = {
            'title': 'Test Post1',
            'description': 'Test Post Description',
            'content_type': 'image',
            'file': self.create_mock_file('test_post1_image', content=b'test content1', content_type='image/jpeg')
        }
        post_2_data = { 
            'title': 'Test Post2',
            'description': 'Test Post2 Description',
            'content_type': 'image',
            'file': self.create_mock_file('test_post2_image', content=b'test content2', content_type='image/jpeg')
        }
        response1 = self.client.post('/api/post/', post_1_data, format='multipart')
        self.assertEqual(response1.status_code, 201)
        response2 = self.client.post('/api/post', post_2_data, format='multipart')
        self.assertEqual(response2.status_code, 201)

        # get uploaded posts
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200) # expected status code 200 (OK)
        self.assertEqual(len(response.data), 2) # length of the response data


    def test_permissions(self):
        #check on non-admin users
        no_admin = User.objects.create_user(username='user', password='testpassword')
        self.client.login(username='user', password='testpassword')
        response = self.client.get('/api/post')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/api/post/', {'title': 'Post title', 'description': 'New description'}, format='multipart')
        self.assertEqual(response.status_code)

    def test_for_valid_posts(self):
        """Tests for post data validation"""
        invalid_data = {
            'content-type': 'image',
            'file': self.create_mock_file('test_image', content_type='image/jpeg')
        }
        response = self.client.post('api/post/', invalid_data, format='multipart')
        self.assertEqual(response.status_code, 400)

    def test_for_error_handling(self):
        response = self.client.get('/api/posts/8000/')
        self.assertEqual(response.status_code, 404)

        self.client.put('/api/posts/8000/', {
            'title': 'Post title',
            'description': 'Test Description',
            'file': self.create_mock_file('test_image', content=b'test content', content_type='image/jpeg')
        }, format='multipart' )
        self.assertEqual(response.status_code, 404)

        response = self.client.delete('/api/post/8000/')
        self.assertEqual(response.status_code, 404)