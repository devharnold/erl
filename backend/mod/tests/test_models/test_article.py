#!/usr/bin/env python3

from django.test import TestCase
from django.contrib.auth.models import User
from mod.models.article import Article

class ArticleTestCase(TestCase):
    """Article class TestCase"""
    @classmethod
    def setUpTestData(cls):
        """Set up test data"""
        cls.test_user = User.objects.create_user(
            username='testuser',
            email='email@example.com',
            password='12345'
        )
        cls.test_article = Article.objects.create(
            user=cls.test_user,
            title='Test Article',
            description='Test Description',
            content='Test Content'
        )

    def test_article_creation(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.user.username, 'testuser')
        self.assertEqual(article.title, 'Test Article')
        self.assertEqual(article.description, 'Test Description')
        self.assertEqual(article.content, 'Test Content')
        self.assertIsNotNone(article.created_at)

    def test_article_title_max_length(self):
        article = self.test_article
        max_length = self.test_article._meta.get_field('title').max_length
        self.assertEqual(max_length, 225)

    def test_article_created_at_auto_now_add(self):
        article = self.test_article
        self.assertIsNotNone(article.created_at)

    def test_article_save(self):
        article_1 = Article.objects.create(
            user = self.test_user,
            title = 'Test Article 1',
            description = 'Test Description 1',
            content = 'Test Content 1'
        )
        article_2 = Article.objects.create(
            user = self.test_user,
            title = 'Test Article 2',
            description = 'Test Description 2',
            content = 'Test Content 2'
        )
        articles = Article.objects.order_by('created_at')
        self.assertEqual(list(articles), [self.test_article, article_1, article_2])