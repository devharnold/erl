#!/usr/bin/env python3

from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    """Author model class"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __Str__(self):
        """Returns the { Author's } username"""
        return self.user.username
    
    class Meta:
        app_label = 'mod'