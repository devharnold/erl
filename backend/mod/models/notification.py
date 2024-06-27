#!/usr/bin/env python3

from django.db import models
from django.contrib.auth.models import User
from mod.models.blog import Blog
from mod.models.posts import Post

class Notification(models.Model):
    """Notification model class"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the notification by title"""
        return self.title
    
    class Meta:
        app_label = 'mod'
        ordering = ['-created_at']