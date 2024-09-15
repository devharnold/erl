from django.test import TransactionTestCase
from mod.models import Article
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class ArticleAPITest(TransactionTestCase):
    """Article Views test case"""
    def setUp(self):
        """setUp data for our testcase"""
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.client = APIClient()
        self.article = Article.objects.create(title='Test Article', description='Test Article Description')
        self.client.login(username='testuser', password='testpassword')

    def test_empty_article_db(self):
        """test for empty database"""
        response = self.client.get('/api/article')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_for_single_article(self):
        article_data = {'title': 'Test Article', 'description': 'Test Description'}
        response = self.client.post('/api/article', article_data, format='json')
        self.assertEqual(response.status_code, 201)
        article_id = response.data['id']

        # get article by the title
        response = self.client.get('/api/article/'f'{article_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'title': 'Test Title'})

        # test for updated article
        updated_article_data = {'title': 'Updated Test Article', 'description': 'Updated Test Description'}
        response = self.client.put('/api/article/', updated_article_data, format='json')
        self.asssertEqual(response.status_code, 200)
        
        # test for delete article
        self.client.delete('/api/article/'f'{article_id}')
        self.assertEqual(response.status_code, 200)

    
    def test_multiple_articles(self):
        # test case for multiple articles
        article_1_data = {'title': 'Test Article 1', 'description': 'Test Description'}
        article_2_data = {'title': 'Test Article 2', 'description': 'Test Description'}
        response = self.client.post('/api/article/', article_1_data, format='json')
        response = self.client.post('/api/article/', article_2_data, format='json')
        self.assertEqual(response.status_code, 201)

        response1 = self.client.get('/api/article/article_1_data/')
        self.assertEqual(response1.status_code, 200)

        response2 = self.client.get('/api/article/article_2_data/')
        self.assertEqual(response2.status_code, 200)

        # get uploaded articles
        response = self.client.get('/api/article/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_for_error_handling(self):
        # error handling tests
        response = self.client.get('/api/article/456065/')
        self.assertEqual(response.status_code, 404)

        response = self.client.put('/api/article/456065/', {
            'title': 'Trial Update Test Article',
            'description': 'Trial Update',
        }, format='json')
        self.assertEqual(response.status_code, 404) # indicating that the article with that id does not exist