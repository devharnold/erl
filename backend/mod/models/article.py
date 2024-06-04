#!/usr/bin/env python3

from django.db import models
from django.contrib.auth.models import User
from mod.models import Author

class Article(models.Model):
    """implementation of the Article class
    The article class will allow users to create 
    different articles and they are identified as Authors
    Params:
        Author: The user who owns the article
        Article: The object model
    """
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the article's title"""
        return self.title
    
    class Meta:
        app_label = 'mod'
