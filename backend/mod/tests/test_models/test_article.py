#!/usr/bin/env python3

from django.test import TestCase
from mod.models.article import Article
from django.contrib.auth.models import User
from mod.models import Author

class ArticleTestCase(TestCase):
    """Testcase for the { Article } object model,
    Ensures that functions within this model work as expected
    """
    @classmethod
    def setUpClass(cls):
        """SetUp test data"""
        cls.test_author = Author.objects.create(author='testauthor', email='email@example.com', password='testpassword')
        cls.test_article = Article.objects.create(author=cls.test_author, title='Test Title', body='Test Content')

    def test_aricle_create(self):
        article = Article.objects.get(id=1)
        self.assertEqual(
            article.author, 'testauthor',
            article.title, 'Test Title',
            article.body, 'Test Content',
        )
        self.assertTrue(article.read)
        self.assertIsNotNone(article.created_at)

    def test_article_auto_now_add(self):
        article = self.article
        self.assertIsNotNone(article.created_at)

    def test_article_title_max_length(self):
        article = self.article
        max_length = self.article._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_article_order(self):
        article_1 = Article.objects.create(
            author=self.test_author,
            title='Test Title 1',
            body='Test Message 1',
        )
        article_2 = Article.objects.create(
            author=self.test_author,
            title='Test Title 2',
            body='Test Messsage 2',
        )
        articles = Article.objects.all()
        self.assertEqual(list(articles), [self.article, article_1, article_2])

    def test_article_save(self):
        article1 = Article.objects.create(
            author=self.test_author,
            title='Test Title 1',
            body='Test Message 1',
        )
        article2 = Article.objects.create(
            author=self.test_author,
            title='Test Title 2',
            body='Test Messsage 2',
        )
        article1.save()
        article2.save()
        self.assertTrue(
            article1.read,
            article2.read,
        )
        self.assertEqual(list(Article.objects.all()), [self.article, article1, article2])

    def test_article_category(self):
        article1 = Article.objects.create(
            author=self.test_author,
            title='Test Title 1',
            body='Test Message 1',
            category='Test Category'
        )
        article2 = Article.objects.create(
            author=self.test_author,
            title='Test Title 2',
            body='Test Messsage 2',
            category='Test Category #1'
        )
        article1.category = 'Test Category'
        article1.save()
        article2.category = 'Test Category #1'
        article2.save()
        self.assertEqual(
            article1.category, 'Test Category',
            article2.category, 'Test Category #1',
        )

    def test_article_by_readers_pick(self):
        article1 = Article.objects.create(
            author=self.test_author,
            title='Test Title 1',
            body='Test Message 1',
            category='Test Category'
        )
        article2 = Article.objects.create(
            author=self.test_author,
            title='Test Title 2',
            body='Test Messsage 2',
            category='Test Category #1'
        )
        article1.User.pick = 'Education'
        article2.User.pick = 'Music'
        self.assertTrue(
            article1.User.pick, 'Education',
            article2.User.pick, 'Music',
        )
        self.assertIsNotNone(
            article1.created_at,
            article2.created_at,
        )