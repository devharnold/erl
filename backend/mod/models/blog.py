#!/usr/bin/env python3

from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
    """implementation of the Blog model class"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    #author = models.ForeignKey(Author, related_name='blog', on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the blog title"""
        return self.title
    
    class Meta:
        app_label = 'mod'
        ordering = ['-created_at'] #Orders blogs