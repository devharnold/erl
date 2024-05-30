#!/usr/bin/env python3

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Implementation of the model class post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the post by title"""
        return self.title
    
    class Meta:
        app_label = 'mod'
        ordering = ['-created_at']