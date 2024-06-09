#!/usr/bin/env python3

from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    """Implementation of the class Article
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"self.title"

    class Meta:
        app_label = 'mod'