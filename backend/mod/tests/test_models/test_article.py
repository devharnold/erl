#!/usr/bin/env python3

from django.test import TestCase
from django.contrib.auth.models import User
from mod.models.article import Article
from django.core.exceptions import ValidationError

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

    def test_create_article(self):
        """Test for valid article creation"""
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

    def test_article_blank_title(self):
        with self.assertRaises(ValidationError) as context:
            article = Article.objects.create(
            title='Test Article',
            description='Test Description',
            content='Test Content written for article'
        )
        article.full_clean()
        self.assertIn(
            'Title cannot be blank.', context.exception.messages
        )

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

    def test_unique_content_per_article(self):
        """test for unique article content"""
        article1 = Article.objects.create(
            title = 'Test Title',
            description = 'Test Description',
            content = 'Unique Content'
        )
        article2 = Article.objects.create(
            title = 'Test Title2',
            description = 'Test Description2',
            content = 'Unique Content'
        )
        with self.assertRaises(ValidationError) as context:
            article2.full_clean()
            article2.save()
        self.assertIn(
            'Article with this content already exists',
            context.exception.messages
        )