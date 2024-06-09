#!/usr/bin/env python3

from django.test import TestCase
from mod.models import Article
from django.contrib.auth.models import User

"""Tests for the { Article }object model.
These tests ensure that the { Article }modelis fucntioning
as expected and that upon implementing a new feature the tests to the 
feature will be added
"""

class ArticleTestCase(TestCase):
    @classmethod:
    def setUpTestData(cls):
        